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
