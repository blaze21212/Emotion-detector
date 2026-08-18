"""
Example usage of the emotion_detector package
"""

from emotion_detector import (
    analyze_emotion,
    EmotionDetector,
    validate_text,
    get_emotion_intensity
)


def example_1_simple_usage():
    """Example 1: Simple text analysis"""
    print("=" * 50)
    print("Example 1: Simple Text Analysis")
    print("=" * 50)
    
    result = analyze_emotion("I am very happy today!")
    print(f"Text: 'I am very happy today!'")
    print(f"Dominant Emotion: {result['dominant_emotion']}")
    print(f"Emotion Scores:")
    for emotion in ['anger', 'disgust', 'fear', 'joy', 'sadness']:
        score = result[emotion]
        intensity = get_emotion_intensity(score)
        print(f"  {emotion.capitalize()}: {score} ({intensity})")
    print()


def example_2_multiple_texts():
    """Example 2: Analyze multiple texts"""
    print("=" * 50)
    print("Example 2: Multiple Text Analysis")
    print("=" * 50)
    
    texts = [
        "I am so happy!",
        "This is terrible!",
        "I'm really scared",
        "This is disgusting",
        "I feel neutral about this"
    ]
    
    for text in texts:
        result = analyze_emotion(text)
        print(f"Text: '{text}'")
        print(f"Dominant Emotion: {result['dominant_emotion']}")
        print()


def example_3_class_usage():
    """Example 3: Using EmotionDetector class"""
    print("=" * 50)
    print("Example 3: EmotionDetector Class Usage")
    print("=" * 50)
    
    detector = EmotionDetector()
    
    text = "I absolutely love this amazing product!"
    result = detector.detect(text)
    
    print(f"Text: '{text}'")
    print(f"\nFull Result:")
    for key, value in result.items():
        print(f"  {key}: {value}")
    print()


def example_4_validation():
    """Example 4: Text validation"""
    print("=" * 50)
    print("Example 4: Text Validation")
    print("=" * 50)
    
    test_cases = [
        "Valid text here",
        "",
        "   ",
        None,
    ]
    
    for text in test_cases:
        is_valid = validate_text(text) if isinstance(text, str) else False
        print(f"Text: {repr(text)}")
        print(f"Valid: {is_valid}")
        print()


def example_5_batch_processing():
    """Example 5: Batch processing"""
    print("=" * 50)
    print("Example 5: Batch Processing")
    print("=" * 50)
    
    texts = [
        "This is wonderful!",
        "I hate this!",
        "I'm so scared!",
        "This is amazing!",
        "I'm sad today",
    ]
    
    detector = EmotionDetector()
    results = [detector.detect(text) for text in texts]
    
    # Analyze results
    emotion_counts = {}
    for result in results:
        emotion = result['dominant_emotion']
        emotion_counts[emotion] = emotion_counts.get(emotion, 0) + 1
    
    print("Emotion Distribution:")
    for emotion, count in emotion_counts.items():
        percentage = (count / len(results)) * 100
        print(f"  {emotion.capitalize()}: {count} ({percentage:.1f}%)")
    print()


def example_6_error_handling():
    """Example 6: Error handling"""
    print("=" * 50)
    print("Example 6: Error Handling")
    print("=" * 50)
    
    # Empty text
    result = analyze_emotion("")
    print(f"Empty text result: {result['dominant_emotion']}")
    
    # Valid text with fallback
    result = analyze_emotion("I am very angry!")
    print(f"Valid text result: {result['dominant_emotion']}")
    print()


if __name__ == "__main__":
    print("\n🎭 Emotion Detector Package - Examples\n")
    
    example_1_simple_usage()
    example_2_multiple_texts()
    example_3_class_usage()
    example_4_validation()
    example_5_batch_processing()
    example_6_error_handling()
    
    print("=" * 50)
    print("✅ All examples completed!")
    print("=" * 50)
