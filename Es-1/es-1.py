import requests

"""
Per inserire dei dati nel body della
richiesta, innanzitutto creare un dizionario
contenente i dati da inviare, ad esempio:
da_inviare = {
        "titolo": "Titolo di esempio",
        "quantità": 12345,
        "messaggio": "testo di esempio",
        "valore": 10
    }
Successivamente specificare l'opzione
json=da_inviare dopo l'opzione headers=my_headers
della richiesta.
"""

"""
Su jsonplaceholder le risorse non vengono veramente inserite,
modificate o eliminate, quindi quando vengono recuperate dopo
una di queste azioni non si ha un riscontro di quanto fatto.
"""

if __name__ == "__main__":
    api_url = "http://jsonplaceholder.typicode.com"
    my_headers = {"Content-type": "application/json"}

    # GET /todos
    # Recuperare tutti i Todo
    print("GET /todos")
    res = requests.get(f"{api_url}/todos", headers=my_headers)
    print(f"Stato HTTP: {res.status_code}")
    print(f"Risposta dal server:\n{res.json()}")

    # GET /todos/1
    # Recuperare il Todo con id 1
    # TODO:
    print("\n")
    print("GET /todos/1")

    # POST /todos
    # Aggiungere un nuovo Todo, il cui id verrà
    # assegnato automaticamente dal server,
    # quindi non è da specificare
    # TODO:
    print("\n")
    print("POST /todos")

    # PUT /todos/1
    # Modificare/Sostituire il Todo con id 1.
    # In questo caso va specificata l'intera
    # risorsa, compreso l'id
    # TODO:
    print("\n")
    print(f"PUT /todos/1")

    # DELETE /todos/5
    # Eliminare il Todo con id 5
    # TODO:
    print("\n")
    print(f"DELETE /todos/5")
