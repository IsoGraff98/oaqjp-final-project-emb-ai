"""
Pruebas de función emotion_detector
"""
import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    """Clase de pruebas para validar la detección de emociones."""
    def test_emotion_detector(self):
        """Prueba que el detector reconozca correctamente cada emoción."""
        # Caso de prueba para sentimiento positivo (Alegría)
        result_1 = emotion_detector('I am glad this happened')
        self.assertEqual(result_1['Dominant Emotion'], 'joy')

        # Caso de prueba para sentimiento de enojo (Ira)
        result_2 = emotion_detector('I am really mad about this')
        self.assertEqual(result_2['Dominant Emotion'], 'anger')

        # Caso de prueba para sentimiento disgusto (Asco)
        result_3 = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(result_3['Dominant Emotion'], 'disgust')

        # Caso de prueba para sentimiento triste (Tristeza)
        result_4 = emotion_detector('I am so sad about this')
        self.assertEqual(result_4['Dominant Emotion'], 'sadness')

        # Caso de prueba para sentimiento asustado (Miedo)
        result_5 = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(result_5['Dominant Emotion'], 'fear')

if __name__ == '__main__':
    unittest.main()
    