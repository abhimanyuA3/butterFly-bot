from flask import Flask, request, jsonify
from twilio.twiml.messaging_response import MessagingResponse
from database import orders_collection
from flask_cors import CORS
import config

from flask import Flask, jsonify
from pymongo import MongoClient

import config
print("Twilio SID:", config.TWILIO_ACCOUNT_SID)
print("Twilio Auth Token:", config.TWILIO_AUTH_TOKEN)
print("whatsapp Number:", config.TWILIO_WHATSAPP_NUMBER)


app = Flask(__name__)
CORS(app)

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017")  # Use "mongodb+srv://..." for MongoDB Atlas
db = client["VendorShop"]

@app.route("/test-db", methods=["GET"])
def test_db():
    try:
        db.list_collection_names()  # Check if the connection works
        return jsonify({"status": "Connected to MongoDB!"})
    except Exception as e:
        return jsonify({"status": "Failed to connect", "error": str(e)})

# Product list
products = {
    "1": "Books - 50/-",
    "2": "Pens - 20/-",
    "3": "Pencils - 5/-",
    "4": "Notebooks - 40/-"
}

@app.route("/whatsapp", methods=["POST"])
def whatsapp_bot():
    incoming_msg = request.form.get("Body").strip().lower()
    sender = request.form.get("From")
    response = MessagingResponse()
    message = response.message()

    if incoming_msg == "menu":
        product_list = "\n".join([f"{key}. {value}" for key, value in products.items()])
        message.body(f"Welcome to ButterFly Store!\n\nHere are the items:\n{product_list}\n\nReply with the product number to order.")
    elif incoming_msg in products:
        selected_item = products[incoming_msg]
        orders_collection.insert_one({"customer": sender, "item": selected_item})
        message.body(f"You've ordered: {selected_item}. Your order has been recorded.")
    else:
        message.body("Welcome to ButterFly Store! Reply with 'menu' to see the product list.")

    return str(response)

@app.route("/orders", methods=["GET"])
def get_orders():
    orders = list(orders_collection.find({}, {"_id": 0}))  # Exclude MongoDB's _id field
    return jsonify(orders)

@app.route("/add-test-order", methods=["GET"])
def add_test_order():
    db["orders"].insert_one({"customer": "Test User1", "item": "Sample Product1"})
    return jsonify({"status": "Order added"})


if __name__ == "__main__":
    app.run(port=5000, debug=True)

