from flask import Flask, jsonify, request

app = Flask(__name__)
orders = []

@app.route('/')
def home():
	return "<h1>Order Service</h1><p>Place and track orders.</p>"

@app.route('/orders', methods=['GET'])
def get_orders():
	return jsonify(orders)

@app.route('/orders', methods=['POST'])
def create_order():
	data = request.get_json()
	order = {
		"id": len(orders) + 1,
		"game": data.get("game"),
		"quantity": data.get("quantity", 1),
		"status": "pending"
	}
	orders.append(order)
	return jsonify(order), 201

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5002)
