from flask import Flask, jsonify, request, render_template

app = Flask(__name__)
orders = [
	{"id:": 1, "game": "Minecraft", "quantity": 2, "status": "pending", "cover": "/static/images/minecraft.jpeg"},
	{"id:": 2, "game": "Mario 8 Deluxe", "quantity": 1, "status": "shipped", "cover": "/static/images/marioKart8Deluxe.jpeg"},
	{"id:": 3, "game": "God of War Ragnarok", "quantity": 3, "status": "delivered", "cover": "/static/images/GodofWar.png"},
	{"id:": 4, "game": "The Legend of Zelda: Tears of the Kingdom", "quantity": 0, "status": "Unavailable/Out of Stock"},
	 ]

@app.route('/')
def home():
	"""Render the HTML interface for browsing orders."""
	return render_template('index.html', orders=orders)

@app.route('/orders', methods=['GET'])
def get_orders():
	"""Return all orders as JSON"""
	return jsonify(orders)

@app.route('/orders', methods=['POST'])
def create_order():
	"""Create a new order from JSON payload."""
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
