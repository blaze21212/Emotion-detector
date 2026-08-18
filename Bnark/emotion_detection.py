import json
import requests

def fallback_emotion_detector(text_to_analyze):
    """
    Fallback local emotion detection using keyword matching.
    Used when Watson API is unavailable.
    """
    text_lower = text_to_analyze.lower()
    
    # Define keywords for each emotion
    emotions = {
        'anger': ['angry', 'mad', 'furious', 'hate', 'upset', 'angry', 'aggravate', 'irritate', 'rage'],
        'disgust': ['disgust', 'gross', 'yuck', 'ew', 'gross', 'vomit', 'sick', 'repugnant'],
        'fear': ['afraid', 'scared', 'fear', 'terrified', 'horror', 'panic', 'anxious', 'nervous'],
        'joy': ['happy', 'glad', 'joy', 'cheerful', 'delight', 'love', 'wonderful', 'amazing', 'great', 'awesome', 'excellent', 'excited'],
        'sadness': ['sad', 'unhappy', 'depressed', 'grief', 'sorrow', 'miserable', 'upset', 'lonely']
    }
    
    # Count keyword matches for each emotion
    scores = {}
    for emotion, keywords in emotions.items():
        score = sum(1 for keyword in keywords if keyword in text_lower)
        scores[emotion] = round(score * 0.15, 2) if score > 0 else 0.0
    
    # Normalize scores to max 1.0
    max_score = max(scores.values()) if scores.values() else 0
    if max_score > 1.0:
        scores = {k: round(v / max_score, 2) for k, v in scores.items()}
    
    # Find dominant emotion
    dominant = max(scores, key=scores.get)
    
    return {
        'anger': scores['anger'],
        'disgust': scores['disgust'],
        'fear': scores['fear'],
        'joy': scores['joy'],
        'sadness': scores['sadness'],
        'dominant_emotion': dominant
    }

def emotion_detector(text_to_analyze):
    """
    Sends text to the Watson NLP Emotion Predict API and returns
    individual emotion scores alongside the dominant emotion.
    Falls back to local detection if API is unavailable.
    """
    # Check for empty or blank input
    if not text_to_analyze or not text_to_analyze.strip():
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    # Watson NLP Emotion Predict Endpoint
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = {"raw_document": {"text": text_to_analyze}}

    try:
        response = requests.post(url, json=payload, headers=headers, timeout=5)
        
        # Handle non-200 responses
        if response.status_code == 400 or response.status_code == 500:
            # Use fallback detector
            return fallback_emotion_detector(text_to_analyze)

        formatted_response = json.loads(response.text)
        
        # Extract emotions dictionary
        emotions = formatted_response['emotionPredictions'][0]['emotion']
        
        # Determine dominant emotion
        dominant_emotion = max(emotions, key=emotions.get)
        
        return {
            'anger': emotions.get('anger', 0.0),
            'disgust': emotions.get('disgust', 0.0),
            'fear': emotions.get('fear', 0.0),
            'joy': emotions.get('joy', 0.0),
            'sadness': emotions.get('sadness', 0.0),
            'dominant_emotion': dominant_emotion
        }

    except (requests.exceptions.RequestException, json.JSONDecodeError, KeyError, IndexError):
        # If API fails for any reason, use fallback
        return fallback_emotion_detector(text_to_analyze)