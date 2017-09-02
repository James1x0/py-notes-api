import logging
from flask import Flask
from flask_restful import Resource, Api
from flask_pymongo import PyMongo

app = Flask(__name__)
api = Api(app)
mongo = PyMongo(app)

class Note(Resource):
  def get(self, note_id):
    note = mongo.db.notes.find_one_or_404(note_id)
    return { note: note }

  def put(self, note_id):
    args = parser.parse_args()
    note = {'note': args['note']}
    result = mongo.db.notes.replace_one(note_id, note)
    return result;

api.add_resource(Note, '/notes/<string:note_id>')

if __name__ == '__main__':
  app.run(debug=True)
