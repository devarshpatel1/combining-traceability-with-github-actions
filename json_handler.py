"""
This module provides a class for handling JSON data.

The JsonHandler class includes methods for reading from,
writing to, checking keys in, and updating JSON files.
"""

import json

class JsonHandler:
    """
    This class provides methods for handling JSON data.
    """

    def read_json(self, file_path):
        """
        Reads a JSON file from the provided file_path, parses it into a Python object,
        and returns this object.

        Args:
            file_path (str): The path to the JSON file.

        Returns:
            dict: The JSON data as a Python dictionary.
        """
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data

    def write_json(self, data, file_path):
        """
        Writes the provided Python object to a file in JSON format.

        Args:
            data (dict): The data to write to the JSON file.
            file_path (str): The path to the JSON file.

        Returns:
            None
        """
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file)

    def check_key(self, data, key):
        """
        Checks if the given key exists in the data object.

        Args:
            data (dict): The data object to check.
            key (str): The key to check for.

        Returns:
            bool: True if the key exists, False otherwise.
        """
        return key in data

    def update_json(self, key, value, file_path):
        """
        Updates the value for a given key in a JSON file.

        Args:
            key (str): The key to update.
            value (any): The new value for the key.
            file_path (str): The path to the JSON file.

        Returns:
            None
        """
        with open(file_path, 'r+', encoding='utf-8') as file:
            data = json.load(file)
            data[key] = value
            file.seek(0)
            json.dump(data, file)
            file.truncate()
