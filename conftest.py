"""
The conftest.py file in pytest is used to write fixtures 
that are shared across multiple files, modules, or sessions. 
It's a way to provide a set of setup functions or hooks for your tests. 
The name conftest.py is a standard name recognized by pytest, 
and it will automatically discover these files in your test directories.
"""
import pytest

def pytest_runtest_protocol(item, nextitem):
    """
    pytest_runtest_protocol(item, nextitem): 
    This hook is called before a test is run. 
    Here, it checks if the test function has a requirement attribute 
    (which was set by the requirement decorator in your test file). 
    If it does, it prints a message indicating which test is being run 
    and its associated requirement.
    """
    if hasattr(item, 'function') and hasattr(item.function, 'requirement'):
        print(f"Running test {item.nodeid} with requirement {item.function.requirement}")
    return None  # continue with the default test protocol

def pytest_runtest_makereport(item, call):
    """
    pytest_runtest_makereport(item, call): 
    This hook is called after a test is run. 
    It creates a report for the test, indicating 
    whether the test passed, failed, was skipped, or was expected to fail (xfail). 
    It then adds this report to a traceability_matrix in the pytest configuration.
    """
    if call.when == 'call':
        result = 'NOT RUN'
        if call.excinfo is not None:
            if call.excinfo.typename == 'pytest.skip':
                result = 'SKIP'
            elif call.excinfo.typename == 'pytest.xfail':
                result = 'XFAIL'
            else:
                result = 'FAIL'
        else:
            result = 'PASS'
        item.config.traceability_matrix[item.nodeid] = (item.function.requirement, result)

def pytest_sessionstart(session):
    """
    pytest_sessionstart(session): This hook is called at the start of the pytest session. 
    Here, it initializes the traceability_matrix in the pytest configuration.
    """
    session.config.traceability_matrix = {}

def pytest_sessionfinish(session, exitstatus):
    """
    pytest_sessionfinish(session, exitstatus):
    This hook is called at the end of the pytest session. 
    Here, it prints the traceability_matrix, 
    which shows the result of each test and its associated requirement.
    """
    print("Traceability Matrix:")
    for test, (requirement, result) in session.config.traceability_matrix.items():
        print(f"{test}: {requirement}, {result}")
