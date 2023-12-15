"""ASCII-art generator."""

from pyfiglet import Figlet
from colorama import Fore
# To initialize colorama and configure its behavior
from colorama import init as colorama_init
import sys
sys.path.append('/Users/admin/Desktop/lpnu/5 сем/Specialised programming languages/source')
from shared.ascii_utils import check_size, preview_art, change_symbols
from shared.user_input import get_phrase

# Initialize colorama
# autoreset=True -> Color settings will automatically reset after each print statement
colorama_init(autoreset=True)

def create_ascii_art(FOLDER_PATH, settings_obj):
    """Ask user for phrase and show ASCII-art.
    
    Args:
        settings_obj (AsciiArtSettings): Object with settings.
    """
    user_input = get_phrase() 
    width, height = settings_obj.size
    try:
        check_size(user_input, width, height)
    except ValueError as e:
        print(f"An error occurred: {e}")
        return None
    
    art = Figlet(font=settings_obj.font, width=settings_obj.size[0])
    art = art.renderText(user_input)
    
    if settings_obj.symbols:
        art = change_symbols(art, settings_obj.symbols[0])
        
    art = settings_obj.color + art
    
    preview_art(FOLDER_PATH, art)    