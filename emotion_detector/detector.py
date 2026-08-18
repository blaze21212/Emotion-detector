"""
Emotion Detection Module
Detects emotions from text using Watson NLP API with local fallback
"""

import json
import requests
from typing import Dict, Optional
from .utils import fallback_emotion_detector


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
            Dictionary with emotion scores and dominant emotion:
            {
                'anger': float,
                'disgust': float,
                'fear': float,
                'joy': float,
                'sadness': float,
                'dominant_emotion': str
            }
        """
        # Check for empty or blank input
        if not text or not text.strip():
            return self._empty_response()
        
        # Try Watson API first
        try:
            return self._query_watson_api(text)
        except Exception as e:
            print(f"Watson API unavailable ({str(e)}), using fallback detector")
            return fallback_emotion_detector(text)
    
    def _query_watson_api(self, text: str) -> Dict:
        """Query Watson NLP API for emotion detection"""
        payload = {"raw_document": {"text": text}}
        
        response = requests.post(
            self.api_url,
            json=payload,
            headers=self.headers,
            timeout=self.timeout
        )
        
        # Handle error responses
        if response.status_code in [400, 500]:
            return fallback_emotion_detector(text)
        
        # Parse response
        formatted_response = json.loads(response.text)
        emotions = formatted_response['emotionPredictions'][0]['emotion']
        
        # Find dominant emotion
        dominant_emotion = max(emotions, key=emotions.get)
        
        return {
            'anger': emotions.get('anger', 0.0),
            'disgust': emotions.get('disgust', 0.0),
            'fear': emotions.get('fear', 0.0),
            'joy': emotions.get('joy', 0.0),
            'sadness': emotions.get('sadness', 0.0),
            'dominant_emotion': dominant_emotion
        }
    
    @staticmethod
    def _empty_response() -> Dict:
        """Return empty response for empty input"""
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }


# Module-level convenience function
def analyze_emotion(text: str) -> Dict:
    """
    Convenience function to analyze emotion in text.
    
    Args:
        text: Text to analyze
        
    Returns:
        Dictionary with emotion scores and dominant emotion
        
    Example:
        >>> from emotion_detector import analyze_emotion
        >>> result = analyze_emotion("I am very happy")
        >>> print(result['dominant_emotion'])
        'joy'
    """
    detector = EmotionDetector()
    return detector.detect(text)
