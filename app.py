from flask import Flask, request, jsonify
from models.task import Task

app = Flask(__name__)

tasks = []

@app.route("/task",methods=['POST'])
def create():
    data = request.get_json()
    newTask = Task(id=data["id"], title=data["title"], description=data.get("description", ""))
    tasks.append(newTask)
    return jsonify({"message": "Sucesso!"})

@app.route("/tasks", methods=["GET"])
def getAll():
    output = {
        "tasks": [task.to_dict() for task in tasks],
        "total_tasks": len(tasks)
    }
    return jsonify(output)

@app.route("/task/<int:id>", methods=["GET"])
def get(id):
    for t in tasks:
        if t.get_id() == id:
            return jsonify(t.to_dict())
    return jsonify({"message": "Tarefa não encontrada"}), 404

@app.route("/task/<int:id>", methods=["PUT"])
def update(id):
    data = request.get_json()
    for t in tasks:
        if t.get_id() == id:
            t.set_title(data["title"])
            t.set_description(data["description"])
            t.set_completed(data["completed"])
            return jsonify(t.to_dict()) 
    return jsonify({"message": "Tarefa não encontrada"}),

@app.route("/task/<int:id>", methods=["DELETE"])
def remove(id):
    task = None
    for t in tasks:
        if t.get_id() == id:
           task = t
           break
    if task == None:
        return jsonify({"message": "Tarefa não encontrada"}), 404
    
    tasks.remove(task)
    return jsonify({"message": "Tarefa removida com sucesso!"})

if __name__ == "__main__":
    app.run(debug=True)