"""
Imagine you are given a stream of content ids along with an associated action to be performed on them
Example of contents are video, pages, posts etc. There cam be two actions associated with a content id:
• increasePopularity -> increases the popularity of the content by 1. The popularity increases when someone comments on the content or likes the comtent
• decreasePopularity-> decreases the popularity of the content by 1. The popularity decreases when a spam bot’s/users comments are deleted from the content or its likes are removed from the content
• content ids are positive integers
Implement a class that can return the mostPopular content id at any time while consuming the stream of content ids and its associated action. If there are no contentIds with popularity greater than 0, return -1
"""
import unittest

from sortedcontainers import SortedSet


class ContentService:
    def __init__(self):
        self.content_score = {}
        self.sortedset = SortedSet()

    def increase_popularity(self, content_id: int):
        if content_id in self.content_score:
            key = (self.content_score[content_id], content_id)
            self.sortedset.remove(key)
        self.content_score[content_id] = self.content_score.get(content_id, 0) + 1
        key = (self.content_score[content_id], content_id)
        self.sortedset.add(key)

    def decrease_popularity(self, content_id: int):
        if content_id in self.content_score:
            key = (self.content_score[content_id], content_id)
            self.sortedset.remove(key)
        self.content_score[content_id] = self.content_score.get(content_id, 0) - 1
        key = (self.content_score[content_id], content_id)
        self.sortedset.add(key)
    
    def most_popular_content(self) -> list[int]:
        result = []
        for i in range(len(self.sortedset)-1, -1, -1):
            score, content_id = self.sortedset[i]
            if score <= 0:
                break
            result.append(content_id)
            if len(result) == 10:
                return result
        return result if result else []


if __name__ == '__main__':
    class ContentServiceTests(unittest.TestCase):
        def test_popularity_streams(self):
            # Preserve the list interface: positive scores only, highest first,
            # at most 10 IDs. Equal scores use descending content ID order,
            # matching the reverse ordering of (score, content_id) tuples.
            cases = [
                ('empty service', [], []),
                ('single content', [('increase', 42)], [42]),
                ('repeated increases do not duplicate IDs',
                 [('increase', 42)] * 3, [42]),
                ('scores take priority over content IDs',
                 [('increase', 99), ('increase', 1), ('increase', 1)],
                 [1, 99]),
                ('equal scores use descending IDs',
                 [('increase', 2), ('increase', 7), ('increase', 4)],
                 [7, 4, 2]),
                ('decreasing the leader changes the ranking',
                 [('increase', 1), ('increase', 1), ('increase', 2),
                  ('decrease', 1)], [2, 1]),
                ('zero score is excluded',
                 [('increase', 1), ('increase', 2), ('decrease', 2)],
                 [1]),
                ('all scores return to zero',
                 [('increase', 1), ('increase', 2), ('decrease', 1),
                  ('decrease', 2)], []),
                ('decreasing unknown content produces no positive content',
                 [('decrease', 42)], []),
                ('content can become popular again after reaching zero',
                 [('increase', 1), ('decrease', 1), ('increase', 1)],
                 [1]),
                ('top ten are selected by score',
                 [('increase', content_id)
                  for content_id in range(1, 13)
                  for _ in range(13 - content_id)],
                 list(range(1, 11))),
                ('ties at the top ten boundary',
                 [('increase', content_id) for content_id in range(1, 13)],
                 list(range(12, 2, -1))),
            ]

            for name, actions, expected in cases:
                with self.subTest(case=name):
                    service = ContentService()
                    for action, content_id in actions:
                        if action == 'increase':
                            service.increase_popularity(content_id)
                        else:
                            service.decrease_popularity(content_id)
                    self.assertEqual(service.most_popular_content(), expected)
                    # Reading the ranking must not consume or change it.
                    self.assertEqual(service.most_popular_content(), expected)

    unittest.main(verbosity=2)
