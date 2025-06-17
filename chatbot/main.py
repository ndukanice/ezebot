
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
    if "hello" in message or "hi" in message:
        return "Wetin dey sup! How far? 😄"
    elif "name" in message:
        return "Dem call me EzeBot, built by the one and only Emmanuel N. Eze!"
    elif "how are you" in message:
        return "I'm chilled like Ice water—thanks for asking!"
    elif "what can you do" in message or "help" in message:
        return "I fit chat with you, answer small-small questions, and just keep you company!"
    elif "bye" in message:
        return "Alright now, make you no forget me o! ✌️"
    else:
        return "Hmm... I no too grab that one. Try me again?"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
