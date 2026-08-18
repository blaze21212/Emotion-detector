"""
Emotion Detector Package
A Python package for detecting emotions in text using Watson NLP API with fallback to local detection.
"""

from .detector import EmotionDetector, analyze_emotion
from .utils import fallback_emotion_detector, validate_text, get_emotion_intensity

__version__ = "1.0.0"
__author__ = "Your Name"
__description__ = "Emotion detection library using IBM Watson NLP API"

__all__ = [
    "EmotionDetector",
    "analyze_emotion",
    "fallback_emotion_detector",
    "validate_text",
    "get_emotion_intensity"
]

