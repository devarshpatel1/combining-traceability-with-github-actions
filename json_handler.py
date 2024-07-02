import json

"""
This Python script defines a class JsonHandler that provides methods for handling JSON data.
"""
class JsonHandler:
    def read_json(self, file_path):
        """
        read_json(self, file_path): 
        This method reads a JSON file from the provided file_path,
        parses it into a Python object using json.load(), and 
        returns this object.
        """
        with open(file_path, 'r') as f:
            data = json.load(f)
        return data

    def write_json(self, data, file_path):
        """
        write_json(self, data, file_path): 
        This method takes a Python object data and a file_path as input. 
        It writes the data to a file at file_path in JSON format using json.dump().
        """
        with open(file_path, 'w') as f:
            json.dump(data, f)

    def check_key(self, data, key):
        """
        check_key(self, data, key): 
        This method checks if a given key exists in the data object.
        It returns True if the key exists and False otherwise. 
        The data object is expected to be a dictionary-like object 
        (for example, a result of json.load()).
        """
        return key in data
    
    def update_json(self, key, value, file_path):
        """
        
        """
        with open(file_path, 'r+') as f:
            data = json.load(f)
            data[key] = value
            f.seek(0)
            json.dump(data, f)
            f.truncate()
