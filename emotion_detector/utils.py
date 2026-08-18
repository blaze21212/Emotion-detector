"""
Utility functions for emotion detection
"""

from typing import Dict


def fallback_emotion_detector(text: str) -> Dict:
    """
    Fallback local emotion detection using keyword matching.
    Used when Watson API is unavailable.
    
    Args:
        text: Text to analyze
        
    Returns:
        Dictionary with emotion scores and dominant emotion
    """
    text_lower = text.lower()
    
    # Define keywords for each emotion
    emotions_keywords = {
        'anger': ['angry', 'mad', 'furious', 'hate', 'upset', 'aggravate', 'irritate', 'rage', 'enraged'],
        'disgust': ['disgust', 'gross', 'yuck', 'ew', 'vomit', 'sick', 'repugnant', 'revolting'],
        'fear': ['afraid', 'scared', 'fear', 'terrified', 'horror', 'panic', 'anxious', 'nervous', 'dread'],
        'joy': ['happy', 'glad', 'joy', 'cheerful', 'delight', 'love', 'wonderful', 'amazing', 'great', 'awesome', 'excellent', 'excited', 'thrilled'],
        'sadness': ['sad', 'unhappy', 'depressed', 'grief', 'sorrow', 'miserable', 'upset', 'lonely', 'heartbroken']
    }
    
    # Count keyword matches for each emotion
    scores = {}
    for emotion, keywords in emotions_keywords.items():
        score = sum(1 for keyword in keywords if keyword in text_lower)
        scores[emotion] = round(score * 0.15, 2) if score > 0 else 0.0
    
    # Normalize scores to max 1.0
    max_score = max(scores.values()) if scores.values() else 0
    if max_score > 1.0:
        scores = {k: round(v / max_score, 2) for k, v in scores.items()}
    
    # Find dominant emotion (or return first if all are 0)
    dominant = max(scores, key=scores.get) if max(scores.values()) > 0 else 'neutral'
    
    return {
        'anger': scores['anger'],
        'disgust': scores['disgust'],
        'fear': scores['fear'],
        'joy': scores['joy'],
        'sadness': scores['sadness'],
        'dominant_emotion': dominant
    }


def validate_text(text: str) -> bool:
    """
    Validate if text is suitable for emotion analysis.
    
    Args:
        text: Text to validate
        
    Returns:
        True if text is valid, False otherwise
    """
    if not text or not isinstance(text, str):
        return False
    return len(text.strip()) > 0


def get_emotion_intensity(score: float) -> str:
    """
    Get human-readable intensity level based on emotion score.
    
    Args:
        score: Emotion score (0.0 to 1.0)
        
    Returns:
        Intensity level as string
    """
    if score is None:
        return "N/A"
    elif score < 0.2:
        return "Very Low"
    elif score < 0.4:
        return "Low"
    elif score < 0.6:
        return "Medium"
    elif score < 0.8:
        return "High"
    else:
        return "Very High"
