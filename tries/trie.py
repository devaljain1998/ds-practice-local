from collections import defaultdict
from typing import Any, DefaultDict

class TrieNode:
    def __init__(self):
        self.children: DefaultDict[Any, TrieNode] = defaultdict(TrieNode)
        self.is_end_of_word: bool = False        
    
    def contains_letter(self, l: str) -> bool:
        return l in self.children

    def put(self, letter: str, node: 'TrieNode'):
        self.children[letter] = node
        
    def get(self, letter: str) -> 'TrieNode':
        return self.children[letter]
    
    def mark_end(self):
        self.is_end_of_word = True
    
    def is_end(self) -> bool:
        return self.is_end_of_word

class Trie:
    def __init__(self):
        self.root: TrieNode = TrieNode()

    
    def insert(self, word: str):
        node = self.root
        for letter in word:
            # If node does not contains the letter
            # then create it and move to the next node
            if not node.contains_letter(letter):
                newnode = TrieNode()
                node.put(letter, newnode)
            node = node.get(letter)
        # Mark end of the word as true
        node.mark_end()
                


    def search(self, word: str) -> bool:
        node = self.root
        for letter in word:
            if not node.contains_letter(letter):
                return False
            node = node.get(letter)
        return node.is_end()               

    
    def startswith(self, word: str):
        node = self.root
        for letter in word:
            if not node.contains_letter(letter):
                return False
            node = node.get(letter)
        return True

input_strings = ["appleairpods", "appleipod", "apples", "applewatch"]
trie = Trie()
for istr in input_strings:
    trie.insert(istr)

searchword = 'apple'
print(f'{searchword} - {trie.search(searchword)}')
for word in input_strings:
    print(word, f'contains - {searchword}: {trie.search(word)}')
searchword = 'eokfn'
print(f'{searchword} - {trie.search(searchword)}')

startswithword = 'apple'
print(f'Starts with: {trie.startswith(startswithword)}')