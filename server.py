from flask import Flask, request
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector', methods=['GET'])
def detect_emotion():
    text_to_analyze = request.args.get('text')

    if not text_to_analyze:
        return "Error: No text provided", 400

    result = emotion_detector(text_to_analyze)

    response = (
        f"Para la declaración dada, la respuesta del sistema es "
        f"'ira': {result['anger']}, "
        f"'asco': {result['disgust']}, "
        f"'miedo': {result['fear']}, "
        f"'alegría': {result['joy']}, "
        f"'tristeza': {result['sadness']}. "
        f"La emoción dominante es {result['dominant_emotion']}."
    )

    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)