"""
Flask server application that processes emotion analysis from text input.
This module handles the '/emotionDetector' route and integrates with an emotion detection API.
"""

from flask import Flask, request, jsonify
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
    statement = request.args.get("statement", "").strip()

    # If the statement is blank, return an error message
    if not statement:
        return jsonify({"message": "Invalid text! Please try again!"}), 400

    # Call the emotion_detector function to analyze the emotion of the statement
    result = emotion_detector(statement)

    # If the dominant emotion is None, return an error message
    if result['dominant_emotion'] is None:
        return jsonify({"message": "Invalid text! Please try again!"}), 400

    # Prepare the response with the emotion analysis
    response = (
        f"For the given statement, the system response is 'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, 'fear': {result['fear']}, 'joy': {result['joy']} "
        f"and 'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion']}."
    )
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=5000)
