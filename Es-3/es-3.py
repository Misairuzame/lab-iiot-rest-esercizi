import requests

if __name__ == "__main__":
    api_url = "http://jsonplaceholder.typicode.com"
    my_headers = {"Content-type": "application/json"}

    # GET /users/1/todos
    # Recuperare i todo dell'utente con id 1
    # TODO:
    print("GET /users/1/todos")

    # POST /users/1/todos
    # Aggiungere un nuovo todo per l'utente 1,
    # il cui id verrà assegnato automaticamente
    # dal server
    # TODO:
    print("\n")
    print("POST /users/1/todos")
