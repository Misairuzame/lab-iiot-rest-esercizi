from flask import Flask, request, jsonify

app = Flask(__name__)

users = [
    {"id":"1","name":"Mario Rossi","username":"MR","email":"mario.rossi@test.com","address":{"street":"Via Saragat","suite":"Apt. 1","city":"Ferrara","zipcode":"44122","geo":{"lat":"44.8333129","lng":"11.5973502"}},"phone":"123-456-789","website":"unife.it","company":{"name":"Università degli Studi di Ferrara","catchPhrase":"ReST","bs":"API"}},
    {"id":"2","name":"Luigi Bianchi","username":"LB","email":"luigi.bianchi@test.com","address":{"street":"Via Saragat","suite":"Apt. 13","city":"Ferrara","zipcode":"44122","geo":{"lat":"44.8312366","lng":"11.5971991"}},"phone":"987-654-321","website":"unife.it","company":{"name":"Università degli Studi di Ferrara","catchPhrase":"ReST","bs":"API"}}
]

def _find_next_user_id():
    return max(user["id"] for user in users) + 1

def _find_user_by_id(id):
    for user in users:
        if user["id"] == int(id):
            return user
    return None

# Prima di servire qualsiasi richiesta,
# verificare che il Content-type sia
# application/json, se non lo è allora
# restituire un messaggio di errore
@app.before_request
def check_cont_type_json():
    if not request.is_json:
        return {"errore": "Content-type non supportato (deve essere JSON)"}, 415


# ----- USERS -----


# Recupera tutti gli utenti
# TODO:
@app.get("/users")


# Recupera un utente dato il suo ID
# Se non lo trova, restituisce un
# oggetto JSON vuoto, ovvero {}, e
# risponde con stato HTTP 404
# TODO:
@app.get("/users/<id>")


# Crea un nuovo utente, del quale l'id
# viene impostato al successivo id disponibile
# (come se fosse un autoincrementante)
# TODO:
@app.post("/users")


# Modifica/Sostituisce un utente esistente,
# restituendo al Client la "nuova" risorsa
# e lo stato HTTP 201
# TODO:
@app.put("/users/<id>")


# Elimina un utente esistente
# TODO:
@app.delete("/users/<id>")
