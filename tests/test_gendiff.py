import pytest
import os

from gendiff.gendiff import generate_diff

CURRENT_PATH = os.path.dirname(__file__)
NESTED_JSON1 = os.path.join(CURRENT_PATH, "fixtures/file1.json")
NESTED_JSON2 = os.path.join(CURRENT_PATH, "fixtures/file2.json")
NESTED_YML1 = os.path.join(CURRENT_PATH, "fixtures/file1.yml")
NESTED_YML2 = os.path.join(CURRENT_PATH, "fixtures/file2.yml")
CORRECT_NESTED_RES = os.path.join(CURRENT_PATH,
                                  "fixtures/result_stylish")
CORRECT_PLAIN_NESTED_RES = os.path.join(CURRENT_PATH,
                                        "fixtures/result_plain")
NOT_EXISTED_FILE = os.path.join(CURRENT_PATH, "fixtures/file13895y23.yml")


@pytest.mark.parametrize(\
        "file1, file2, correct_res, formatter",\
        [ \
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
    assert generate_diff(NESTED_JSON1, CORRECT_PLAIN_NESTED_RES) == "Unsupported file format"


def test_gendiff_file_not_exist():
    assert generate_diff(NESTED_JSON1, NOT_EXISTED_FILE) == "One or both files not found"

