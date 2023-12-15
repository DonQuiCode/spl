"""
Module: docs_service

This module defines the DocsService class, which is responsible for managing the
display of HTML content stored in a specified folder using an HtmlProcessor.

Classes:
    - DocsService: Manages the display of HTML content, allowing navigation between pages.

Usage:
    # Example usage:
    if __name__ == "__main__":
        docs_service = DocsService("/path/to/html/files")

        # Display the current page
        docs_service.display_page()

        # Change to a specific page
        docs_service.change_page(2)

        # Move to the next page
        docs_service.next_page()

        # Move to the previous page
        docs_service.prev_page()
"""
from shared.html_processor import HtmlProcessor


class DocsService:
    """
    DocsService class manages the display of HTML content, allowing navigation between pages.
    """

    def __init__(self, folder_path: str):
        """
        Initializes a DocsService instance.

        Parameters:
            folder_path (str): The path to the folder containing HTML files.

        Returns:
            None
        """
        self.__html_processor = HtmlProcessor(folder_path)
        self.__current_page = 1

    @property
    def current_page(self):
        """
        Property: Gets the current page number.

        Returns:
            int: The current page number.
        """
        return self.__current_page

    def display_page(self):
        """
        Display the HTML content of the current page.

        Returns:
            None
        """
        text_data = self.__html_processor.get_text_data(self.__current_page)
        print(text_data)

    def change_page(self, page_number):
        """
        Change the current page to the specified page number.

        Parameters:
            page_number (int): The page number to change to.

        Returns:
            None
        """
        if page_number < 1 or page_number > len(self.__html_processor.files_data):
            print("Invalid page number.")
        else:
            self.__current_page = page_number
            self.display_page()

    def next_page(self):
        """
        Move to the next page and display its content.

        Returns:
            None
        """
        if self.__current_page < len(self.__html_processor.files_data):
            self.__current_page += 1
            self.display_page()
        else:
            print("No next page available.")

    def prev_page(self):
        """
        Move to the previous page and display its content.

        Returns:
            None
        """
        if self.current_page > 1:
            self.__current_page -= 1
            self.display_page()
        else:
            print("Already at the first page.")
