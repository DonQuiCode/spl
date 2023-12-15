"""
Module: interactive_docs_menu

This module provides a text-based interactive menu for navigating through HTML documentation.

Classes:
    - DocsMenu: Provides a text-based interactive menu for navigating through HTML documentation.
"""

from service.docs_service import DocsService


class DocsMenu:
    """
    DocsMenu class provides a text-based interactive menu for navigating through HTML documentation.

    Attributes:
        docs_service (DocsService): An instance of DocsService for managing HTML content.

    Methods:
        __init__(folder_path: str)
            Initializes a DocsMenu instance with a specified folder path.

        print_menu()
            Static method to print the interactive menu options.

        run()
            Runs the interactive menu loop, allowing the user to navigate through the documentation.
    """

    def __init__(self, folder_path: str):
        """
        Initializes a DocsMenu instance with a specified folder path.

        Parameters:
            folder_path (str): The path to the folder containing HTML files.

        Returns:
            None
        """
        self.docs_service = DocsService(folder_path)

    @staticmethod
    def print_menu():
        """
        Static method to print the interactive menu options.

        Returns:
            None
        """
        print("1. Display current page")
        print("2. Change to a specific page")
        print("3. Move to the next page")
        print("4. Move to the previous page")
        print("0. Exit")

    def run(self):
        """
        Runs the interactive menu loop, allowing the user to navigate through the documentation.

        Returns:
            None
        """
        while True:
            print("Current Page:", self.docs_service.current_page)
            self.print_menu()

            try:
                choice = int(input("Enter your choice: "))

                if choice == 1:
                    self.docs_service.display_page()
                elif choice == 2:
                    page_number = int(input("Enter the page number: "))
                    self.docs_service.change_page(page_number)
                elif choice == 3:
                    self.docs_service.next_page()
                elif choice == 4:
                    self.docs_service.prev_page()
                elif choice == 0:
                    break
                else:
                    print("Invalid choice. Please enter a corresponding number")

            except ValueError:
                print("Invalid input. Please enter a number.")
