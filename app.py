# app.py

from flask import Flask, jsonify, request

app = Flask(__name__)

# Mock product data
data = [
    {"id": 1, "name": "Laptop", "price": 899.99, "category": "electronics"},
    {"id": 2, "name": "Book", "price": 14.99, "category": "books"},
    {"id": 3, "name": "Desk", "price": 199.99, "category": "furniture"},
]

@app.route("/")
def index():
    return jsonify({"message": "Welcome to the product API", "resource_endpoint": "/products"}), 200

# TODO: Implement GET /products to return all products or filter by category
@app.route("/products", methods=["GET"])
def get_products():
    category = request.args.get("category")
    if category:
        filtered = [item for item in data if item["category"] == category]
        return jsonify(filtered), 200
    return jsonify(data), 200

# TODO: Implement GET /products/<id> to return a single product by ID
@app.route("/products/<int:id>", methods=["GET"])
def get_products_by_id(id):
    for product in data:
        if product["id"] == id:
            return jsonify(product), 200
    return jsonify({"message": "Product not found"}), 404


if __name__ == "__main__":
    app.run(port=5555, debug=True)
