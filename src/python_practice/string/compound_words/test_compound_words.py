import os
import subprocess
import sys

import pytest


HERE = os.path.dirname(os.path.abspath(__file__))


def convert_to_str(list_str):
    return "".join(f"{row}\n" for row in list_str)


data = [
    # test general case compound word made up of two components
    {
        "input": [
            "man",
            "woman",
            "manhandle",
            "handle",
            "race",
            "drag",
            "car",
            "racecar",
            "computer",
            "bag",
            "dragon",
            "manbag",
        ],
        "expected": ["manbag", "manhandle", "racecar"],
    },
    # test some letters missing from component words
    {
        "input": ["ma", "handle", "handleman", "bag", "an", "bagant", "ant"],
        "expected": ["bagant"],
    },
    # test no compound words
    {
        "input": ["man", "ma", "nat", "dogma"],
        "expected": [],
    },
    # test duplicate compounds words
    {
        "input": [
            "man",
            "handle",
            "manhandle",
            "manhandle",
            "bag",
            "cat",
            "catbag",
            "bagcat",
        ],
        "expected": ["bagcat", "catbag", "manhandle"],
    },
    # test duplicate components words
    {
        "input": ["man", "handle", "bag", "man", "manhandleman", "bagman"],
        "expected": ["bagman"],
    },
    # test component word only used once
    {
        "input": ["man", "handle", "manhandleman"],
        "expected": [],
    },
    # test compound word made up of more than 2 components (odd length)
    {
        "input": ["hello", "my", "world", "myworldhello"],
        "expected": ["myworldhello"],
    },
    # test compound word made up of more than 2 components (even length)
    {
        "input": ["is", "lighter", "feather", "islighterthanfeather", "than", "duty"],
        "expected": ["islighterthanfeather"],
    },
    # test component being subset of other components. Make sure if component
    # can't be used at current partition of the word, then we can still later use it
    {
        "input": ["to", "tom", "tomato", "a"],
        "expected": ["tomato"],
    },
    # test if for given compound word, the current partitions are all components
    # except for the last element which has already been used up
    {
        "input": ["a", "c", "bc", "de", "ab", "abcdea"],
        "expected": ["abcdea"],
    },
]


@pytest.mark.parametrize("test_case", data)
def test_find_compound_words(test_case):

    input = convert_to_str(test_case["input"])
    expected = convert_to_str(test_case["expected"])
    p = subprocess.run(
        [sys.executable, os.path.join(HERE, "compound_words.py")],
        stdout=subprocess.PIPE,
        input=input,
        encoding="ascii",
    )

    assert p.stdout == expected
