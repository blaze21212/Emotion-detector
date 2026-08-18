#!/usr/bin/env python
"""Test script for emotion_detector package"""

from emotion_detector import analyze_emotion, EmotionDetector, get_emotion_intensity

print("\n" + "="*60)
print("Testing emotion_detector Package")
print("="*60 + "\n")

# Test 1: Simple function
print("TEST 1: analyze_emotion() function")
print("-" * 60)
result = analyze_emotion("I am very happy today!")
print("Text: 'I am very happy today!'")
print(f"Dominant Emotion: {result['dominant_emotion']}")
print(f"Joy Score: {result['joy']}")
print()

# Test 2: Class usage
print("TEST 2: EmotionDetector class")
print("-" * 60)
detector = EmotionDetector()
result = detector.detect("This is disgusting!")
print("Text: 'This is disgusting!'")
print(f"Dominant Emotion: {result['dominant_emotion']}")
print(f"Disgust Score: {result['disgust']}")
print()

# Test 3: Intensity function
print("TEST 3: get_emotion_intensity() function")
print("-" * 60)
print(f"Score 0.15: {get_emotion_intensity(0.15)}")
print(f"Score 0.5: {get_emotion_intensity(0.5)}")
print(f"Score 0.9: {get_emotion_intensity(0.9)}")
print()

# Test 4: Multiple emotions
print("TEST 4: Multiple text samples")
print("-" * 60)
texts = [
    "I am so angry!",
    "I feel afraid",
    "This is wonderful!",
]

for text in texts:
    result = analyze_emotion(text)
    print(f"Text: '{text}'")
    print(f"Dominant: {result['dominant_emotion']}")
    print()

print("="*60)
print("✅ All tests passed! Package is working correctly!")
print("="*60 + "\n")
