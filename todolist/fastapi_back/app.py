from fastapi import FastAPI
from db import RestApiDataBase

app = FastAPI()


@app.get('/todos')
def index():
    todos = RestApiDataBase().get_all_rows()
    results = [
        {
            "id": todo[0],
            "title": todo[1],
            "description": todo[2]
        } for todo in todos
    ]
    return results


@app.get('/todos/{id_}')
def detailed_index(id_: int):
    todo = RestApiDataBase().get_one_row(id_=id_)
    try:
        result = {
            "id": todo[0],
            "title": todo[1],
            "description": todo[2]
        }
        return result
    except TypeError:
        return {"detail": "Row does not exist"}


@app.post('/todos')
def index_post(title: str, desc: str):
    RestApiDataBase().create(title=title, description=desc)
    return {"title": title, "description": desc}


@app.put('/todos/{id_}')
def index_put(id_: int, title: str, desc: str):
    RestApiDataBase().update(id_=id_, title=title, description=desc)
    return {"title": title, "description": desc}


@app.delete('/todos/{id_}')
def index_delete(id_: int):
    RestApiDataBase().delete(id_=id_)
    return {"detail": "Object has been deleted."}
