import json
from watson_nlp import EmotionPredictor

def emotion_detector(text):
    model = EmotionPredictor.from_pretrained("emotion_aggregated-workflow_lang_en_stock")
    prediction = model.predict(text)
    emotions = prediction.get_emotions()
    dominant_emotion = max(emotions, key=emotions.get)
    return {
        "anger": emotions.get("anger"),
        "disgust": emotions.get("disgust"),
        "fear": emotions.get("fear"),
        "joy": emotions.get("joy"),
        "sadness": emotions.get("sadness"),
        "dominant_emotion": dominant_emotion
    }
