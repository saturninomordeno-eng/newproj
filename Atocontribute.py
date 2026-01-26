books = {
    "Harry Potter": True,
    "Python Basics": True,
    "Math 101": True
}

def borrow_book(book_name):
    if book_name in books:
        if books[book_name]:
            books[book_name] = False
            print("Book borrowed successfully.")
        else:
            print("Book is already borrowed.")
    else:
        print("Book not found.")

# Example usage
borrow_book("Harry Potter")
borrow_book("Harry Potter")
