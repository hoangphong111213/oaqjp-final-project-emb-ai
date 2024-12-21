"""
Flask server application that processes emotion analysis from text input.
This module handles the '/emotionDetector' route and integrates with an emotion detection API.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector', methods=['GET'])
def detect_emotion():
    """
    Handles the '/emotionDetector' route, processes the input statement, 
    and returns the emotion analysis or an error message.

    Parameters:
        None
    
    Returns:
        json: A JSON response containing emotion analysis or an error message.
    """
    # Retrieve and clean the input statement
    statement = request.args.get("textToAnalyze", "").strip()

    # Call the emotion_detector function to analyze the emotion of the statement
    result = emotion_detector(statement)

    # If the dominant emotion is None, return an error message
    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    # Prepare the response with the emotion analysis
    response = (
        f"For the given statement, the system response is 'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, 'fear': {result['fear']}, 'joy': {result['joy']} "
        f"and 'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion']}."
    )
    return response

@app.route("/")
def render_index_page():
    """
    Renders the index page of the application.

    Returns:
        html: The rendered HTML page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    