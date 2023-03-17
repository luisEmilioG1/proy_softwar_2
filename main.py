from typing import Union
from fastapi import FastAPI

app = FastAPI()

users = [
    {'id': 1, 'username':'jRei', 'password':'quiz'},
    {'id': 2, 'username':'Manuel', 'password':'quiz2'},
    {'id': 3, 'username':'María', 'password':'quiz3'},
    {'id': 4, 'username':'Chat', 'password':'GPT'},
    {'id': 5, 'username':'Claudia', 'password':'quiz4'}
    ]

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get('/user/all')
def get_all_users():
    return users

@app.get('/user/{id}')
def get_user_by_id(id: int):
    for user in users:
        if user['id'] == id : 
            return user
    return 'not found user'

''' @app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q} '''