"""Module for implementing a simple calculator menu."""
import sys
sys.path.append('/Users/admin/Desktop/lpnu/5 сем/Specialised programming languages/source')
from service.lab2.calculator_service import CalculatorService
from ui.menu_builder import Menu


class CalculatorMenu(Menu):
    """A simple calculator menu class."""

    def run(self):
        """Run the calculator program."""
        calculator_service = CalculatorService()

        while True:
            try:
                self.display_menu()
                choice = input("Enter your choice: ")

                if choice == '1':
                    calculator_service.input_values()
                    print(f"The result is {calculator_service.calculate()}")
                elif choice == '2':
                    break
                else:
                    print("Invalid choice. Please try again.")

            except ValueError as ve:
                print(f"Invalid input: {ve}")
                
            except ZeroDivisionError as zde:
                print(f"Invalid input: {zde}")
                
            except Exception as e:
                print(f"An unexpected error occurred: {e}")

    @staticmethod
    def display_menu():
        """Display the calculator menu."""
        print("1. Perform calculation")
        print("2. Exit")
