
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_msg = data.get("message", "")
    response = get_bot_response(user_msg)
    return jsonify({"response": response})

def get_bot_response(message):
    message = message.lower()
    if "hello" in message:
        return "Hi there! How can I assist you today?"
    elif "name" in message:
        return "I'm a friendly little chatbot built by Eze."
    elif "bye" in message:
        return "Goodbye! Talk soon."
    else:
        return "Sorry, I didn't understand that."

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_msg = data.get("message", "")
    response = get_bot_response(user_msg)
    return jsonify({"response": response})

def get_bot_response(message):
    message = message.lower()
    if "hello" in message:
        return "Hi there! How can I assist you today?"
    elif "name" in message:
        return "I'm a friendly little chatbot built by Eze."
    elif "bye" in message:
        return "Goodbye! Talk soon."
    else:
        return "Sorry, I didn't understand that."

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_msg = data.get("message", "")
    response = get_bot_response(user_msg)
    return jsonify({"response": response})

def get_bot_response(message):
    message = message.lower()
    if "hello" in message:
        return "Hi there! How can I assist you today?"
    elif "name" in message:
        return "I'm a friendly little chatbot built by Eze."
    elif "bye" in message:
        return "Goodbye! Talk soon."
    else:
        return "Sorry, I didn't understand that."

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

