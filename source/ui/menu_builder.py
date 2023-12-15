"""
Menu System Module

This module defines an abstract base class 'Menu' and a 'MenuFacade' class
to manage a collection of menus. The 'Menu' class serves as a blueprint for
individual menu implementations, and the 'MenuFacade' class provides a
user-friendly interface for interacting with multiple menus.

Classes:
    - Menu: Abstract base class for menu implementations.
    - MenuFacade: Facade class for managing a collection of menus.

Usage:
    Create instances of specific menu classes that inherit from 'Menu' to define
    custom menu behaviors. Then, use the 'MenuFacade' class to organize and present
    these menus to users.
"""
from abc import ABC, abstractmethod


class Menu(ABC):
    """
    A description of the entire function, its parameters, and its return types.
    """

    @abstractmethod
    def run(self):
        """
        Abstract method to be implemented by subclasses.

        This method defines the behavior of the menu when it is executed.

        Raises:
            NotImplementedError: This method must be implemented by subclasses.
        """
