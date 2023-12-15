"""
The module provides a text-based interactive menu for navigating through HTML documentation.
"""
import os
import sys
sys.path.append('/Users/admin/Desktop/lpnu/5 сем/Specialised programming languages/source')

from config.paths_config import HTML_DATA
from ui.menu.docs_menu import DocsMenu
from ui.menu.lab2.calculator_menu import CalculatorMenu
from ui.menu.lab3.ascii_generator_menu import AsciiArtMenu
from ui.menu.lab5.cube_menu import CubeMenu
from ui.menu.lab7.google_books_api_menu import GoogleBooksApiMenu
from ui.menu.lab8.plot_menu import PlotMenu


class MenuFacade:
    """
    Facade class for managing a collection of menus.

    This class provides a simple user interface to interact with a collection of menus.
    Menus are represented as tuples of menu names and menu instances. The class allows
    the user to select and execute a menu based on their choice.
    """

    def __init__(self):
        """
        Initialize the MenuFacade instance with a list of menus.
        """
        self.__menus = [("Calculator", CalculatorMenu()),
                        ("Ascii Art Generator", AsciiArtMenu()),
                         ("CubeMenu", CubeMenu()),
                         ("PlotMenu", PlotMenu()),
                         ("Google Books API Menu", GoogleBooksApiMenu())]
    
        self.__finish_number = 0

    def print_menu_options(self):
        """
        Print the available menu options to the console.

        This method iterates through the list of menus and prints each menu option
        along with its corresponding number.

        Returns:
            None
        """
        for index, (name, _) in enumerate(self.__menus, start=1):
            print(f"{index}. {name}")
        print(f"{self.__finish_number}. Exit")

    def start(self):
        """
        Start the menu façade, allowing the user to interact with the menus.

        This method enters a loop where it continuously prints the menu options and
        prompts the user for their choice. It then executes the selected menu.

        Returns:
            None
        """
        while True:
            self.print_menu_options()
            choice = input("Enter your choice: ")
            try:
                choice = int(choice)
                if choice == self.__finish_number:
                    break
                if not 1 <= choice <= len(self.__menus):
                    raise ValueError
                _, menu = self.__menus[choice - 1]
                menu.run()
            except ValueError:
                print("Invalid choice. Enter again!")
