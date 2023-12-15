"""
JSON Processor Module

This module provides functions for working with JSON data. It includes functions
for flattening nested JSON structures
and displaying flattened JSON data with colored output.

Usage:
1. Import the module: `import src.shared.json_processor as json_processor`
2. Use the provided functions to process JSON data.

Note: Ensure the required libraries (`colorama`) are installed before using this module.
You can install it using: `pip install colorama`

Example:
```python
import src.shared.json_processor as json_processor

# Flatten a nested JSON structure
json_data = {'name': 'John', 'address': {'city': 'New York', 'zip': '10001'}}
flattened_data = json_processor.flatten_json(json_data)
print(flattened_data)
# {'name': 'John', 'address_city': 'New York', 'address_zip': '10001'}

# Display flattened JSON data with colored output
json_processor.display_flattened_json([json_data], color_position=2)
"""
from colorama import Fore

from config.logger_config import logger
from shared import color_processor
import json
import os
import csv

class JSONProcessor:
    """
    Utility class for processing JSON data.

    This class provides static methods for flattening nested JSON structures
    and displaying flattened JSON data with colored output.

    Methods:
    - flatten_json(json_data: dict, parent_key: str = '', delimiter: str = '_') -> dict:
        Flattens a nested JSON structure and returns a flattened dictionary.

    - display_flattened_json(jsons, color_position: int = 4):
        Displays flattened JSON data with colored output.

    Parameters:
    - jsons: The JSON data to be displayed (can be a dictionary or a list of dictionaries).
    - color_position (int): The position of the color in the
      color_processor.colors dictionary (default is 4).

    Raises:
    - ValueError: If data types or color position are incorrect.
    """

    @staticmethod
    def flatten_json(json_data: dict, parent_key: str = '', delimiter='_'):
        """
        Flattens a nested JSON structure and returns a flattened dictionary.

        Parameters:
        - json_data (dict): The nested JSON structure to be flattened.
        - parent_key (str): The parent key used for constructing flattened
        keys (default is an empty string).
        - delimiter (str): The delimiter used between keys in the
        flattened structure (default is '_').

        Returns:
        - dict: A flattened dictionary.
        """
        if (not isinstance(json_data, dict) and not isinstance(parent_key, str)
                and not isinstance(delimiter, str)):
            logger.error("Please check the input parameters! They should be of type "
                         "dict, str, str respectively!")
            raise ValueError("Wrong data types!")
        flat_data = {}

        for key, value in json_data.items():
            new_key = parent_key + delimiter + key if parent_key else key

            if isinstance(value, dict):
                flat_data.update(JSONProcessor.flatten_json(value, new_key, delimiter))
            elif isinstance(value, list):
                for i, item in enumerate(value):
                    flat_data.update(JSONProcessor.flatten_json({str(i): item}, new_key, delimiter))
            else:
                flat_data[new_key] = value

        return flat_data

    @staticmethod
    def display_flattened_json(jsons, color_position: int = 4):
        """
        Displays flattened JSON data with colored output.

        Parameters:
        - jsons: The JSON data to be displayed (can be a dictionary or a list of dictionaries).
        - color_position (int): The position of the color in the
        color_processor.colors dictionary (default is 4).

        Raises:
        - ValueError: If data types or color position are incorrect.
        """
        if ((not isinstance(jsons, dict) or not isinstance(jsons, list))
                and not isinstance(color_position, int)):
            raise ValueError("Wrong data types!")
        if color_position < 0 or color_position > len(color_processor.colors):
            logger.error("Please check the input parameters! The color position "
                         "should be between 0 and length of colors! "
                         "The quantity of them is 15!")
            raise ValueError("Wrong color position!")
        if isinstance(jsons, list):
            for _, json_data in enumerate(jsons):
                flat_json = JSONProcessor.flatten_json(json_data)
                for key, value in flat_json.items():
                    print(getattr(Fore, color_processor.colors[color_position]) + f'{key}:'
                          + Fore.RESET + f' {value}')

        elif isinstance(jsons, dict):
            flat_json = JSONProcessor.flatten_json(jsons)
            for key, value in flat_json.items():
                print(getattr(Fore, color_processor.colors[color_position])
                      + f'{key}:' + Fore.RESET + f' {value}')
    
    @staticmethod            
    def save_data(data, folder_path, file_name, file_format, field_names=None):
        supported_formats = ['json', 'csv', 'txt']
        
        if file_format.lower() not in supported_formats:
            print(f"Unsupported file format: {file_format}")
            return
        
        file_path = os.path.join(folder_path, f"{file_name}.{file_format}")
        
        try:
            with open(file_path, 'w', encoding='utf-8') as file:
                if file_format.lower() == 'json':
                    json.dump(data, file, indent=2)
                elif file_format.lower() == 'csv':
                    writer = csv.DictWriter(file, field_names=field_names)
                    writer.writeheader()
                    writer.writerows(data)
                elif file_format.lower() == 'txt':
                    for item in data:
                        file.write(str(item) + '\n')
                else:
                    print(f"Unsupported file format: {file_format}")
        except Exception as e:
            print(f"Error saving data: {e}")
