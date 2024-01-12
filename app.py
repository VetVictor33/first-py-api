from flask import Flask, jsonify, request

app = Flask(__name__)

books = [
  {'id': '1', 'title': 'Clean code', 'author': 'Robert Martin'},
  {'id': '2', 'title': 'Las Venas Abiertas de America Latina', 'author': 'Eduardo Galeano'},
  {'id':'3', 'title':'I, Robot', 'author': 'Isaac Asimov'}
]

@app.route('/books', methods=['POST'])
def create_book():
  new_book = request.get_json()
  books.append(new_book)
  return jsonify(books)

app.run(port=5000, host='localhost', debug=True)