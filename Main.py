def add_book():
    book_id = input("Enter Book ID: ")
    title = input("Enter Book Title: ")
    author = input("Enter Book Author: ")

    with open("books.txt", "a") as file:
        file.write(f"{book_id},{title},{author}\n")

    print("Book added successfully!")


def view_books():
    try:
        with open("books.txt", "r") as file:
            books = file.readlines()

        if not books:
            print("No books available.")
        else:
            print("\n--- Library Books ---")
            for book in books:
                book_id, title, author = book.strip().split(",")
                print(f"ID: {book_id}, Title: {title}, Author: {author}")

    except FileNotFoundError:
        print("No books file found.")


def search_book():
    search_id = input("Enter Book ID to search: ")
    found = False

    try:
        with open("books.txt", "r") as file:
            for line in file:
                book_id, title, author = line.strip().split(",")
                if book_id == search_id:
                    print(f"Found -> ID: {book_id}, Title: {title}, Author: {author}")
                    found = True

        if not found:
            print("Book not found.")

    except FileNotFoundError:
        print("No books file found.")


def delete_book():
    delete_id = input("Enter Book ID to delete: ")
    found = False
    books = []

    try:
        with open("books.txt", "r") as file:
            books = file.readlines()

        with open("books.txt", "w") as file:
            for line in books:
                book_id, title, author = line.strip().split(",")
                if book_id != delete_id:
                    file.write(line)
                else:
                    found = True

        if found:
            print("Book deleted successfully!")
        else:
            print("Book not found.")

    except FileNotFoundError:
        print("No books file found.")


while True:
    print("\n--- Library Management System developed by Monty---")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Delete Book")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        add_book()
    elif choice == "2":
        view_books()
    elif choice == "3":
        search_book()
    elif choice == "4":
        delete_book()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
