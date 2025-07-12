from flask import Flask, render_template, request, jsonify
from markov_generator import load_text, build_markov_chain, generate_text

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    text = request.form.get("text")
    length = int(request.form.get("length", 50))

    if not text:
        return jsonify({"error": "Input text is empty."}), 400

    clean_text = load_text(text)
    chain = build_markov_chain(clean_text)
    result = generate_text(chain, length)

    return jsonify({"generated": result})

if __name__ == "__main__":
    app.run(debug=True)
