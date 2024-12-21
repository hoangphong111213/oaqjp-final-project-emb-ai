import requests
import json

def emotion_detector(text_to_analyse):
    if text_to_analyse == "":
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock", "Content-Type": "application/json"}
    json = { "raw_document": { "text": text_to_analyse } }
    
    response = requests.post(url, headers=headers, json=json)
    response.raise_for_status()
    emotions = response.json()["emotionPredictions"][0]["emotion"]

    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']
    dominant_emotion = max(emotions.items(), key=lambda x: x[1])[0]

    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }