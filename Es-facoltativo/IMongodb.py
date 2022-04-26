from pymongo.mongo_client import MongoClient

# todos e users contengono gli elementi che verranno
# inseriti nel database come dati di esempio
todos = [
    {"userId": 1, "id": 1, "title": "Fare la spesa", "completed": False},
    {"userId": 1, "id": 2, "title": "Studiare per l'esame", "completed": True},
    {"userId": 2, "id": 3, "title": "Riordinare gli appunti", "completed": True},
    {"userId": 2, "id": 4, "title": "Andare a correre", "completed": False}
]

users = [
    {"id":1,"name":"Mario Rossi","username":"MR","email":"mario.rossi@test.com","address":{"street":"Via Saragat","suite":"Apt. 1","city":"Ferrara","zipcode":"44122","geo":{"lat":"44.8333129","lng":"11.5973502"}},"phone":"123-456-789","website":"unife.it","company":{"name":"Università degli Studi di Ferrara","catchPhrase":"ReST","bs":"API"}},
    {"id":2,"name":"Luigi Bianchi","username":"LB","email":"luigi.bianchi@test.com","address":{"street":"Via Saragat","suite":"Apt. 13","city":"Ferrara","zipcode":"44122","geo":{"lat":"44.8312366","lng":"11.5971991"}},"phone":"987-654-321","website":"unife.it","company":{"name":"Università degli Studi di Ferrara","catchPhrase":"ReST","bs":"API"}}
]

client = None
db = None

def init_db():
    global client, db
    client = MongoClient()
    db = client.rest # Crea un database chiamato "rest"
    db.todos.drop() # Elimina tutti i todo dal database
    db.users.drop() # Elimina tutti gli utenti dal database
    insert_sample_data()

def insert_sample_data():
    for todo in todos:
        db.todos.insert_one(todo)
    for user in users:
        db.users.insert_one(user)

def find_max_todo_id():
    result = db.todos.find({}).sort([{'id',-1}]).limit(1)
    a_list = list(result)
    return int(a_list[0]["id"])

def find_max_user_id():
    result = db.users.find({}).sort([{'id',-1}]).limit(1)
    a_list = list(result)
    return int(a_list[0]["id"])

def find_todo_by_id(id):
    result = db.todos.find_one({'id': int(id)})
    return result

def find_user_by_id(id):
    result = db.users.find_one({'id': int(id)})
    return result

def find_todos_by_user_id(userId):
    result = db.todos.find({'userId': int(userId)})
    return list(result)

def find_all_todos():
    result = db.todos.find()
    return list(result)

def find_all_users():
    result = db.users.find()
    return list(result)

def insert_todo(todo):
    result = db.todos.insert_one(todo)
    return result.inserted_id

def insert_user(user):
    result = db.users.insert_one(user)
    return result

def delete_todo_by_id(id):
    result = db.todos.delete_one({'id': int(id)})
    return result

def delete_user_by_id(id):
    result = db.users.delete_one({'id': int(id)})
    return result
