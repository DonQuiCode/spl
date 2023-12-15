import sys
sys.path.append('/Users/admin/Desktop/lpnu/5 сем/Specialised programming languages/source')
from service.lab7.google_books_api_service import GoogleBooksApiService
from ui.menu_builder import Menu


class GoogleBooksApiMenu(Menu):
    
    def run(self):
        google_books_api_service = GoogleBooksApiService()
        credentials = google_books_api_service.get_credentials()
        
        while True:
            self.display_menu()
            
            choice = input("Enter option: ")
            if choice == '0':
                break
            if choice == '1':
                book_title =  input("Enter book title to search: ")
                google_books_api_service.display_book_details(credentials, book_title)
            elif choice == '2':
                google_books_api_service.display_books_by_author(credentials, input("Enter author name to search: "))
            elif choice == '3':
                google_books_api_service.display_books_by_isbn(credentials, input("Enter ISBN to search: "))
            elif choice == '4':
                google_books_api_service.display_new_releases(input("Enter category to search: "))
            elif choice == '5':
                google_books_api_service.display_popular_books_in_category(credentials, input("Enter category to search: "))
    
    @staticmethod
    def display_menu():
        """Display the google books api menu."""
        print("1. Search by Title")
        print("2. Search by Author")
        print("3. Display Books by ISBN")
        print("4. Display Popular books in category")
        print("5. Display New releases in category")
        print("0. Exit")