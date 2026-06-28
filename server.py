"""
Servidor de analizis de emociones de texto
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

"""
Funcion para adquirir el texto del input en el html para poder ser analizado
"""

@app.route("/emotionDetector")
def emotion_detector_sv():
    """Recepción del codigo del input de html y respuesta del servidor"""
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    if response['Dominant Emotion'] is None:
        return "Invalid text! Please try again!."

    return (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, 'joy': {response['joy']} y 'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['Dominant Emotion']}."
    )


@app.route("/")
def home():

    """Retorna el template html de la pagina de inicio en el servidor"""
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
