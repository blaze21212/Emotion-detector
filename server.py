from flask import Flask, render_template, request
from emotion_detector import analyze_emotion

app = Flask("Emotion Detector")

@app.route("/")
def render_index_page():
    """Renders the HTML interface."""
    return render_template("index.html")

@app.route("/emotionDetector")
def emotion_analyzer():
    """Analyzes text sent via query params and returns formatted text."""
    text_to_analyze = request.args.get('textToAnalyze')
    response = analyze_emotion(text_to_analyze)

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    return (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, 'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. The dominant emotion is "
        f"<b>{response['dominant_emotion']}</b>."
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
