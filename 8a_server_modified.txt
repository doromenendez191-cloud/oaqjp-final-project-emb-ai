"""
Servidor Flask para la aplicación de detección de emociones.
Incluye manejo de errores y está preparado para análisis estático con pylint.
"""

from flask import Flask, request
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector', methods=['GET'])
def detect_emotion():
    """
    Procesa el texto recibido por parámetro GET y devuelve
    el análisis emocional formateado. Maneja entradas en blanco.
    """
    text_to_analyze = request.args.get('text')

    if not text_to_analyze:
        return "¡Texto no válido! ¡Por favor, inténtelo de nuevo!"

    result = emotion_detector(text_to_analyze)

    if result['dominant_emotion'] is None:
        return "¡Texto no válido! ¡Por favor, inténtelo de nuevo!"

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
    """
    Punto de entrada principal del servidor Flask.
    Ejecuta la aplicación en localhost:5000.
    """
    app.run(host='0.0.0.0', port=5000)
