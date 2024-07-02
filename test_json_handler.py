"""
This module contains unit tests for the JsonHandler class.
"""

import pytest
from json_handler import JsonHandler  # assuming the class is in json_handler.py

def requirement(req_id):
    """
    Decorator to assign a requirement ID to a test function for traceability.

    Args:
        req_id (str): The requirement ID to assign.

    Returns:
        function: The decorated function with a requirement attribute.
    """
    def decorator(function):
        function.requirement = req_id
        return function
    return decorator

@pytest.fixture
def json_handler():
    """
    Fixture to create and return an instance of JsonHandler.

    Returns:
        JsonHandler: An instance of JsonHandler.
    """
    return JsonHandler()

@pytest.fixture
def temp_file(tmp_path):
    """
    Fixture to create a temporary file path using the built-in tmp_path fixture from pytest.

    Args:
        tmp_path (pathlib.Path): Temporary directory unique to the test invocation.

    Returns:
        pathlib.Path: The temporary file path.
    """
    return tmp_path / "test.json"

@requirement("REQ-101")
def test_read_json(json_handler, temp_file):
    """
    Test the read_json method of JsonHandler.

    Args:
        json_handler (JsonHandler): An instance of JsonHandler.
        temp_file (pathlib.Path): The temporary file path.

    This test writes some test data to a temporary file using write_json,
    then reads the data back using read_json, and asserts that the read data
    is the same as the written data.
    """
    data = {"test": "data"}
    json_handler.write_json(data, temp_file)
    read_data = json_handler.read_json(temp_file)
    assert read_data == data

@requirement("REQ-102")
def test_write_json(json_handler, temp_file):
    """
    Test the write_json method of JsonHandler.

    Args:
        json_handler (JsonHandler): An instance of JsonHandler.
        temp_file (pathlib.Path): The temporary file path.

    This test writes some test data to a temporary file using write_json,
    then reads the data back using read_json, and asserts that the read data
    is the same as the written data.
    """
    data = {"test": "data"}
    json_handler.write_json(data, temp_file)
    read_data = json_handler.read_json(temp_file)
    assert read_data == data

@requirement("REQ-103")
def test_check_key(json_handler):
    """
    Test the check_key method of JsonHandler.

    Args:
        json_handler (JsonHandler): An instance of JsonHandler.

    This test asserts that the key 'test' exists in the data dictionary.
    """
    data = {"test": "data"}
    assert json_handler.check_key(data, 'test')

@requirement("REQ-104")
def test_update_json(json_handler, temp_file):
    """
    Test the update_json method of JsonHandler.

    Args:
        json_handler (JsonHandler): An instance of JsonHandler.
        temp_file (pathlib.Path): The temporary file path.

    This test writes some test data to a temporary file using write_json,
    updates the data using update_json, then reads the updated data back
    using read_json, and asserts that the updated data is correct.
    """
    data = {"test": "data"}
    json_handler.write_json(data, temp_file)
    json_handler.update_json("test", "new data", temp_file)
    updated_data = json_handler.read_json(temp_file)
    assert updated_data["test"] == "new data"
