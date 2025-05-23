import os
import json

LIBRARY_FILE = "library.txt"  # File ka naam jahan hum library save/load karengay

def load_library():
    # File se library load karne ka function
    if not os.path.exists(LIBRARY_FILE):
        return []  # Agar file nahi hai to empty list return kar do
    with open(LIBRARY_FILE, "r", encoding="utf-8") as f:
        try:
            return json.load(f)  # JSON format mein data load karo
        except json.JSONDecodeError:
            return []  # Agar file kharab ho to empty list return karo

def save_library(library):
    # Library ko file mein save karne ka function
    with open(LIBRARY_FILE, "w", encoding="utf-8") as f:
        json.dump(library, f, indent=4)  # JSON format mein achi tarah save karo

def add_book(library):
    # Nayi kitaab add karne ka function
    title = input("Enter the book title: ").strip()
    author = input("Enter the author: ").strip()
    
    while True:
        try:
            year = int(input("Enter the publication year: ").strip())  # Year ko integer mein convert karo
            break
        except ValueError:
            print("Please enter a valid year (integer).")  # Agar galat input ho to dobara poochho
    
    genre = input("Enter the genre: ").strip()
    
    while True:
        read_status = input("Have you read this book? (yes/no): ").strip().lower()
        if read_status in ['yes', 'no']:
            read = True if read_status == 'yes' else False  # Read status ko boolean mein convert karo
            break
        else:
            print("Please enter 'yes' or 'no'.")  # Agar galat jawaab ho to dobara poochho
    
    book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read
    }
    library.append(book)  # Library list mein nayi kitaab add karo
    print("Book added successfully!")

def remove_book(library):
    # Kitaab remove karne ka function
    title = input("Enter the title of the book to remove: ").strip()
    removed = False
    for i, book in enumerate(library):
        if book['title'].lower() == title.lower():
            del library[i]  # Jo kitaab title match karti hai usko delete karo
            removed = True
            print("Book removed successfully!")
            break
    if not removed:
        print("Book not found.")  # Agar kitaab nahi mili to ye message do

def search_book(library):
    # Kitaab search karne ka function
    print("Search by:  ")
    print("1. Title")
    print("2. Author")
    choice = input("Enter your choice: ").strip()
    
    if choice == '1':
        keyword = input("Enter the title: ").strip().lower()
        results = [book for book in library if keyword in book['title'].lower()]  # Title se match karo
    elif choice == '2':
        keyword = input("Enter the author: ").strip().lower()
        results = [book for book in library if keyword in book['author'].lower()]  # Author se match karo
    else:
        print("Invalid choice.")
        return
    
    if results:
        print("Matching Books:")
        for i, book in enumerate(results, 1):
            read_str = "Read" if book['read'] else "Unread"
            print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {read_str}")
    else:
        print("No matching books found.")

def display_all_books(library):
    # Library ki saari kitaabein display karne ka function
    if not library:
        print("Your library is empty.")  # Agar library khaali ho to message do
        return
    print("Your Library:")
    for i, book in enumerate(library, 1):
        read_str = "Read" if book['read'] else "Unread"
        print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {read_str}")

def display_statistics(library):
    # Library ki statistics dikhane ka function
    total = len(library)
    if total == 0:
        print("No books in the library to show statistics.")
        return
    read_count = sum(book['read'] for book in library)  # Kitni kitaabein padhi gayi hain
    percentage_read = (read_count / total) * 100
    print(f"Total books: {total}")
    print(f"Percentage read: {percentage_read:.1f}%")

def main():
    library = load_library()  # Program shuru hotay hi library load karo
    print("Welcome to your Personal Library Manager!")
    
    while True:
        print("\nMenu")
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
            display_all_books(library)
        elif choice == '5':
            display_statistics(library)
        elif choice == '6':
            save_library(library)  # Program band karne se pehle library save karo
            print("Library saved to file. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
