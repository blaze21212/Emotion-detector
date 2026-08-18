# Emotion Detector Package

A Python package for detecting emotions in text using IBM Watson NLP API with intelligent fallback to local keyword-based detection.

## Features

- 🤖 **IBM Watson NLP Integration**: Uses Watson's advanced NLP models when available
- 🔄 **Fallback Detection**: Automatically falls back to keyword-based detection if API is unavailable
- 📦 **Easy to Install**: Install via pip from local directory
- 🎯 **5 Emotion Categories**: Detects anger, disgust, fear, joy, and sadness
- 🔌 **Simple API**: Easy-to-use Python interface
- 🧪 **Well-documented**: Full docstrings and type hints

## Installation

### From Local Directory

```bash
cd emotion_detector
pip install -e .
```

### From GitHub (future)

```bash
pip install emotion-detector
```

### Development Installation

```bash
pip install -e ".[dev]"
```

## Quick Start

### Basic Usage

```python
from emotion_detector import analyze_emotion

# Analyze text
result = analyze_emotion("I am very happy today!")

print(result)
# Output:
# {
#     'anger': 0.0,
#     'disgust': 0.0,
#     'fear': 0.0,
#     'joy': 0.15,
#     'sadness': 0.0,
#     'dominant_emotion': 'joy'
# }
```

### Using the EmotionDetector Class

```python
from emotion_detector import EmotionDetector

# Create detector instance
detector = EmotionDetector()

# Analyze emotion
result = detector.detect("This is disgusting!")
print(f"Dominant emotion: {result['dominant_emotion']}")
print(f"Disgust score: {result['disgust']}")
```

### Custom API Configuration

```python
from emotion_detector import EmotionDetector

# Use custom API endpoint and timeout
detector = EmotionDetector(
    api_url="https://custom-api.example.com/emotion",
    timeout=10
)

result = detector.detect("Some text to analyze")
```

## API Reference

### analyze_emotion(text: str) -> Dict

Convenience function to analyze emotion in text.

**Parameters:**
- `text` (str): Text to analyze

**Returns:**
- Dict with keys:
  - `anger` (float): Anger score (0.0-1.0)
  - `disgust` (float): Disgust score (0.0-1.0)
  - `fear` (float): Fear score (0.0-1.0)
  - `joy` (float): Joy score (0.0-1.0)
  - `sadness` (float): Sadness score (0.0-1.0)
  - `dominant_emotion` (str): The primary emotion detected

**Example:**
```python
result = analyze_emotion("I love this!")
# {'anger': 0.0, 'disgust': 0.0, 'fear': 0.0, 'joy': 0.15, 'sadness': 0.0, 'dominant_emotion': 'joy'}
```

### EmotionDetector Class

#### __init__(api_url: Optional[str] = None, timeout: int = 5)

Initialize the emotion detector.

**Parameters:**
- `api_url` (str, optional): Watson API endpoint URL
- `timeout` (int): Request timeout in seconds (default: 5)

#### detect(text: str) -> Dict

Detect emotions in text.

**Parameters:**
- `text` (str): Text to analyze

**Returns:**
- Dict with emotion scores and dominant emotion

### Utility Functions

#### validate_text(text: str) -> bool

Validate if text is suitable for emotion analysis.

```python
from emotion_detector import validate_text

if validate_text("Some text"):
    result = analyze_emotion("Some text")
```

#### get_emotion_intensity(score: float) -> str

Convert emotion score to human-readable intensity.

```python
from emotion_detector import get_emotion_intensity

intensity = get_emotion_intensity(0.75)
# Returns: "High"
```

## Emotion Scores

- **0.0 - 0.2**: Very Low
- **0.2 - 0.4**: Low
- **0.4 - 0.6**: Medium
- **0.6 - 0.8**: High
- **0.8 - 1.0**: Very High

## Examples

### Example 1: Simple Text Analysis

```python
from emotion_detector import analyze_emotion

texts = [
    "I am so happy!",
    "This is terrible!",
    "I'm scared",
]

for text in texts:
    result = analyze_emotion(text)
    print(f"Text: {text}")
    print(f"Dominant Emotion: {result['dominant_emotion']}")
    print()
```

### Example 2: Batch Processing

```python
from emotion_detector import EmotionDetector

detector = EmotionDetector()
results = []

for text in text_list:
    result = detector.detect(text)
    results.append(result)

# Analyze results
happy_count = sum(1 for r in results if r['dominant_emotion'] == 'joy')
print(f"Happy texts: {happy_count}/{len(results)}")
```

### Example 3: Flask Integration

```python
from flask import Flask, request, jsonify
from emotion_detector import analyze_emotion

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    text = data.get('text', '')
    result = analyze_emotion(text)
    return jsonify(result)
```

## Environment Variables

Create a `.env` file to configure Watson API credentials (optional):

```env
WATSON_API_KEY=your_api_key
WATSON_API_URL=your_watson_endpoint
WATSON_AUTH_TYPE=iam
```

## Error Handling

The package automatically handles errors:

- **API Connection Errors**: Falls back to local detection
- **Invalid Input**: Returns empty response with all scores as None
- **Malformed Response**: Falls back to local detection

```python
from emotion_detector import analyze_emotion

# Invalid input
result = analyze_emotion("")
# {'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None, 'dominant_emotion': None}
```

## Testing

Run tests with pytest:

```bash
pip install pytest
pytest tests/
```

## Performance

- **Local Fallback**: ~1-5ms per text
- **Watson API**: ~100-500ms per text (depends on API availability)

## Requirements

- Python 3.8+
- requests
- ibm-watson
- python-dotenv

## License

MIT License - see LICENSE file for details

## Contributing

Contributions are welcome! Please feel free to submit pull requests.

## Support

For issues and questions, please open an issue on GitHub.

## Changelog

### v1.0.0 (2024-08-18)
- Initial release
- Watson API integration
- Local fallback detection
- Comprehensive API documentation
- Full type hints and docstrings
