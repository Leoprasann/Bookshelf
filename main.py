from fastapi import FastAPI
from schema import Book, Genre
from logConfig import logger

app = FastAPI()

BOOK_CODE = "BS00"
count = 1

# Default books list
books = {
    "BS001": {
        "name": "Book 1",
        "edition": "2",
        "author": "author 1",
        "year": 2001,
        "pages": 396,
        "price": 999.2,
        "description": "Description of book 1 ",
        "genre": Genre.biography
    }
}


def get_book_id():
    global count
    count += 1
    book_id = BOOK_CODE + str(count)
    return book_id


@app.get("/books")
def display_books():
    response = {}
    try:
        global books
        logger.debug(f"Displaying books {books}")
        logger.info("get method for displaying books list -> done")
        response['books'] = books
    except Exception as e:
        logger.exception(f"Exception occurred at display books method --> {e}")
    return response


@app.get("/books/{book_id}")
def show_book(book_id: str):
    logger.debug("retrieve book with an id endpoint called")
    response = {}
    global books
    try:
        if book_id in books.keys():
            response = {
                book_id: books[book_id],
            }
            logger.info(f"book with id {book_id}  is {books[book_id]}")
        else:
            response = {
                book_id: "Book id doesn't exists"
            }
            logger.info(f"Book id: {book_id}, not Matched")
    except Exception as e:
        response[book_id] = f'unable to retrieve book -> {e}'
        logger.exception(f"Exception occurred at show book method --> {e}")
    return response


@app.post("/add")
def new_book(book: Book):
    logger.debug("add book endpoint called")
    # global books
    response = {}
    try:
        book_id = get_book_id()
        books[book_id] = book
        message = "Successfully added the book"
        logger.info(f"added a new book of id {book_id}: {books[book_id]}")
    except Exception as e:
        message = f"unable to add the book -> {e}"
        logger.exception(f"Exception occurred at new book method --> {e}")
    response['message'] = message
    return response


@app.put("/update/{book_id}")
def update_book(book_id: str, book: Book):
    logger.debug("update book endpoint called")
    response = {}
    try:
        if book_id in books.keys():
            books[book_id] = book
            message = f"Successfully updated the Book with id {book_id}"
            logger.info(f"found the book of id {book_id} {books[book_id]}")
        else:
            book_id = get_book_id()
            books[book_id] = book
            message = f"Book id {book_id} not exist, created new book "
            logger.info(f"book with id {book_id} not found, created a new book {books[book_id]}")
    except Exception as e:
        message = f"update operation failed -->{e}"
        logger.exception(f"Exception occurred at update book method --> {e}")
    response['message'] = message
    return response


@app.delete("/delete/{book_id}")
def remove_book(book_id: str):
    logger.debug("delete book endpoint called")
    response = {}
    try :
        if book_id in books.keys():
            del books[book_id]
            message = f"Successfully Deleted the book with id {book_id}"
            logger.info(f"deleted the book of id {book_id}")
        else:
            message = f"Book id-> {book_id}, doesn't exists"
            logger.debug("Book id doesn't match")
    except Exception as e:
        message = f"unable to delete {e}"
        logger.exception(f"Exception occurred at delete book method --> {e}")
    response['message'] = message
    return response
