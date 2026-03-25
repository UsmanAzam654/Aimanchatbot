from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Load your romantic data
with open("data.txt", "r", encoding="utf-8") as f:
    knowledge = f.readlines()

def get_response(user_input):
    user_input = user_input.lower()
    for line in knowledge:
        if any(word in line.lower() for word in user_input.split()):
            return line.strip()
    return "This is something only we know ❤️"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chatbot():
    msg = request.form["msg"]
    reply = get_response(msg)
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)