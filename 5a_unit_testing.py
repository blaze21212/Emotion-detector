#!/usr/bin/env python
"""
Task 5: Unit Testing for Emotion Detector
File: 5a_unit_testing.py

This module demonstrates unit tests for the emotion_detector package.
Tests cover all 5 emotion categories: joy, anger, disgust, sadness, and fear.
"""

import unittest
from emotion_detection import format_emotion_response


class TestEmotionDetector(unittest.TestCase):
    """Unit tests for emotion detection functionality"""
    
    def test_joy_emotion(self):
        """Test detection of joy emotion"""
        result = format_emotion_response("I am glad this happened")
        self.assertEqual(result['dominant_emotion'], 'joy')
    
    def test_anger_emotion(self):
        """Test detection of anger emotion"""
        result = format_emotion_response("I am really mad about this")
        self.assertEqual(result['dominant_emotion'], 'anger')
    
    def test_disgust_emotion(self):
        """Test detection of disgust emotion"""
        result = format_emotion_response("I feel disgusted just hearing about this")
        self.assertEqual(result['dominant_emotion'], 'disgust')
    
    def test_sadness_emotion(self):
        """Test detection of sadness emotion"""
        result = format_emotion_response("I am so sad about this")
        self.assertEqual(result['dominant_emotion'], 'sadness')
    
    def test_fear_emotion(self):
        """Test detection of fear emotion"""
        result = format_emotion_response("I am really afraid that this will happen")
        self.assertEqual(result['dominant_emotion'], 'fear')


class TestResponseFormat(unittest.TestCase):
    """Unit tests for response format and structure"""
    
    def test_response_has_all_emotions(self):
        """Test that response contains all 5 emotions"""
        result = format_emotion_response("Test text")
        required_emotions = ['anger', 'disgust', 'fear', 'joy', 'sadness']
        for emotion in required_emotions:
            self.assertIn(emotion, result)
    
    def test_response_has_dominant_emotion(self):
        """Test that response contains dominant_emotion key"""
        result = format_emotion_response("Test text")
        self.assertIn('dominant_emotion', result)
    
    def test_emotion_scores_are_numeric(self):
        """Test that emotion scores are numeric values"""
        result = format_emotion_response("I am happy")
        self.assertIsInstance(result['joy'], (int, float))
        self.assertIsInstance(result['anger'], (int, float))
        self.assertIsInstance(result['disgust'], (int, float))
        self.assertIsInstance(result['fear'], (int, float))
        self.assertIsInstance(result['sadness'], (int, float))
    
    def test_emotion_scores_in_valid_range(self):
        """Test that emotion scores are between 0.0 and 1.0"""
        result = format_emotion_response("I am very happy today!")
        for emotion in ['anger', 'disgust', 'fear', 'joy', 'sadness']:
            score = result[emotion]
            self.assertGreaterEqual(score, 0.0, f"{emotion} score below 0.0")
            self.assertLessEqual(score, 1.0, f"{emotion} score above 1.0")
    
    def test_dominant_emotion_is_string(self):
        """Test that dominant_emotion is a string"""
        result = format_emotion_response("Test text")
        self.assertIsInstance(result['dominant_emotion'], str)


class TestEdgeCases(unittest.TestCase):
    """Unit tests for edge cases and error handling"""
    
    def test_empty_text_returns_none_values(self):
        """Test that empty text returns None values"""
        result = format_emotion_response("")
        self.assertIsNone(result['dominant_emotion'])
        self.assertIsNone(result['joy'])
    
    def test_whitespace_only_returns_none_values(self):
        """Test that whitespace-only text returns None values"""
        result = format_emotion_response("   ")
        self.assertIsNone(result['dominant_emotion'])
    
    def test_neutral_text_returns_valid_result(self):
        """Test that neutral text returns a valid result"""
        result = format_emotion_response("The weather is nice")
        self.assertIsNotNone(result['dominant_emotion'])
        # Neutral text should return one of the emotions or neutral
        valid_emotions = ['anger', 'disgust', 'fear', 'joy', 'sadness', 'neutral']
        self.assertIn(result['dominant_emotion'], valid_emotions)
    
    def test_long_text_is_processed(self):
        """Test that long text is properly processed"""
        long_text = "I am very happy! " * 50
        result = format_emotion_response(long_text)
        self.assertEqual(result['dominant_emotion'], 'joy')
    
    def test_special_characters_handled(self):
        """Test that special characters are handled"""
        result = format_emotion_response("I'm so @#$% angry!!!")
        self.assertIsNotNone(result['dominant_emotion'])


class TestMultipleDetections(unittest.TestCase):
    """Unit tests for consistency across multiple detections"""
    
    def test_same_text_consistent_results(self):
        """Test that same text produces consistent results"""
        text = "I am very happy"
        result1 = format_emotion_response(text)
        result2 = format_emotion_response(text)
        
        self.assertEqual(result1['dominant_emotion'], result2['dominant_emotion'])
        self.assertEqual(result1['joy'], result2['joy'])
    
    def test_case_insensitivity(self):
        """Test that detection is case-insensitive"""
        result_lower = format_emotion_response("i am happy")
        result_upper = format_emotion_response("I AM HAPPY")
        result_mixed = format_emotion_response("I aM hApPy")
        
        # All should detect joy as dominant emotion
        self.assertEqual(result_lower['dominant_emotion'], 'joy')
        self.assertEqual(result_upper['dominant_emotion'], 'joy')
        self.assertEqual(result_mixed['dominant_emotion'], 'joy')


if __name__ == '__main__':
    # Run all tests with verbose output
    unittest.main(verbosity=2)
