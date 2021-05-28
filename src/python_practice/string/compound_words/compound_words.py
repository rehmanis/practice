"""
Filename: compound_words.py
Python version: python >= 3.6
Usage: python compound_words.py
Description: finds all compound words from words inputted into stdin
Assumption:
    1- words are only made up of lower case english alphabets
    2- If duplicate words are present, ignore the ones after the first
    3- The set of component words used to compose a specific compound word
       should be mutually exclusive and collectively exhaustive when composing that
       compound word
    4- input stream can have leading or tailing spaces
    5- input stream may or maynot have a newline at the end
"""
import sys
from typing import Set


class TrieNode:
    """A Trie's Node object that contains link to its children and a boolean to
    mark if the node is end of word
    """

    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:
    """A Trie data structure to store the word and allow fast word search
    at the expense of memory
    """

    def __init__(self):
        self.root = TrieNode()

    def contains(self, word: str) -> bool:
        """find whether a given word is present inside the trie

        :param word: a string of lower case english alphabets[a-z]
        :type word: str
        :return: True if trie contains the word, False otherwise
        :rtype: bool
        """
        curr_node = self.root

        for letter in word:
            curr_node = curr_node.children.get(letter)

            if curr_node is None:
                return False

        return curr_node.is_end_of_word

    def insert(self, word: str) -> None:
        """insert the given word into the trie

        :param word: a string of lower case english alphabets[a-z]
        :type word: str
        """
        curr_node = self.root

        for letter in word:
            next_node = curr_node.children.get(letter)
            # only create a new Trie Node if it does not already exist
            if next_node is None:
                next_node = TrieNode()
                curr_node.children[letter] = next_node
            curr_node = next_node

        curr_node.is_end_of_word = True

    def is_compound_word(self, word: str, visited: Set) -> bool:
        """find whether the given word is a compound word i.e made up of
        other words present in the trie

        :param word: a string of lower case english alphabets[a-z]
        :type word: str
        :param visited: keep track of component words seen so far in the compound word
        :type visited: Set
        :return: True if given word is a valid compound word and False otherwise
        :rtype: bool
        """
        curr_node = self.root

        for idx, letter in enumerate(word):
            # get the child node for given letter
            curr_node = curr_node.children.get(letter)

            if curr_node is None:
                return False

            if curr_node.is_end_of_word:
                # current word is already been used in compound word
                if word[: idx + 1] in visited:
                    return False

                visited.add(word[: idx + 1])

                if self.contains(word[idx + 1 :]) and word[idx + 1 :] not in visited:
                    return True

                is_compound = self.is_compound_word(word[idx + 1 :], visited)

                if is_compound:
                    return True

                # remove the old component(word[: idx + 1]) from visited so we can
                # still use it later as we cannot use to make the compound word for now
                visited.remove(word[: idx + 1])

        return False


def find_compound_words():
    """Performs all the necessary setup, and computation"""
    # initialise datastructures used for finding compound words sorted in
    # alphabetical order
    trie = Trie()
    words = set()
    compound_words = []

    # read words from stdin and insert them into Trie. Each line should only
    # contain one word
    for line in sys.stdin:
        word = line.strip()
        # no point wasting insert computation if the word is already in trie
        if word and word not in words:
            words.add(word)
            trie.insert(word)

    # find all compound words in the trie
    for word in words:
        visited = set()
        if trie.is_compound_word(word, visited):
            compound_words.append(word)

    # sort the compound words in lexicographical order
    compound_words.sort()

    # print the sorted compound words to stdout with newline
    for idx in range(len(compound_words)):
        print(compound_words[idx])


if __name__ == "__main__":
    """Entry point for the program."""
    find_compound_words()
