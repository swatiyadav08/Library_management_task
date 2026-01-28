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
#### Why did I choose this approach?

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

#### Hardest Bug Faced & How I Fixed It : 

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
* Add Book (POST /books)
![add book](https://github.com/user-attachments/assets/db973dac-3679-4f4d-8988-8fab5ba9f6e8)



* Get Book by iD(Get /books/{id})
![get_book_by_id](https://github.com/user-attachments/assets/1b67f583-51b1-44d9-8b8e-3f55252c7fd8)



* SEARCH BOOK BY YEAR(GET /books/search?year=2018)
<img width="1907" height="1015" alt="search book by year" src="https://github.com/user-attachments/assets/72f8eae2-c96b-44a0-be68-d05e53b3719e" />



* Delete Book (DELETE /books/{id}
![delete_book_by_id](https://github.com/user-attachments/assets/fd22892e-1c1a-4479-bad1-74680471242b)



### 5. Future Improvements

If more time was available, the following enhancements could be added:

Database integration (MySQL / PostgreSQL)

Update book endpoint (PUT /books/{id})

User authentication & authorization

Pagination for large data

Swagger / OpenAPI documentation

Unit testing
