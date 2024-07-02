"""
import pytest: 
This imports the pytest module, which is a framework for 
building simple and scalable test suites.

from json_handler import JsonHandler: 
This imports the JsonHandler class from the json_handler module.
"""
import pytest
from json_handler import JsonHandler  # assuming the class is in json_handler.py

def requirement(id):
    """
    def requirement(id): 
    This is a decorator function that assigns a requirement ID to a test function. 
    This can be useful for tracing tests back to their requirements. 
    This is traceability aspect. 
    """
    def decorator(function):
        function.requirement = id
        return function
    return decorator

"""
@pytest.fixture: These are fixture functions. 
Fixtures are a way to provide data or set up certain conditions that are needed for tests. 
Here, two fixtures are defined:
"""
@pytest.fixture
def json_handler():
    """
    json_handler(): This fixture creates and returns an instance of JsonHandler.
    """
    return JsonHandler()

@pytest.fixture
def temp_file(tmp_path):
    """
    temp_file(tmp_path): 
    This fixture creates a temporary file path using the built-in 
    tmp_path fixture from pytest.

    The tmp_path fixture provides a temporary directory unique to the test invocation.
    """
    return tmp_path / "test.json"

@requirement("REQ-101")
def test_read_json(json_handler, temp_file):
    """
    @requirement("REQ-101"), @requirement("REQ-102"), @requirement("REQ-103"): 
    These are uses of the requirement decorator defined earlier. 
    They assign requirement IDs to the test functions.
    
    test_read_json(json_handler, temp_file): 
    This is a test function that tests the read_json and write_json methods of JsonHandler. 
    It writes some test data to a temporary file using write_json, 
    then reads the data back using read_json, and 
    asserts that the read data is the same as the written data.
    """
    data = {"test": "data"}
    json_handler.write_json(data, temp_file)
    read_data = json_handler.read_json(temp_file)
    assert read_data == data

@requirement("REQ-102")
def test_write_json(json_handler, temp_file):
    """
    test_write_json(json_handler, temp_file): 
    This is a test function that tests the write_json method of JsonHandler. 
    It writes some test data to a temporary file using write_json, 
    then reads the data back using read_json, 
    and asserts that the read data is the same as the written data.
    """
    data = {"test": "data"}
    json_handler.write_json(data, temp_file)
    read_data = json_handler.read_json(temp_file)
    assert read_data == data

@requirement("REQ-103")
def test_check_key(json_handler):
    """
    test_check_key(json_handler): 
    This is a test function that tests the check_key method of JsonHandler. 
    It asserts that the key 'test' exists in the data dictionary
    """
    data = {"test": "data"}
    assert json_handler.check_key(data, 'test')

@requirement("REQ-104")
def test_update_json(json_handler, temp_file):
    """
    The test for this class will be as follows to be added to test_json_handler.py
    """
    data = {"test": "data"}
    json_handler.write_json(data, temp_file)
    json_handler.update_json("test", "new data", temp_file)
    updated_data = json_handler.read_json(temp_file)
    assert updated_data["test"] == "new data"
