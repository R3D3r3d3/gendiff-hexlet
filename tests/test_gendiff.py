import pytest
import os

from gendiff.gendiff import generate_diff

CURRENT_PATH = os.path.dirname(__file__)
FLAT_JSON1 = os.path.join(CURRENT_PATH, "fixtures/file1.json")
FLAT_JSON2 = os.path.join(CURRENT_PATH, "fixtures/file2.json")
CORRECT_RES1 = os.path.join(CURRENT_PATH, "fixtures/compare_file1_file2.txt")

def test_gendiff_flat_jsons():
    with open(CORRECT_RES1, encoding="utf-8") as f:
        expected = f.read()
    assert generate_diff(FLAT_JSON1, FLAT_JSON2) == expected

