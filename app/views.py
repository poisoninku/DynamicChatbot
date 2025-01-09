from flask import Flask, render_template, request
import chatbot

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.form["message"]
    user_id = 1  # This could be dynamic, based on logged-in user
    personality = request.form.get("personality", "friendly")  # Get personality choice from the form

    # Get response based on personality and user input
    response = chatbot.get_response(user_message, personality)

    # Store the conversation in the database
    chatbot.store_message(user_id, user_message, response)

    return render_template("chat.html", user_message=user_message, bot_response=response)

if __name__ == "__main__":
    app.run(debug=True)
