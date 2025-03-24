from flask import Flask, jsonify, request

app = Flask(__name__)

# Initialize questions dictionary
questions = {
    "Question1": "Question1",
    "Question2": "Question2",
    "Question3": "Question3",
    "Steps" : 2,
    "Voice" : "Voice"
}


@app.route("/Fambot", methods=['GET', 'POST'])
def handle_questions():
    if request.method == 'GET':
        return jsonify(questions)
    elif request.method == 'POST':
        data = request.get_json()

        # Update existing questions with new values
        for key in data:
            if key in questions:
                questions[key] = data[key]

        return jsonify(questions), 200


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8888)
