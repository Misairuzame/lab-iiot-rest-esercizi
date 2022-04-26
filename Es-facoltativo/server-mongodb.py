from flask import Flask, request, jsonify
import json
from bson.json_util import ObjectId
import IMongodb

class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        return super(MyEncoder, self).default(obj) 

app = Flask(__name__)
app.json_encoder = MyEncoder

IMongodb.init_db()

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
# TODO:
@app.get("/todos")
def get_todos():


# Recupera un Todo dato il suo ID
# Se non lo trova, restituisce un
# oggetto JSON vuoto, ovvero {}, e
# risponde con stato HTTP 404
# TODO:
@app.get("/todos/<id>")
def get_todo_by_id(id):


# Crea un nuovo Todo, del quale l'id
# viene impostato al successivo id disponibile
# (come se fosse un autoincrementante)
# TODO:
@app.post("/todos")
def add_todo():


# Modifica/Sostituisce un Todo esistente,
# restituendo al Client la "nuova" risorsa
# e lo stato HTTP 201
# TODO:
@app.put("/todos/<id>")
def put_todo(id):


# Elimina un Todo esistente
# TODO:
@app.delete("/todos/<id>")
def delete_todo(id):


# ----- USERS -----


# Recupera tutti gli utenti
# TODO:
@app.get("/users")
def get_users():


# Recupera un utente dato il suo ID
# Se non lo trova, restituisce un
# oggetto JSON vuoto, ovvero {}, e
# risponde con stato HTTP 404
# TODO:
@app.get("/users/<id>")
def get_user_by_id(id):


# Crea un nuovo utente, del quale l'id
# viene impostato al successivo id disponibile
# (come se fosse un autoincrementante)
# TODO:
@app.post("/users")
def add_user():


# Modifica/Sostituisce un utente esistente,
# restituendo al Client la "nuova" risorsa
# e lo stato HTTP 201
# TODO:
@app.put("/users/<id>")
def put_user(id):


# Elimina un utente esistente
# TODO:
@app.delete("/users/<id>")
def delete_user(id):


# ----- USERS/<ID>/TODOS -----


# Restituisce tutti i todo appartenenti
# all'utente con l'id specificato
# TODO:
@app.get("/users/<id>/todos")
def get_todos_by_user(id):


# Aggiunge ai todo dell'utente con id
# specificato un nuovo todo
# TODO:
@app.post("/users/<id>/todos")
def add_todo_to_user(id):
