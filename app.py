from flask import Flask, request, jsonify

app = Flask(__name__)


books = {}

@app.route('/')
def home():
    return jsonify({
        "message": "Library Management API",
        "routes": {
            "Add book": "POST /books",
            "Get book": "GET /books/<id>",
            "Search by year": "GET /books/search?year=2024",
            "Delete book": "DELETE /books/<id>"
        }
    })



@app.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Send data in JSON format"}), 400

    book_id = data.get("id")
    title = data.get("title")
    author = data.get("author")
    year = data.get("year")

    # Simple validation
    if not book_id or not title or not author or not year:
        return jsonify({"error": "id, title, author, year are required"}), 400

    # Duplicate check
    if book_id in books:
        return jsonify({"error": "Book already exists"}), 409

    books[book_id] = {
        "title": title,
        "author": author,
        "year": year
    }

    return jsonify({"message": "Book added successfully"}), 201



@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    if book_id not in books:
        return jsonify({"error": "Book not found"}), 404

    return jsonify({
        "id": book_id,
        **books[book_id]
    })



@app.route('/books/search', methods=['GET'])
def search_books():
    year = request.args.get('year')

    if not year:
        return jsonify({"error": "Year query parameter required"}), 400

    result = []

    for book_id, book in books.items():
        if str(book["year"]) == year:
            result.append({"id": book_id, **book})

    if not result:
        return jsonify({"message": "No books found"}), 404

    return jsonify(result)

@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    if book_id not in books:
        return jsonify({"error": "Book not found"}), 404

    books.pop(book_id)
    return jsonify({"message": "Book deleted successfully"})

if __name__ == '__main__':
    app.run(debug=True)