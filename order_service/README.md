# Order Service

A Flask-based HTTP service for the **Video Game Retail Store** project (CYBI 3345). This service allows customers to place and track
video game orders through a REST API with an interactive HTML interface.

## Features

- Place new orders via HTTP POST
- View all orders as JSON via HTTP GET
- Interactive HTML interface with game cover images
- In-memory storage (no database required)

## Requirements

- Python 3.x
- Flask

## Installation

```bash```
sudo apt install python3-flash -y

## Running

python3 app.py

## Endpoints
METHOD | ENDPOINT | DESCRIPTION
 GET   | /        | HTML page showing all orders
 GET   | /orders  | Returns all orders as JSON
 POST  | /orders  | Creates a new order

## Usage

1. View HTML interface

Open in browser
http://<service-ip>5002 -> http://192.168.64.2:5002

2. Get all orders
curl http://localhost:5002/orders

3. Create an order
curl -X POST http://localhost:5002/orders \
-H "Content-Type: application/json" \
-d '{"game":"Minecraft","quantity":1}'

## Project Structure
order_service/
|-app.py			# Flask application
|-README.md			# This file
|-templates/
  |-index.html			#HTML interface
|-static/
  |-images/			# Game cover images
   |-minecraft.jpeg
   |-marioKart8Deluxe.jpeg
   |-GodofWar.png

## Author

CYBI 3345 - Team 1
