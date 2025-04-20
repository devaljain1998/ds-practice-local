from typing import List


class Solution:
    def __init__(self):
        self.map = {}

    def encode(self, strs: List[str]) -> str:
        s = ''.join(strs)
        encoded_string = str(hash(s))
        self.map[encoded_string] = strs
        return encoded_string

    def decode(self, s: str) -> List[str]:
        return self.map.get(s, [])
