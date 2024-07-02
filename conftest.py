"""
The conftest.py file in pytest is used to write fixtures 
that are shared across multiple files, modules, or sessions. 
It's a way to provide a set of setup functions or hooks for your tests. 
The name conftest.py is a standard name recognized by pytest, 
and it will automatically discover these files in your test directories.
"""

def pytest_runtest_protocol(item, nextitem):
    """
    Hook called before a test is run.

    Args:
        item (pytest.Item): The test item.
        nextitem (pytest.Item): The next test item (unused).

    This hook checks if the test function has a requirement attribute
    and prints a message indicating which test is being run and its
    associated requirement.
    """
    del nextitem  # Handle the unused argument
    if hasattr(item, 'function') and hasattr(item.function, 'requirement'):
        print(
            f"Running test {item.nodeid} with requirement {item.function.requirement}"
        )

def pytest_runtest_makereport(item, call):
    """
    Hook called after a test is run.

    Args:
        item (pytest.Item): The test item.
        call (pytest.CallInfo): The call info.

    This hook creates a report for the test, indicating whether the test
    passed, failed, was skipped, or was expected to fail (xfail). It then
    adds this report to a traceability_matrix in the pytest configuration.
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
        item.config.traceability_matrix[item.nodeid] = (
            item.function.requirement,
            result
        )

def pytest_sessionstart(session):
    """
    Hook called at the start of the pytest session.

    Args:
        session (pytest.Session): The pytest session.

    This hook initializes the traceability_matrix in the pytest configuration.
    """
    session.config.traceability_matrix = {}

def pytest_sessionfinish(session, exitstatus):
    """
    Hook called at the end of the pytest session.

    Args:
        session (pytest.Session): The pytest session.
        exitstatus (int): The exit status of the session (unused).

    This hook prints the traceability_matrix, which shows the result of
    each test and its associated requirement.
    """
    del exitstatus  # Handle the unused argument
    print("Traceability Matrix:")
    for test, (requirement, result) in session.config.traceability_matrix.items():
        print(f"{test}: {requirement}, {result}")
