from flask import Flask
from flask_restful import reqparse, abort, Api, Resource, fields, marshal_with
from flask_restful_swagger import swagger
app = Flask(__name__)
api = swagger.docs(Api(app), apiVersion='0.1')


class TodoDao():
    def __init__(self, todo_id, task):
        self.todo_id = todo_id
        self.task = task
        self.status = 'active'


TODOS = {
    'todo1': TodoDao(todo_id='todo1', task='Remember the milk'),
    'todo2': TodoDao(todo_id='todo2', task='Remember the bread'),
    'todo3': TodoDao(todo_id='todo3', task='Remember the bank'),
}


def abort_if_todo_doesnt_exist(todo_id):
    if todo_id not in TODOS:
        abort(404, message="Todo {} doesn't exist".format(todo_id))


parser = reqparse.RequestParser()
parser.add_argument('task', type=str, required=True)

resource_fields = {
    'todo_id': fields.String(),
    'task': fields.String()
}

resource_fields_list = {
    'tasks': fields.List(fields.Nested(resource_fields))
}


class Todo(Resource):
    @marshal_with(resource_fields)
    def get(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        return TODOS[todo_id]

    def delete(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        del TODOS[todo_id]
        return '', 204

    @marshal_with(resource_fields)
    def put(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        args = parser.parse_args()
        task = TODOS[todo_id]
        task.task = args['task']
        return task, 201


class TodoList(Resource):
    @marshal_with(resource_fields_list)
    def get(self):
        return {"tasks": list(TODOS.values())}

    @marshal_with(resource_fields)
    def post(self):
        args = parser.parse_args()
        todo_id = int(max(TODOS.keys()).lstrip('todo')) + 1
        todo_id = 'todo%i' % todo_id
        TODOS[todo_id] = TodoDao(todo_id=todo_id, task=args['task'])
        return TODOS[todo_id], 201


api.add_resource(TodoList, '/todos')
api.add_resource(Todo, '/todos/<todo_id>')

if __name__ == '__main__':
    app.run(debug=True)
