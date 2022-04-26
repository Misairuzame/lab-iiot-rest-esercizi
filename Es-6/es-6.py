from flask import Flask, request, jsonify

app = Flask(__name__)

todos = [
    {"userId": 1, "id": 1, "title": "Fare la spesa", "completed": False},
    {"userId": 1, "id": 2, "title": "Studiare per l'esame", "completed": True},
    {"userId": 2, "id": 3, "title": "Riordinare gli appunti", "completed": True},
    {"userId": 2, "id": 4, "title": "Andare a correre", "completed": False}
]

users = [
    {"id":"1","name":"Mario Rossi","username":"MR","email":"mario.rossi@test.com","address":{"street":"Via Saragat","suite":"Apt. 1","city":"Ferrara","zipcode":"44122","geo":{"lat":"44.8333129","lng":"11.5973502"}},"phone":"123-456-789","website":"unife.it","company":{"name":"Università degli Studi di Ferrara","catchPhrase":"ReST","bs":"API"}},
    {"id":"2","name":"Luigi Bianchi","username":"LB","email":"luigi.bianchi@test.com","address":{"street":"Via Saragat","suite":"Apt. 13","city":"Ferrara","zipcode":"44122","geo":{"lat":"44.8312366","lng":"11.5971991"}},"phone":"987-654-321","website":"unife.it","company":{"name":"Università degli Studi di Ferrara","catchPhrase":"ReST","bs":"API"}}
]


def _find_next_id():
    return max(todo["id"] for todo in todos) + 1

def _find_next_user_id():
    return max(user["id"] for user in users) + 1

def _find_todo_by_id(id):
    for todo in todos:
        if todo["id"] == id or todo["id"] == int(id):
            return todo
    return None

def _find_user_by_id(id):
    for user in users:
        if user["id"] == id or user["id"] == int(id):
            return user
    return None

def _find_todos_by_user_id(id):
    to_return = []
    for todo in todos:
        if todo["userId"] == id or todo["userId"] == int(id):
            to_return.append(todo)
    return to_return

# Prima di servire qualsiasi richiesta,
# verificare che il Content-type sia
# application/json, se non lo è allora
# restituire un messaggio di errore
@app.before_request
def check_cont_type_json():
    if not request.is_json:
        return {"errore": "Content-type non supportato (deve essere JSON)"}, 415


# ----- TODOS -----


# Recupera tutti i Todo
@app.get("/todos")
def get_todos():
    return jsonify(todos), 200


# Recupera un Todo dato il suo ID
# Se non lo trova, restituisce un
# oggetto JSON vuoto, ovvero {}, e
# risponde con stato HTTP 404
@app.get("/todos/<id>")
def get_todo_by_id(id):
    to_return = _find_todo_by_id(id)
    if to_return is None:
        return "{}", 404
    else:
        return jsonify(to_return), 200


# Crea un nuovo Todo, del quale l'id
# viene impostato al successivo id disponibile
# (come se fosse un autoincrementante)
@app.post("/todos")
def add_todo():
    todo = request.get_json()
    todo["id"] = _find_next_id()
    todos.append(todo)
    return todo, 201


# Modifica/Sostituisce un Todo esistente,
# restituendo al Client la "nuova" risorsa
# e lo stato HTTP 201
@app.put("/todos/<id>")
def put_todo(id):
    todo = request.get_json()
    old_todo = _find_todo_by_id(id)
    todos.remove(old_todo)
    todos.append(todo)
    return todo, 201


# Elimina un Todo esistente
@app.delete("/todos/<id>")
def delete_todo(id):
    old_todo = _find_todo_by_id(id)
    todos.remove(old_todo)
    return {"message": "OK"}, 200


# ----- USERS -----


# Recupera tutti gli utenti
@app.get("/users")
def get_users():
    return jsonify(users), 200


# Recupera un utente dato il suo ID
# Se non lo trova, restituisce un
# oggetto JSON vuoto, ovvero {}, e
# risponde con stato HTTP 404
@app.get("/users/<id>")
def get_user_by_id(id):
    to_return = _find_user_by_id(id)
    if to_return is None:
        return "{}", 404
    else:
        return jsonify(to_return), 200


# Crea un nuovo utente, del quale l'id
# viene impostato al successivo id disponibile
# (come se fosse un autoincrementante)
@app.post("/users")
def add_user():
    user = request.get_json()
    user["id"] = _find_next_user_id()
    users.append(user)
    return user, 201


# Modifica/Sostituisce un utente esistente,
# restituendo al Client la "nuova" risorsa
# e lo stato HTTP 201
@app.put("/users/<id>")
def put_user(id):
    user = request.get_json()
    old_user = _find_user_by_id(id)
    users.remove(old_user)
    users.append(user)
    return user, 201


# Elimina un utente esistente
@app.delete("/users/<id>")
def delete_todo(id):
    old_user = _find_user_by_id(id)
    users.remove(old_user)
    return {"message": "OK"}, 200


# ----- USERS/<ID>/TODOS -----


# Restituisce tutti i todo appartenenti
# all'utente con l'id specificato
# TODO:
@app.get("/users/<id>/todos")


# Aggiunge ai todo dell'utente con id
# specificato un nuovo todo
# TODO:
@app.post("/users/<id>/todos")
