from flask import jsonify
from . import app
from .models import TodoFlask
from flask import request
from . import db


@app.route('/todos', methods=['GET', 'POST'])
def get_all_todos():
    if request.method == "GET":
        todos = TodoFlask.query.all()
        results = [
            {
                "id": todo.id,
                "title": todo.title,
                "description": todo.description
            } for todo in todos
        ]
        return jsonify(results)

    elif request.method == "POST":
        data = request.get_json()
        new_todo = TodoFlask(
            title=data['title'],
            description=data['description']
        )
        db.session.add(new_todo)
        db.session.commit()
        return {
            "message": f"{new_todo.title} has been created.",
            "status": 201
        }
    else:
        return {"error": "The request payload is not in JSON format."}


@app.route('/todos/<pk>')
def get_detail_todo(pk):
    todo = TodoFlask.query.get_or_404(pk)

    if request.method == "GET":
        result = {
            "id": todo.id,
            "title": todo.title,
            "description": todo.description
        }
        return jsonify(result)

    elif request.method == "PUT":
        data = request.get_json()
        todo.title = data['title']
        todo.description = data['description']
        db.session.add(todo)
        db.session.commit()
        return {
            "message": f"{todo.title} has been updated.",
            "status": 202
        }

    elif request.method == "DELETE":
        db.session.delete(todo)
        db.session.commit()
        return {
            "message": f"{todo.title} has been deleted.",
            "status": 203
        }
