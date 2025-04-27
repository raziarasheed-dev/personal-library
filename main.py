import os
import json

# File name for saving/loading the library
FILE_NAME = "library.json"

# Load the library from file if it exists
def load_library():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as file:
            return json.load(file)
    return []

# Save the library to file
def save_library(library):
    with open(FILE_NAME, 'w') as file:
        json.dump(library, file, indent=4)

# Add a book to the library
def add_book(library):
    title = input("Enter the book title: ").strip()
    author = input("Enter the author: ").strip()
    try:
        year = int(input("Enter the publication year: ").strip())
    except ValueError:
        print("Invalid year. Setting publication year to 0.")
        year = 0
    genre = input("Enter the genre: ").strip()
    read_input = input("Have you read this book? (yes/no): ").strip().lower()
    read_status = read_input == 'yes'
    
    book = {
        'Title': title,
        'Author': author,
        'Year': year,
        'Genre': genre,
        'Read': read_status
    }
    library.append(book)
    print("Book added successfully!")

# Remove a book by title
def remove_book(library):
    title = input("Enter the title of the book to remove: ").strip()
    for book in library:
        if book['Title'].lower() == title.lower():
            library.remove(book)
            print("Book removed successfully!")
            return
    print("Book not found.")

# Search for a book by title or author
def search_book(library):
    print("Search by:\n1. Title\n2. Author")
    choice = input("Enter your choice: ").strip()
    if choice not in ['1', '2']:
        print("Invalid choice.")
        return
    query = input("Enter the search term: ").strip().lower()
    matches = []
    for book in library:
        if choice == '1' and query in book['Title'].lower():
            matches.append(book)
        elif choice == '2' and query in book['Author'].lower():
            matches.append(book)
    if matches:
        print("Matching Books:")
        for idx, book in enumerate(matches, 1):
            display_book(book, idx)
    else:
        print("No matching books found.")

# Display all books
def display_books(library):
    if not library:
        print("Library is empty.")
        return
    print("Your Library:")
    for idx, book in enumerate(library, 1):
        display_book(book, idx)

# Helper function to display a single book
def display_book(book, idx):
    read_status = "Read" if book['Read'] else "Unread"
    print(f"{idx}. {book['Title']} by {book['Author']} ({book['Year']}) - {book['Genre']} - {read_status}")

# Display statistics
def display_statistics(library):
    total = len(library)
    if total == 0:
        print("No books in library.")
        return
    read_books = sum(1 for book in library if book['Read'])
    percentage = (read_books / total) * 100
    print(f"Total books: {total}")
    print(f"Percentage read: {percentage:.1f}%")

# Main menu loop
def menu():
    library = load_library()
    while True:
        print("\nMenu\nWelcome to your Personal Library Manager!")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            add_book(library)
        elif choice == '2':
            remove_book(library)
        elif choice == '3':
            search_book(library)
        elif choice == '4':
            display_books(library)
        elif choice == '5':
            display_statistics(library)
        elif choice == '6':
            save_library(library)
            print("Library saved to file. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Start the program
if __name__ == "__main__":
    menu()
