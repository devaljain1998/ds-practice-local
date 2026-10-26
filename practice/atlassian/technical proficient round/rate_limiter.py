from typing import Protocol


class RateLimiterInterface(Protocol):
    def should_allow_request(time_bucket: int) -> bool:
        ...


class RateLimiter:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.time_bucket = None
        self.count = 0

    def should_allow_request(self, time_bucket: int) -> bool:
        # new time bucket - reset the previous one
        if time_bucket != self.time_bucket:       
            self._reset_bucket(time_bucket=time_bucket)

        self.count += 1
        return self.count <= self.capacity

    def _reset_bucket(self, time_bucket: int):
        self.time_bucket = time_bucket
        self.count = 0
