import requests

if __name__ == "__main__":
    api_url = "http://jsonplaceholder.typicode.com"
    my_headers = {"Content-type": "application/json"}

    # GET /users/1
    # Recuperare l'utente con id 1
    # TODO:
    print("GET /users/1")

    # POST /users
    # Aggiungere un nuovo utente, il cui id verrà
    # assegnato automaticamente dal server
    # TODO:
    print("\n")
    print("POST /users")

    # PUT /users/1
    # Modificare/Sostituire l'utente con id 1
    # TODO:
    print("\n")
    print(f"PUT /users/1")
