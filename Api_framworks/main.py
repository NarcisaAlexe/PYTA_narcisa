import json
import uuid 

# dupa ce am instalat libraria cu: pip install flask
from flask import Flask, request, Response

app = Flask(__name__)

fake_library_db = {
    "books": [
        {
            "id": "buid1",
            "title": "A song of ice and fire 1",
            "author": "George R. R. Martin",
            "pages": 700,
            "category": "Fantasy"
        },
        {
            "id": "buid2",
            "title": "Moara cu noroc",
            "author": "Ioan Slavici",
            "pages": 50,
            "category": "Nouvel"
        },
        {
            "id": "buid3",
            "title": "A song of ice and fire 2",
            "author": "George R. R. Martin",
            "pages": 680,
            "category": "Fantasy"
        },
    ],
    "users": [
        {
            "id": "uuid1",
            "name": "primul",
            "email": "primul@mylib.com",
            "password": "1111",
            "is_logged": False
        },
        {
            "id": "uuid2",
            "name": "second",
            "email": "second@mylib.com",
            "password": "2222",
            "is_logged": False
        },
        {
            "id": "uuid3",
            "name": "terzo",
            "email": "terzo@mylib.com",
            "password": "3333",
            "is_logged": False
        },
    ]
}

# API endpoints
@app.route("/", methods=["GET"])
def index():
    return {"message": "Hello Pythonistas!!"}


@app.route("/display_message", methods=["POST"])
def display_msg():
    # datele primite de flask pe un request de tip POST (request body-ul) se regaseste in obiectul request.data (! obiectul request trebuie importat)
    requested_message = json.loads(request.data)  # incarcam datele primte sub forma de string intr`un dict (deserializam cu json.loads)
    return json.dumps({"response_mesage": f'Hello, the message to display is: {requested_message["message"]}'}) # serializam cu json.dumps si trimitem unhttp response


# Book APIs
# read all books
@app.route("/books", methods=["GET"])
def read_all_books():
    list_of_books = fake_library_db["books"]
    return json.dumps(list_of_books)

# read book
@app.route("/books/<book_id>", methods=["GET"])
def read_book(book_id):
    for book_dict in fake_library_db["books"]:
        if book_dict['id'] == book_id:
            return Response(status=200, response=json.dumps(book_dict))
    return Response(status=404, response=json.dumps({"response_message": f"The book with id {book_id} has not been found in DB."}))

# create book
@app.route("/books/add", methods=["POST"])
def add_book():
    # POST - adaugam/trimite date catre server (salvam in fake_db)
    # 1. luam datele de pe request
    # 2. (in mod normal se verifica ca datele sa fie valide)
    # 3. salvam datele in db
    user_data = json.loads(request.data)
    # asignam un id noului user
    user_id = str(uuid.uuid4())
    user_data['id'] = user_id
    fake_library_db["books"].append(user_data)
    return Response(status=201, response=json.dumps({"response_message": f"User with id {user_id} has been successfully created"}))

# delete book
@app.route("/books/delete/<book_id>", methods=["DELETE"])
def delete_book(book_id):
    for book_dict in fake_library_db["books"]:
        if book_dict['id'] == book_id:
            fake_library_db["books"].remove(book_dict)
            return Response(status=200, response=json.dumps({"response_message": f"The book with id {book_id} has been successfully removed from DB."}))
    return Response(status=404, response=json.dumps({"response_message": f"The book with id {book_id} has not been found in DB."}))

# update book
@app.route("/books/update/<book_id>", methods=["PATCH"])
def update_book(book_id):
    book_data = json.loads(request.data)  # luam datele cu care facem update de pe body-ul requestului
    for book_dict in fake_library_db["books"]:
        if book_dict['id'] == book_id:
            book_dict.update(book_data)
            return Response(status=200, response=json.dumps({"response_message": f"The book with id {book_id} has been successfully updated in DB."}))
    return Response(status=404, response=json.dumps({"response_message": f"The book with id {book_id} has not been found in DB."}))


# TODO: get all books with category "Nouvel"


# TODO: get all books from author "George R. R. Martin"


# TODO:
# User APIs

# create user

# read all users

# read user by id

# update user

# delete user


if __name__ == '__main__':  # prima linie de cod care se citeste (dupa import-uri) in momentul in care rulam fisierul ca un script: python main.py
    app.run(debug=True, port=7000)
