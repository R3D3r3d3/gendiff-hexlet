import pytest
import os

from gendiff.gendiff import generate_diff

CURRENT_PATH = os.path.dirname(__file__)
FLAT_JSON1 = os.path.join(CURRENT_PATH, "fixtures/file1.json")
FLAT_JSON2 = os.path.join(CURRENT_PATH, "fixtures/file2.json")
FLAT_YML1 = os.path.join(CURRENT_PATH, "fixtures/file1.yml")
FLAT_YML2 = os.path.join(CURRENT_PATH, "fixtures/file2.yml")
NESTED_JSON1 = os.path.join(CURRENT_PATH, "fixtures/nested_file1.json")
NESTED_JSON2 = os.path.join(CURRENT_PATH, "fixtures/nested_file2.json")
NESTED_YML1 = os.path.join(CURRENT_PATH, "fixtures/nested_file1.yml")
NESTED_YML2 = os.path.join(CURRENT_PATH, "fixtures/nested_file2.yml")
CORRECT_FLAT_RES = os.path.join(CURRENT_PATH, "fixtures/compared_file1_file2.txt")
CORRECT_NESTED_RES = os.path.join(CURRENT_PATH,
                                  "fixtures/compared_nested_file1_file2.txt")
CORRECT_PLAIN_NESTED_RES = os.path.join(CURRENT_PATH,
                                        "fixtures/compared_plain_nested_file1_file2.txt")
NOT_EXISTED_FILE = os.path.join(CURRENT_PATH, "fixtures/file13895y23.yml")


@pytest.mark.parametrize(\
        "file1, file2, correct_res, formatter",\
        [ \
                (FLAT_JSON1, FLAT_JSON2, CORRECT_FLAT_RES, "stylish"),\
                (FLAT_YML1, FLAT_YML2, CORRECT_FLAT_RES, "stylish"),\
                (NESTED_JSON1, NESTED_JSON2, CORRECT_NESTED_RES, "stylish"),\
                (NESTED_YML1, NESTED_YML2, CORRECT_NESTED_RES, "stylish"),\
                (NESTED_YML1, NESTED_YML2, CORRECT_PLAIN_NESTED_RES, "plain"),\
                (NESTED_JSON1, NESTED_JSON2, CORRECT_PLAIN_NESTED_RES, "plain")\
                ]\
        )
def test_gendiff_flat_jsons(file1, file2, correct_res, formatter):
    with open(correct_res, encoding="utf-8") as f:
        expected = f.read()
    assert generate_diff(file1, file2, formatter) == expected


def test_gendiff_unsupported_file_type():
    assert generate_diff(FLAT_JSON1, CORRECT_FLAT_RES) == "Unsupported file format"


def test_gendiff_file_not_exist():
    assert generate_diff(FLAT_JSON1, NOT_EXISTED_FILE) == "One or both files not found"

