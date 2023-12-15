"""
UI Module for Lab Menus

Example:
    To run the module and start the menu facade, execute the script as follows:

        $ python module_name.py

Functions:
    None

If __name__ == '__main__':
    Creates a MenuFacade instance with a list of menu tuples and starts the menu.

Author:
    DonQuiCode
"""
from ui.menu.menu_facade import MenuFacade

if __name__ == '__main__':
    menuFacade = MenuFacade()
    menuFacade.start()
