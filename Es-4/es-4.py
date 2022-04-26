from flask import Flask, request, jsonify

"""
Per accedere al body della request, ad esempio nel
caso in cui il Client abbia inviato i dati di un
nuovo todo da inserire, utilizzare il metodo
request.get_json()
"""

app = Flask(__name__)

todos = [
    {"userId": 1, "id": 1, "title": "Fare la spesa", "completed": False},
    {"userId": 1, "id": 2, "title": "Studiare per l'esame", "completed": True},
    {"userId": 2, "id": 3, "title": "Riordinare gli appunti", "completed": True},
    {"userId": 2, "id": 4, "title": "Andare a correre", "completed": False}
]


def _find_next_id():
    return max(todo["id"] for todo in todos) + 1


def _find_todo_by_id(id):
    for todo in todos:
        if todo["id"] == int(id):
            return todo
    return None


# Prima di servire qualsiasi richiesta,
# verificare che il Content-type sia
# application/json, se non lo è allora
# restituire un messaggio di errore
@app.before_request
def check_cont_type_json():
    if not request.is_json:
        return {"errore": "Content-type non supportato (deve essere JSON)"}, 415


# Recupera tutti i Todo
# TODO:
@app.get("/todos")


# Recupera un Todo dato il suo ID
# Se non lo trova, restituisce un
# oggetto JSON vuoto, ovvero {}, e
# risponde con stato HTTP 404
# TODO:
@app.get("/todos/<id>")


# Crea un nuovo Todo, del quale l'id
# viene impostato al successivo id disponibile.
# Usare il metodo _find_next_id.
# TODO:
@app.post("/todos")


# Modifica/Sostituisce un Todo esistente,
# restituendo al Client la "nuova" risorsa
# e lo stato HTTP 201
# TODO:
@app.put("/todos/<id>")


# Elimina un Todo esistente
# TODO:
@app.delete("/todos/<id>")
