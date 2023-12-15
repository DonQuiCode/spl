import sys 
sys.path.append('/Users/admin/Desktop/lpnu/5 сем/Specialised programming languages/source')
from shared.ascii_settings import AsciiArtSettings
from service.lab3.ascii_art_generator_service import create_ascii_art
from shared.ascii_utils import show_art
from shared.ascii_utils import set_font, set_size, set_symbols, set_color

FOLDER_PATH = 'data/lab3/ASCII-arts/'
SETTINGS_FILE_PATH = 'data/lab3/settings.json'

class AsciiArtMenu:
    def run(self):    
        settings_obj = AsciiArtSettings()
        settings_obj.set_settings_file_path(SETTINGS_FILE_PATH)
        settings_obj.load_settings()
        
        while True:
            print('Options (1/2/3):')
            print('1. Create ASCII-art')
            print('2. Show ASCII-art')
            print('3. Settings')
            print('4. Exit')
            
            user_input = input('Enter option number: ')
            
            if user_input == '1':
                create_ascii_art(FOLDER_PATH, settings_obj)
            elif user_input == '2':
                show_art(FOLDER_PATH)
            elif user_input == '3':
                settings_menu(settings_obj)
            elif user_input == '4':
                break
            
    def settings_menu(settings_obj):    
        while True:
            print('Options (1/2/3/4/5/6):')
            print('0. Show current settings')
            print('1. Change font')
            print('2. Change size')
            print('3. Change symbol')
            print('4. Change color')
            print('5. Reset settings')
            print('6. Back')
            
            user_input = input('Enter option number: ')
            if user_input == '0':
                settings_obj.show_settings()
            if user_input == '1':
                settings_obj.set_font(set_font())
            elif user_input == '2':
                settings_obj.set_size(*set_size())
            elif user_input == '3':
                settings_obj.set_symbols(*set_symbols())
            elif user_input == '4':
                settings_obj.set_color(set_color())
            elif user_input == '5':
                settings_obj.default_settings()
            elif user_input == '6':
                break