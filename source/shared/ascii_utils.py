import os
import pyfiglet
from colorama import Fore

def set_font():
    """Set font for ASCII-art.
    
    Returns:
        font (str): Font name.
    """
    # Get list of font names
    fonts = pyfiglet.FigletFont.getFonts()
    
    # Enumerate and print fonts with numbering, starting from 1
    for index, font in enumerate(fonts, start=1):
        print(f"{index}. {font}")
        
    user_input = int(input('Enter the font number: '))
    font = fonts[user_input-1]
    
    return font

def set_size():
    """Set size for ASCII-art.
    
    Returns:
        width (int): Width of ASCII-art.
        height (int): Height of ASCII-art.
    """
    width = int(input('Enter width: '))
    height = int(input('Enter height: '))
    
    return width, height
    
def set_symbols():
    """Set symbol for ASCII-art.
    
    Returns:
        symbol (str): Symbol to replace.
    """
    regular_symbol = input('Enter regular symbol: ')
    
    set_shadow = input('Do you want to set a shadow symbol? (y/n): ')
    if set_shadow.lower() == 'y':
        shadow_symbol = input('Enter shadow symbol: ')
    else:
        shadow_symbol = ''
    
    # Get list of ASCII symbols
    ascii_dec_values = [i for i in range(0, 256)]
    ascii_symbols = [chr(i) for i in ascii_dec_values]
    
    # Check if symbol is in ASCII
    if regular_symbol and shadow_symbol not in ascii_symbols and shadow_symbol != '':
        print('Symbol is not in ASCII.')
        return None
    else:
        print("Symbol changed!")
        return regular_symbol, shadow_symbol
    
def set_color():
    """Set color for ASCII-art.
    
    Returns:
        color_code (str): Color code.
        
    Raises:
        IndexError: If color number is not in range.
    """
    # Get dictinary where key is color name and value is color code
    colors = dict(Fore.__dict__.items())

    # Enumerate and print colors with numbering, starting from 1
    for index, color in enumerate(colors.keys(), start=1):
        print(f"{index}. {colors[color]}{color}")
     
    user_input = int(input('Enter the color number: '))
     
    # Get user input
    try:
        color_code = colors[list(colors.keys())[user_input-1]]
        return color_code
    except IndexError:
        print(f'Color number is not in range. Available colors are in range from 1 to {len(colors)}.')
         
def set_alignment():
    """Set alignment for ASCII-art.
    
    Returns:
        alignment (str): Alignment.
    """
    alignment = input('Enter alignment (left/center/right): ')
    
    return alignment
   
def set_3d_option():
    while True:
        user_input = input('3D option (y/n): ')
        if user_input == 'y':
            return True
        elif user_input == 'n':
            return False
        else:
            print('Invalid input. Please enter y or n.')

def change_symbols(art, symbol):
    """Change symbols in ASCII-art.
    
    Args:
        art (str): ASCII-art.
        symbol (str): Symbol to replace.
        
    Returns:
        art (str): ASCII-art with replaced symbols.
    """    
    for char in art:
        if char != '\n' and char != ' ':
            art = art.replace(char, symbol)
    
    return art 

def check_size(char_str, width, height):
    char_width = 8
    char_height = 8
    
    str_length = len(char_str) * char_width
    terminal_columns, terminal_lines = os.get_terminal_size()
    
    if width < char_width:
        raise ValueError(f"Width {width} is too small for the string length of {str_length}")
    elif width > terminal_columns:
        raise ValueError(f"Width {width} exceeds the terminal length of {terminal_columns}")
    else:
        pass
        
    if height < char_height or height < str_length / width:
        raise ValueError(f"Height {height} is too small for the string length of {str_length}")
    elif height > terminal_lines:
        raise ValueError(f"Height {height} exceeds the terminal length of {str_length}")
    else:
        pass

def preview_art(FOLDER_PATH, art):
    """Preview ASCII-art.
    
    Args:
        art (str): ASCII-art.
    """
    print(art)
    
    save_art_answ = input('Do you want to save your art? (y/n): ')
    
    if save_art_answ == 'y':
        save_art(FOLDER_PATH, art)
    else:
        pass

def save_art(FOLDER_PATH, art):    
    """Save ASCII-art to file.
    
    Args:
        art (str): ASCII-art.
    """
    file_name = input('Give a file name: ')
    formated_file_name = FOLDER_PATH + file_name + '.txt'
    
    with open(formated_file_name, 'w') as file:
        file.write(art)

def show_art(FOLDER_PATH):
    """Show ASCII-art from file.
    
    Raises:
        FileNotFoundError: If file not found.
    """
    try:
        file_name = input('Enter file name: ')
        formated_file_name = FOLDER_PATH + file_name + '.txt'
        with open(formated_file_name, 'r') as file:
            print(file.read())
    except FileNotFoundError:
        print('File not found.')