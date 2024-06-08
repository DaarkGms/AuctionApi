from flask import Flask, request, jsonify
import firebase_admin
from firebase_admin import credentials, db

app = Flask(__name__)

# Initialize Firebase
cred = credentials.Certificate('leilao-b2276-firebase-adminsdk-z44fo-c68b4dff41.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://leilao-b2276-default-rtdb.firebaseio.com'
})

# Endpoint para cadastrar itens
@app.route('/items', methods=['POST'])
def create_item():
    data = request.json
    db.reference('items').push(data)
    return jsonify({'message': 'Item cadastrado com sucesso'})

# Endpoint para cadastrar compradores
@app.route('/buyers', methods=['POST'])
def create_buyer():
    data = request.json
    db.reference('buyers').push(data)
    return jsonify({'message': 'Comprador cadastrado com sucesso'})

# Endpoint para efetuar lance
@app.route('/items/<item_id>/bid', methods=['POST'])
def place_bid(item_id):
    data = request.json
    item_ref = db.reference('items').child(item_id)
    current_bid = item_ref.child('current_bid').get()
    if data['bid'] > current_bid:
        item_ref.update({'current_bid': data['bid']})
        return jsonify({'message': 'Lance efetuado com sucesso'})
    else:
        return jsonify({'error': 'O lance deve ser maior que o lance atual'})

# Endpoint para listar itens em leilão
@app.route('/items', methods=['GET'])
def list_items():
    items = db.reference('items').get()
    return jsonify(items)

if __name__ == '__main__':
    app.run(debug=True)
