from flask import Flask, render_template, jsonify, request
from src.helper import load_pdf, text_split
from src.response import generateResponse

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/get", methods=["GET", "POST"])
def chat():
    userQuery = request.form["msg"]  # User's question
    print(f'User query: {userQuery}')

    data = load_pdf("data/")
    text_chunks = text_split(data)
    result = generateResponse(text_chunks,userQuery)

    return result


if __name__ == '__main__':
    app.run(host="0.0.0.0", port= 8080, debug= True)



