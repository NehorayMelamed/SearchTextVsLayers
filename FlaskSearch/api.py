from flask import Flask, request, jsonify
import json
from rank_bm25 import BM25Okapi
from fuzzywuzzy import fuzz
import unicodedata

app = Flask(__name__)

JSON_PATH = "9900_layers.json"

def normalize_text(text):
    return ''.join(c for c in unicodedata.normalize('NFD', text) if unicodedata.category(c) != 'Mn')


def find_most_similar(input_sentence, tokenized_corpus, bm25):
    tokenized_query = input_sentence.split(" ")
    scores = bm25.get_scores(tokenized_query)

    most_similar_index = -1
    max_similarity = 0
    for idx, score in enumerate(scores):
        similarity = fuzz.ratio(input_sentence, ' '.join(tokenized_corpus[idx]))
        if similarity > max_similarity:
            max_similarity = similarity
            most_similar_index = idx

    return most_similar_index, max_similarity


def search_in_json(input_sentence, threshold=70):
    with open(JSON_PATH, 'r') as f:
        data = json.load(f)

    names = [normalize_text(name) for name in data['names']]
    rows = data['rows']

    tokenized_corpus = [name.split(" ") for name in names]
    bm25 = BM25Okapi(tokenized_corpus)

    normalized_input = normalize_text(input_sentence)
    idx, similarity_score = find_most_similar(normalized_input, tokenized_corpus, bm25)

    if idx != -1 and similarity_score >= threshold:
        geometry_data = rows[idx].get("geometry", None)
        layer_id = rows[idx].get("id", None)
        return {
            'name': data['names'][idx],
            'geometry': geometry_data,
            'layer_id': layer_id
        }
    else:
        return {"error": "No similar name found above the threshold."}


@app.route('/search', methods=['POST'])
def search():
    try:
        data = request.json
        input_sentence = data.get('sentence', '')

        if not input_sentence:
            return jsonify({"error": 400, "data": "Missing input sentence"}), 400

        result = search_in_json(input_sentence)  # Assuming this is your existing function

        if result.get("error"):
            return jsonify({"error": 404, "data": "No similar name found above the threshold."}), 404

        return jsonify({"success": 200, "data": result}), 200

    except Exception as e:
        return jsonify({"error": 500, "data": str(e)}), 500


@app.route('/is_service_alive', methods=['GET'])
def is_service_alive():
    try:
        # You can add more logic here if needed
        return jsonify({"success": 200, "data": "Service is alive"}), 200

    except Exception as e:
        return jsonify({"error": 500, "data": str(e)}), 500


@app.errorhandler(500)
def handle_500_error(_):
    """Handle 500 server errors."""
    return jsonify({"error": "Internal server error occurred"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)


