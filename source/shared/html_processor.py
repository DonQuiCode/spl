"""
Module: html_processor

This module defines the HtmlProcessor class, which is responsible for processing HTML files.

Classes:
    - HtmlProcessor: Processes HTML files to extract content and convert it to text.

Usage:
    # Example usage:
    html_processor = HtmlProcessor("/path/to/html/files")

    # Get a list of tuples containing file names and HTML contents
    files_data = html_processor.files_data

    # Get text data for a specific page
    text_data = html_processor.get_text_data(1)
"""
import os
import html2text

from config.logger_config import logger


class HtmlProcessor:
    """
    HtmlProcessor class processes HTML files to extract content and convert it to text.

    Methods:
        __init__(folder_path: str)
            Initializes an HtmlProcessor instance with a specified folder path.

        read_files_in_folder(folder_path: str)
            Reads the contents of all HTML files in the specified folder.

        get_text_data(page_number: int)
            Converts the HTML content of a specified page to text.

    Example:
        # Creating an HtmlProcessor instance with the path to HTML files
        html_processor = HtmlProcessor("/path/to/html/files")

        # Get a list of tuples containing file names and HTML contents
        files_data = html_processor.files_data

        # Get text data for a specific page
        text_data = html_processor.get_text_data(1)
    """

    def __init__(self, folder_path: str):
        """
        Initializes an HtmlProcessor instance with a specified folder path.

        Parameters:
            folder_path (str): The path to the folder containing HTML files.

        Returns:
            None
        """
        self.__files_data = self.read_files_in_folder(folder_path)
        logger.info("Read %s HTML files.", len(self.__files_data))

    @property
    def files_data(self):
        """
        Property: Gets the list of tuples containing file names and HTML contents.

        Returns:
            list: A list of tuples where the first element is the file name, and
                  the second element is the content of the HTML file.
        """
        return self.__files_data

    @staticmethod
    def read_files_in_folder(folder_path: str):
        """
        Reads the contents of all HTML files in the specified folder.

        Parameters:
            folder_path (str): The path to the folder containing the HTML files.

        Returns:
            list: A list of tuples where the first element is the file name, and
                  the second element is the content of the HTML file.
        """
        try:
            html_contents = []
            logger.info("Sorted HTML files in folder: %s", folder_path)
            files = sorted(os.listdir(folder_path))

            for file_name in files:
                file_path = os.path.join(folder_path, file_name)

                if os.path.isfile(file_path) and file_name.lower().endswith('.html'):
                    with open(file_path, 'r', encoding='utf-8') as file:
                        content = file.read()
                        html_contents.append((file_name, content))
                        logger.info("Read HTML file: %s", file_name)

            return html_contents
        except Exception as e:
            print(f"An error occurred while reading files: {e}")
            logger.error("HTML files weren't read", e)
            return []

    def get_text_data(self, page_number: int):
        """
        Converts the HTML content of a specified page to text.

        Parameters:
            page_number (int): The page number for which to get the text data.

        Returns:
            str: The text content of the HTML page.
        """
        if 1 <= page_number <= len(self.__files_data):
            _, content = self.__files_data[page_number - 1]
            return html2text.html2text(content)
        logger.error("Invalid page number: %s", page_number)
        return "Invalid page number."
