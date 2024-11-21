from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import T5Tokenizer, T5ForConditionalGeneration

app = Flask(__name__)
CORS(app)


model_path = ".\\20batch"
tokenizer = T5Tokenizer.from_pretrained(model_path)
model = T5ForConditionalGeneration.from_pretrained(model_path)

@app.route("/summarize", methods=["POST"])
def summarize():
    data = request.get_json()


    if "text" not in data:
        return jsonify({"error": "Missing text input"}), 400


    text = data["text"]
    mode = data["mode"]
    lengths = {
    'short': (30, 200),
    'medium': (40, 300),
    'long': (50, 500)
    }
    min_lengths, max_lengths = lengths.get(mode, (None, None))
    inputs = tokenizer.encode("summarize: " + text, return_tensors="pt", max_length=512, truncation=True)


    summary_ids = model.generate(inputs, max_length=max_lengths, min_length=min_lengths, length_penalty=2.0, num_beams=4, early_stopping=True)
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)


    return jsonify({"summary": summary})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)