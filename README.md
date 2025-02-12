# butterFly-bot

This project is a WhatsApp bot for a small vendor shop that allows users to browse products, place orders, and view them in real-time on a web portal. The bot integrates with **Twilio** for WhatsApp messaging and uses **MongoDB** for storing orders. The frontend is built with **React** and the backend with **Flask**.

## Features
- **Product Listing**: Displays products available for purchase via WhatsApp.
- **Order Placement**: Allows customers to place orders.
- **Real-Time Orders**: Orders are stored in MongoDB and displayed in real-time on the React frontend.
- **Twilio Integration**: The bot connects with **Twilio** to send and receive WhatsApp messages.

## Tech Stack
- **Frontend**: React, Axios
- **Backend**: Flask, Twilio API, MongoDB
- **Database**: MongoDB (local or cloud)
- **WhatsApp API**: Twilio Sandbox for WhatsApp

## Prerequisites
- **Python 3.x**: Install [Python](https://www.python.org/downloads/)
- **Node.js**: Install [Node.js](https://nodejs.org/)
- **MongoDB**: Install [MongoDB](https://www.mongodb.com/try/download/community) (or use MongoDB Atlas)
- **Twilio Account**: Create an account on [Twilio](https://www.twilio.com/) and set up the WhatsApp Sandbox.

## Installation

### Backend Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/butterFly-bot.git
   cd butterFly-bot/backend
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate   # Windows
   source venv/bin/activate  # Mac/Linux
3. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
4. Run the backend server:
   ```bash
   python bot.py

### Frontend Setup
1. Navigate to the frontend directory:
   ```bash
   cd frontend
2. Install dependencies:
   ```bash
   npm install
3. Start the frontend server:
   ```bash
   npm start

### Running MongoDB
Start MongoDB locally (if using local setup):
  ```bash
mongod --dbpath C:\data\db
```
### Twilio Configuration
1. Set up Twilio WhatsApp Sandbox and get the Account SID, Auth Token, and WhatsApp-enabled Twilio number.
2. Update ```backend/config.py``` with your Twilio credentials.

## Usage
- After running the backend and frontend servers, open your WhatsApp and send "menu" to the Twilio WhatsApp number.
- You’ll receive a product list, and you can reply with a product number to place an order.
