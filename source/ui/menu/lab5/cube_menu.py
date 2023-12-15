"""Module for implementing a simple calculator menu."""
import sys
sys.path.append('/Users/admin/Desktop/lpnu/5 сем/Specialised programming languages/source')
from service.lab5.cube_service import CubeService
from ui.menu_builder import Menu


class CubeMenu(Menu):
    """A simple 3d cube menu class."""

    def run(self):
        """Run the cube program."""
        cube_service = CubeService(20, 2)
        try: 
            sys.stdout.write('\x1b[2J')
            while True:
                sys.stdout.write('\x1b[H')

                cube_service.update()
                cube_service.draw()
        except KeyboardInterrupt:
            sys.stdout.write('\x1b[2J')
            sys.stdout.write('\x1b[H')

    @staticmethod
    def display_menu():
        """Display the cube menu."""
        print("1. Set cube values")
        print("2. Display default cube")
        print("3. Exit")
