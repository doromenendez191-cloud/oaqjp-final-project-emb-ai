import unittest
from EmotionDetection import emotion_detector

class TestEmotionDetection(unittest.TestCase):

    def test_joy(self):
        result = emotion_detector("Me alegro de que esto haya sucedido.")
        self.assertEqual(result['dominant_emotion'], 'joy')

    def test_anger(self):
        result = emotion_detector("Estoy realmente enfadado por esto.")
        self.assertEqual(result['dominant_emotion'], 'anger')

    def test_disgust(self):
        result = emotion_detector("Me da asco solo de oír hablar de esto.")
        self.assertEqual(result['dominant_emotion'], 'disgust')

    def test_sadness(self):
        result = emotion_detector("Estoy muy triste por esto.")
        self.assertEqual(result['dominant_emotion'], 'sadness')

    def test_fear(self):
        result = emotion_detector("Tengo mucho miedo de que esto suceda.")
        self.assertEqual(result['dominant_emotion'], 'fear')

if __name__ == '__main__':
    unittest.main()
