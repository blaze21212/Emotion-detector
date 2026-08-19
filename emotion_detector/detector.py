"""
Emotion Detection Module
Detects emotions from text using Watson NLP API with local fallback
"""

import requests
from typing import Dict, Optional, Union
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
    
    def detect(self, text: str) -> Union[Dict, str]:
        """
        Detect emotions in the given text.
        
        Args:
            text: Text to analyze
            
        Returns:
            Raw Watson API response text for valid input, or a fallback
            dictionary if the request cannot be completed.
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
    
    def _query_watson_api(self, text: str) -> str:
        """Query Watson NLP API for emotion detection."""
        payload = {"raw_document": {"text": text}}
        
        response = requests.post(
            self.api_url,
            json=payload,
            headers=self.headers,
            timeout=self.timeout
        )
        
        return response.text
    
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
def analyze_emotion(text: str) -> Union[Dict, str]:
    """
    Convenience function to analyze emotion in text.
    
    Args:
        text: Text to analyze
        
    Returns:
        Raw Watson API response text for valid input, or a fallback dictionary
        if the request cannot be completed.
        
    Example:
        >>> from emotion_detector import analyze_emotion
        >>> result = analyze_emotion("I am very happy")
        >>> print(result['dominant_emotion'])
        'joy'
    """
    detector = EmotionDetector()
    return detector.detect(text)
