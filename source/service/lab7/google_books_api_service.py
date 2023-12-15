from prettytable import PrettyTable
import google_auth_oauthlib.flow
import google.auth.transport.requests
import sys

sys.path.append('/Users/admin/Desktop/lpnu/5 сем/Specialised programming languages/source')
from config.paths_config import GOOGLE_BOOKS_API_CREDENTIALS, GOOGLE_BOOKS_API_OUTPUT
from shared.json_processor import JSONProcessor


class GoogleBooksApiService:
    """A simple Google Books API service class."""
    def __init__(self):
        self.credentials = self.get_credentials()
         
    def get_credentials(self):
        flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
            GOOGLE_BOOKS_API_CREDENTIALS,
            scopes=['https://www.googleapis.com/auth/books']
        )
        flow.run_local_server(port=0)
        return flow.credentials
    
    def search_books_by_title(self, credentials, title_query):
        session = google.auth.transport.requests.AuthorizedSession(credentials)
        url = "https://www.googleapis.com/books/v1/volumes"
        params = {"q": title_query}
        response = session.get(url, params=params)
        return response.json().get('items', [])

    def search_books_by_author(self, author_query):
        session = google.auth.transport.requests.AuthorizedSession(self.credentials)
        url = "https://www.googleapis.com/books/v1/volumes"
        params = {"q": f"inauthor:{author_query}"}
        response = session.get(url, params=params)
        JSONProcessor.save_data(GOOGLE_BOOKS_API_OUTPUT, f'books_by_{author_query}', response.json().get('items', []), 'json')
        return response.json().get('items', [])

    def search_books_by_isbn(self, isbn_query):
        session = google.auth.transport.requests.AuthorizedSession(self.credentials)
        url = "https://www.googleapis.com/books/v1/volumes"
        params = {"q": f"isbn:{isbn_query}"}
        response = session.get(url, params=params)
        return response.json().get('items', [])

    def list_new_releases(self, category="fiction", max_results=10):
        session = google.auth.transport.requests.AuthorizedSession(self.credentials)
        url = "https://www.googleapis.com/books/v1/volumes"
        params = {"q": f"subject:{category}", "orderBy": "newest", "maxResults": max_results}
        response = session.get(url, params=params)
        return response.json().get('items', [])

    def get_popular_books_in_category(self, category, max_results=10):
        session = google.auth.transport.requests.AuthorizedSession(self.credentials)
        url = "https://www.googleapis.com/books/v1/volumes"
        params = {"q": f"subject:{category}", "orderBy": "relevance", "maxResults": max_results}
        response = session.get(url, params=params)
        return response.json().get('items', [])

    def display_data(self, data, field_names, entity_name):
        if not data:
            print(f"No {entity_name} data to display")
            return None

        table = PrettyTable()
        table.field_names = field_names

        for idx, item in enumerate(data, start=1):
            book_info = item.get('volumeInfo', {})
            row = [idx]

            for field in field_names[1:]:  # Skip the index column
                if field == "Title":
                    title = book_info.get('title', 'N/A')
                    row.append(title)
                elif field == "Author(s)":
                    authors = ', '.join(book_info.get('authors', ['Unknown']))
                    row.append(authors)
                elif field == "Published Date":
                    published_date = book_info.get('publishedDate', 'N/A')
                    row.append(published_date)
                elif field == "ISBN":
                    isbn = ', '.join([identifier.get('identifier') for identifier in book_info.get('industryIdentifiers', []) if identifier.get('type') in ['ISBN_10', 'ISBN_13']])
                    row.append(isbn or 'N/A')
                else:
                    row.append('N/A')

            table.add_row(row)

        print(f"{entity_name.capitalize()} data:")
        print(table)
        
    def display_book_details(self, credentials, title_query):
        books = self.search_books_by_title(title_query)
        field_names = ["#", "Title", "Author(s)", "Page Count", "Categories", "Language"]
        self.display_data(books, field_names, "book")

    def display_books_by_author(self, credentials, author_query):
        books = self.search_books_by_author(author_query)
        field_names = ["#", "Title", "Author(s)", "Published Date", "ISBN"]
        self.display_data(books, field_names, "books by author")

    def display_books_by_isbn(self, credentials, isbn_query):
        books = self.search_books_by_isbn(isbn_query)
        field_names = ["#", "Title", "Author(s)", "Published Date"]
        self.display_data(books, field_names, "books by ISBN")

    def display_new_releases(self, category="fiction", max_results=10):
        books = self.list_new_releases(category, max_results)
        field_names = ["#", "Title", "Author(s)", "Published Date"]
        self.display_data(books, field_names, "new releases")

    def display_popular_books_in_category(self, category, max_results=10):
        books = self.get_popular_books_in_category(category, max_results)
        field_names = ["#", "Title", "Author(s)", "Published Date"]
        self.display_data(books, field_names, "popular books in category")
