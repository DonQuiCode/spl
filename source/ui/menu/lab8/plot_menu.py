"""Module for implementing a simple calculator menu."""
import sys
sys.path.append('/Users/admin/Desktop/lpnu/5 сем/Specialised programming languages/source')
from service.lab8.plot_service import PlotService
from ui.menu_builder import Menu

class PlotMenu(Menu):
    """A simple plot menu class."""

    def run(self):
        """Run the plot program."""
        plot_service = PlotService()
        try:
            plot_service.preprocess_data()
            plot_service.visualize_data()
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    @staticmethod
    def display_menu():
        """Display the plot menu."""
        print("1. Generate plots")
        print("2. Exit")
