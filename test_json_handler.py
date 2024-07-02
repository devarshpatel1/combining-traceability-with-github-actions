"""
Module for testing JsonHandler class functionality using pytest.

Imports:
    pytest: The pytest module is a framework for building simple and scalable test suites.
    JsonHandler: The JsonHandler class from the json_handler module.

Decorators:
    requirement: A decorator function for assigning requirement IDs to test functions
                 for traceability.
"""

import pytest
from json_handler import JsonHandler  # Assuming the class is in json_handler.py

def requirement(requirement_id):
    """
    Decorator to assign a requirement ID to a test function.

    Args:
        requirement_id (str): The requirement ID to be assigned to the test function.

    Returns:
        function: The decorated function with an assigned requirement ID.
    """
    def decorator(function):
        function.requirement = requirement_id
        return function
    return decorator

@pytest.fixture
def json_handler():
    """
    Fixture to create and return an instance of JsonHandler.

    Returns:
        JsonHandler: An instance of the JsonHandler class.
    """
    return JsonHandler()

@pytest.fixture
def temp_file(tmp_path):
    """
    Fixture to create a temporary file path using the built-in tmp_path fixture from pytest.

    Args:
        tmp_path (Path): The temporary path provided by pytest.

    Returns:
        Path: The temporary file path for testing.
    """
    return tmp_path / "test.json"

@requirement("REQ-101")
def test_read_json(json_handler_fixture, temp_file_fixture):
    """
    Test for the read_json method of JsonHandler.

    This test writes some test data to a temporary file using write_json,
    then reads the data back using read_json, and asserts that the read
    data is the same as the written data.

    Args:
        json_handler_fixture (JsonHandler): The instance of JsonHandler.
        temp_file_fixture (Path): The temporary file path for testing.
    """
    data = {"test": "data"}
    json_handler_fixture.write_json(data, temp_file_fixture)
    read_data = json_handler_fixture.read_json(temp_file_fixture)
    assert read_data == data

@requirement("REQ-102")
def test_write_json(json_handler_fixture, temp_file_fixture):
    """
    Test for the write_json method of JsonHandler.

    This test writes some test data to a temporary file using write_json,
    then reads the data back using read_json, and asserts that the read
    data is the same as the written data.

    Args:
        json_handler_fixture (JsonHandler): The instance of JsonHandler.
        temp_file_fixture (Path): The temporary file path for testing.
    """
    data = {"test": "data"}
    json_handler_fixture.write_json(data, temp_file_fixture)
    read_data = json_handler_fixture.read_json(temp_file_fixture)
    assert read_data == data

@requirement("REQ-103")
def test_check_key(json_handler_fixture):
    """
    Test for the check_key method of JsonHandler.

    This test asserts that the key 'test' exists in the data dictionary.

    Args:
        json_handler_fixture (JsonHandler): The instance of JsonHandler.
    """
    data = {"test": "data"}
    assert json_handler_fixture.check_key(data, 'test')

@requirement("REQ-104")
def test_update_json(json_handler_fixture, temp_file_fixture):
    """
    Test for the update_json method of JsonHandler.

    This test writes some test data to a temporary file using write_json,
    updates the data using update_json, then reads the updated data back
    using read_json, and asserts that the updated data is correct.

    Args:
        json_handler_fixture (JsonHandler): The instance of JsonHandler.
        temp_file_fixture (Path): The temporary file path for testing.
    """
    data = {"test": "data"}
    json_handler_fixture.write_json(data, temp_file_fixture)
    json_handler_fixture.update_json("test", "new data", temp_file_fixture)
    updated_data = json_handler_fixture.read_json(temp_file_fixture)
    assert updated_data["test"] == "new data"
