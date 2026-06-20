def add_book(catalog: dict, book_id: int, title: str, author: str, year: int) -> None:
    catalog[book_id] = (title, author, year)
    print(f"Book Added: ID {book_id} -> '{title}' by {author} ({year})")


def borrow_book(catalog: dict, borrowed_books: list, book_id: int) -> bool:
    if book_id not in catalog:
        print(f"Cannot borrow: Book ID {book_id} does not exist in the catalog.")
        return False
    if book_id in borrowed_books:
        print(f"Cannot borrow: Book ID {book_id} is already borrowed.")
        return False
    borrowed_books.append(book_id)
    print(f"Book Borrowed: '{catalog[book_id][0]}' (ID {book_id})")
    return True


def return_book(borrowed_books: list, book_id: int) -> bool:
    if book_id in borrowed_books:
        borrowed_books.remove(book_id)
        print(f"Book Returned: ID {book_id}")
        return True
    else:
        print(f"Cannot return: Book ID {book_id} was not borrowed.")
        return False


def register_member(members: set, member_id: int) -> None:
    members.add(member_id)
    print(f"Member Registered: ID {member_id}")


def show_available(catalog: dict, borrowed_books: list) -> None:
    print("\n--- Available Books in Library ---")
    available_count = 0
    for book_id, details in catalog.items():
        if book_id not in borrowed_books:
            title, author, year = details
            print(f"[ID: {book_id}] '{title}' by {author} ({year})")
            available_count += 1
    if available_count == 0:
        print("No books are currently available.")
    print("----------------------------------\n")


def main():
    catalog = {}
    borrowed_books = []
    members = set()

    print("--- 1. Adding 4 Books ---")
    add_book(catalog, 1001, "The Hobbit", "J.R.R. Tolkien", 1937)
    add_book(catalog, 1002, "1984", "George Orwell", 1949)
    add_book(catalog, 1003, "To Kill a Mockingbird", "Harper Lee", 1960)
    add_book(catalog, 1004, "The Great Gatsby", "F. Scott Fitzgerald", 1925)

    print("\n--- 2. Registering Members (including one duplicate) ---")
    register_member(members, 501)
    register_member(members, 502)
    register_member(members, 501)
    register_member(members, 503)
    print(f"Current members in database (unique set): {members}")

    print("\n--- 3. Borrowing 2 Books ---")
    borrow_book(catalog, borrowed_books, 1002)
    borrow_book(catalog, borrowed_books, 1004)
    borrow_book(catalog, borrowed_books, 1002)
    borrow_book(catalog, borrowed_books, 9999)
    print(f"Currently borrowed book IDs: {borrowed_books}")

    print("\n--- 4. Returning 1 Book ---")
    return_book(borrowed_books, 1002)
    print(f"Currently borrowed book IDs: {borrowed_books}")

    print("\n--- 5. Showing Available Books ---")
    show_available(catalog, borrowed_books)


if __name__ == "__main__":
    main()
