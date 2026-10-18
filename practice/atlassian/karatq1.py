# String Formation and Anagram Matching: Given an array of target words words = ["baby", "cat", "dada", "dog"] and a query string word1 = "ctay", write a function find(words, query) that returns the word from the array that can be formed using the characters in the query string ("cat").

from collections import Counter
from typing import List
import unittest


# Set will fail here because it will not consider the duplicates:
# def find(words: list[str], query: str) -> str:
#     """
#     Finds and returns the word from `words` that can be formed 
#     using the characters available in `query`.
    
#     :param words: List of target words
#     :param query: Query string containing available characters
#     :return: The matching word from the words array
#     """

#     # char_sets: List[set] = [set(word) for word in words]
#     # query_set: set = set(query)

#     # print(words, char_sets, '\n', query, query_set)

#     # for i, char_set in enumerate(char_sets):
#     #     if char_set.issubset(query_set):
#     #         return words[i]

#     # return ''

def find(words: list[str], query: str) -> str:
    """
    Finds and returns the word from `words` that can be formed 
    using the characters available in `query`.
    
    :param words: List of target words
    :param query: Query string containing available characters
    :return: The matching word from the words array
    """

    querycounter = Counter(query)

    # O(m)
    for word in words:
        wordcounter = Counter(word)
        not_found = False

        # O(n)
        for char, cnt in wordcounter.items():
            if char in querycounter:
                if not cnt <= querycounter[char]:
                    not_found = True
                    break
            else:
                not_found = True
                break


        if not not_found:
            return word


    return ''
        


class TestFindWord(unittest.TestCase):

    def test_basic_match(self):
        # Base case from prompt: "cat" is formed by 'c', 'a', 't' in "ctay"
        words = ["baby", "cat", "dada", "dog"]
        query = "ctay"
        self.assertEqual(find(words, query), "cat")

    def test_extra_characters_in_query(self):
        # Query contains excess characters ('x', 'z', 'o')
        words = ["apple", "banana", "dog", "elephant"]
        query = "godxz"
        self.assertEqual(find(words, query), "dog")

    def test_duplicate_characters_frequency(self):
        # Query has enough 'a's and 'd's for "dada" (2 'a's, 2 'd's)
        # "baby" needs 2 'b's (query only has 1)
        words = ["baby", "cat", "dada", "dog"]
        query = "aaddz"
        self.assertEqual(find(words, query), "dada")

    def test_exact_character_match(self):
        # Query is an exact anagram of the target word
        words = ["tree", "cloud", "rain", "sun"]
        query = "nrai"
        self.assertEqual(find(words, query), "rain")

    def test_longer_query_with_multiple_candidates_by_length(self):
        # Query contains letters for "cat", but lacks enough 'b's for "baby"
        words = ["baby", "cat", "dada"]
        query = "bcaty"
        self.assertEqual(find(words, query), "cat")

if __name__ == "__main__":
    unittest.main()