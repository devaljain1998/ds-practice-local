from copy import deepcopy
import json
from typing import Protocol
import time
import unittest
from unittest.mock import patch

REQUIRED_KEYS = {'user_id', 'event_type', 'timestamp'}
VALID_EVENT_TYPES = {'login', 'logout', 'purchase'}

class FilterInterface(Protocol):
    def apply(self, row: dict) -> bool:
        ...


class RequiredKeysFilter:
    def apply(self, row: dict) -> bool:
        row_keys = set(row.keys())
        for required_key in REQUIRED_KEYS:
            if required_key not in row_keys:
                return False
        return True

class UserIdFilter:
    def apply(self, row: dict) -> bool:
        user_id = row.get('user_id')
        if not user_id or not type(user_id) is int or not user_id > 0:
            return False
        return True

class ValidEventTypeFilter:
    def apply(self, row: dict) -> bool:
        event_type = row.get('event_type')
        if not event_type or not isinstance(event_type, str) or not event_type in VALID_EVENT_TYPES:
            return False
        return True

class FutureTimeRowFilter:
    def apply(self, row: dict) -> bool:
        current_time = time.time()
        timestamp = row.get('timestamp')
        if not timestamp or not type(timestamp) is int or not timestamp <= current_time:
            return False
        return True
        

class LogProcessor:
    def __init__(self, filters: list[FilterInterface]):
        self.filters: list[FilterInterface] = []
        for filter in filters:
            self.filters.append(filter)
        

    def process_logs(self, log_data: list[dict]) -> list[dict]:
        result = []
        for log in log_data:
            passed = True
            # chain filtering:  
            for filter in self.filters:
                if (ok := filter.apply(log)) == False:
                    passed = False
                    break

            if passed:
                result.append(log)

        return result        





def process_logs(log_data) -> list[dict]:
    log_processor = LogProcessor(
        filters= [
            RequiredKeysFilter(),
            UserIdFilter(),
            ValidEventTypeFilter(),
            FutureTimeRowFilter()
        ]
    )

    if isinstance(log_data, str):
        try:
            log_data = json.loads(log_data)
        except json.JSONDecodeError:
            print('not able to decode json')
            return []

    return log_processor.process_logs(log_data)


class TestProcessLogs(unittest.TestCase):
    """Tests for the pictured prompt, using a fixed Unix time.

    Input is a list of dictionaries or its JSON representation. Keep records
    with all required keys, a positive integer user_id, a supported string
    event_type, and an integer timestamp <= now. Booleans are not integers
    for this contract. Preserve input order, duplicates, and extra fields;
    return a new list without changing the input. Invalid JSON and non-list
    inputs are unspecified by the prompt and are not tested here.

    Run this file directly to execute the tests. These tests do not change
    the implementation above.
    """

    NOW = 1_800_000_000

    def setUp(self):
        clock = patch.object(time, "time", return_value=self.NOW)
        clock.start()
        self.addCleanup(clock.stop)

    def make_log(self, **overrides):
        log = {"user_id": 101, "event_type": "login", "timestamp": self.NOW - 60}
        log.update(overrides)
        return log

    def test_sample_from_picture(self):
        logs = [
            {"user_id": 101, "event_type": "login", "timestamp": 1665792000},
            {"user_id": 102, "event_type": "purchase", "timestamp": 1665792120},
            {"user_id": -1, "event_type": "logout", "timestamp": 1665792180},
            {"user_id": 103, "timestamp": 1665792240},
            {
                "user_id": 104,
                "event_type": "purchase",
                "timestamp": 1665792300,
                "additional_data": "extra",
            },
            {"user_id": 105, "event_type": "invalid_event", "timestamp": 1665792360},
            {"user_id": 105, "event_type": "invalid_event", "timestamp": 4916942417},
        ]
        self.assertEqual(process_logs(logs), [logs[0], logs[1], logs[4]])

    def test_json_input_filters_invalid_records(self):
        valid = self.make_log()
        logs = [valid, self.make_log(user_id=-1), self.make_log(timestamp=self.NOW + 1)]
        self.assertEqual(process_logs(json.dumps(logs)), [valid])

    def test_empty_inputs_return_empty_list(self):
        for log_data in ([], "[]"):
            with self.subTest(log_data=log_data):
                self.assertEqual(process_logs(log_data), [])

    def test_each_required_key_must_be_present(self):
        for key in ("user_id", "event_type", "timestamp"):
            with self.subTest(missing_key=key):
                log = self.make_log()
                del log[key]
                self.assertEqual(process_logs([log]), [])

    def test_empty_record_is_removed(self):
        self.assertEqual(process_logs([{}]), [])

    def test_user_id_must_be_a_positive_integer(self):
        for user_id in (0, -1, -100, 1.0, "101", None, True, False):
            with self.subTest(user_id=user_id):
                self.assertEqual(process_logs([self.make_log(user_id=user_id)]), [])

    def test_smallest_positive_user_id_is_valid(self):
        log = self.make_log(user_id=1)
        self.assertEqual(process_logs([log]), [log])

    def test_all_supported_event_types_are_valid(self):
        for event_type in ("login", "logout", "purchase"):
            with self.subTest(event_type=event_type):
                log = self.make_log(event_type=event_type)
                self.assertEqual(process_logs([log]), [log])

    def test_unsupported_or_non_string_event_types_are_removed(self):
        for event_type in ("invalid_event", "LOGIN", " login", "", None, 1, True, [], {}):
            with self.subTest(event_type=event_type):
                self.assertEqual(process_logs([self.make_log(event_type=event_type)]), [])

    def test_past_and_current_timestamps_are_valid(self):
        # The prompt imposes no lower bound on an integer Unix timestamp.
        for timestamp in (-1, 0, self.NOW - 1, self.NOW):
            with self.subTest(timestamp=timestamp):
                log = self.make_log(timestamp=timestamp)
                self.assertEqual(process_logs([log]), [log])

    def test_future_timestamps_are_removed_with_other_fields_valid(self):
        # The picture's future record also has an invalid event type; isolate
        # the time rule here so an event-type check cannot mask a broken clock check.
        for timestamp in (self.NOW + 1, 4916942417):
            with self.subTest(timestamp=timestamp):
                self.assertEqual(process_logs([self.make_log(timestamp=timestamp)]), [])

    def test_non_integer_timestamps_are_removed(self):
        for timestamp in (str(self.NOW - 1), self.NOW - 0.5, "", None, True, False):
            with self.subTest(timestamp=timestamp):
                self.assertEqual(process_logs([self.make_log(timestamp=timestamp)]), [])

    def test_all_invalid_records_return_empty_list(self):
        logs = [
            {},
            self.make_log(user_id=0),
            self.make_log(event_type="invalid_event"),
            self.make_log(timestamp=self.NOW + 1),
        ]
        self.assertEqual(process_logs(logs), [])

    def test_valid_records_keep_input_order_and_duplicates(self):
        first = self.make_log(user_id=2, timestamp=self.NOW - 1)
        second = self.make_log(user_id=1, event_type="purchase", timestamp=0)
        logs = [first, self.make_log(user_id=-1), second, first.copy()]
        self.assertEqual(process_logs(logs), [first, second, first])

    def test_extra_fields_are_preserved(self):
        log = self.make_log(additional_data={"source": "mobile", "tags": ["sale"]})
        self.assertEqual(process_logs([log]), [log])

    def test_returns_new_list_without_modifying_input(self):
        for logs in ([], [self.make_log()], [self.make_log(user_id=-1), self.make_log()]):
            with self.subTest(logs=logs):
                original = deepcopy(logs)
                result = process_logs(logs)
                self.assertIsInstance(result, list)
                self.assertIsNot(result, logs)
                self.assertEqual(logs, original)

    def test_repeated_calls_have_independent_results(self):
        first = self.make_log(user_id=1)
        second = self.make_log(user_id=2, event_type="logout")
        first_result = process_logs([first])
        self.assertEqual(process_logs([second]), [second])
        self.assertEqual(process_logs([]), [])
        self.assertEqual(first_result, [first])


if __name__ == "__main__":
    unittest.main(verbosity=2)
