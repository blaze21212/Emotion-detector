"""Emotion detection implementation using the Watson NLP Emotion API."""

import json
from typing import Dict, Optional

import requests

from .utils import fallback_emotion_detector


EMOTION_KEYS = ('anger', 'disgust', 'fear', 'joy', 'sadness')


class EmotionDetector:
    """
    Main emotion detector class that interfaces with Watson NLP API
    with fallback to local keyword-based detection.
    """
    
    def __init__(self, api_url: Optional[str] = None, timeout: int = 5):
        """
        Initialize EmotionDetector
        
        Args:
            api_url: Watson API endpoint (optional)
            timeout: Request timeout in seconds
        """
        self.api_url = api_url or 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
        self.headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
        self.timeout = timeout
    
    def detect(self, text: str) -> Dict:
        """
        Detect emotions in the given text.
        
        Args:
            text: Text to analyze
            
        Returns:
            Dictionary containing anger, disgust, fear, joy, sadness, and
            dominant_emotion.
        """
        if not text or not text.strip():
            return self._empty_response()

        try:
            response_text = self._query_watson_api(text)
            response_data = json.loads(response_text)
            emotions = response_data['emotionPredictions'][0]['emotion']
        except (
            requests.exceptions.RequestException,
            json.JSONDecodeError,
            KeyError,
            IndexError,
            TypeError
        ):
            return fallback_emotion_detector(text)

        return self._format_response(emotions)

    def _query_watson_api(self, text: str) -> str:
        """Query Watson NLP API for emotion detection."""
        payload = {"raw_document": {"text": text}}
        
        response = requests.post(
            self.api_url,
            json=payload,
            headers=self.headers,
            timeout=self.timeout
        )

        response.raise_for_status()
        return response.text

    @staticmethod
    def _empty_response() -> Dict:
        """Return the required response format for empty input."""
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    @staticmethod
    def _format_response(emotions: Dict) -> Dict:
        """Extract scores and calculate the dominant emotion."""
        scores = {
            emotion: emotions.get(emotion, 0.0)
            for emotion in EMOTION_KEYS
        }
        dominant_emotion = max(scores, key=scores.get)
        scores['dominant_emotion'] = dominant_emotion
        return scores


def emotion_detector(text_to_analyse: str) -> Dict:
    """Return formatted emotion scores for the supplied text."""
    detector = EmotionDetector()
    return detector.detect(text_to_analyse)


def analyze_emotion(text: str) -> Dict:
    """
    Convenience function to analyze emotion in text.
    
    Args:
        text: Text to analyze
        
    Returns:
        Dictionary with emotion scores and the dominant emotion.
        
    Example:
        >>> from emotion_detector import analyze_emotion
        >>> result = analyze_emotion("I am very happy")
        >>> print(result['dominant_emotion'])
        'joy'
    """
    return emotion_detector(text)
