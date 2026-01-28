# In-Memory Library Management API
### 1. Project Title & Goal

This project is a REST API built using Flask that manages a library book inventory using in-memory storage (Python dictionary) without any database.

### 2. Setup Instructions
Requirements

Python 3.10+

Install dependencies
pip install -r requirements.txt

Run the server
python app.py

Server will run at:
http://127.0.0.1:5000

### 3. The Logic (How I Thought)
Why did I choose this approach?

The project requirement focuses on in-memory storage, so I used a Python dictionary (books = {}) to store all book records during runtime. No database is used.

I chose Flask because:

It is lightweight and simple

Perfect for quickly building REST APIs

Easy routing and JSON handling

Each book is stored in this format:

books = {
    book_id: {
        "title": "...",
        "author": "...",
        "year": ...
    }
}

Hardest Bug Faced & How I Fixed It : 

While testing the API, invalid or missing JSON input caused unexpected behavior.
To fix this, I added validation:

Checked if request body exists

Verified all required fields (id, title, author, year)

Added proper HTTP status codes:

400 for bad request

404 for not found

409 for duplicates

201 for successful creation

This ensures the API behaves predictably and follows REST standards.

### 4. Ouput ScreenShots
Add Book (POST /books)


Get Book by iD(Get /books/{id})


SEARCH BOOK BY YEAR(GET /books/search?year=2018)


Delete Book (DELETE /books/{id}


### 5. Future Improvements

If more time was available, the following enhancements could be added:

Database integration (MySQL / PostgreSQL)

Update book endpoint (PUT /books/{id})

User authentication & authorization

Pagination for large data

Swagger / OpenAPI documentation

Unit testing
