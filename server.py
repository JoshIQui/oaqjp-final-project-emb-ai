"""Server Code."""
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector
app = Flask("Emotion Detector")

@app.route("/")
def render_index_page():
    """Function for rendering the app page."""
    return render_template('index.html')

@app.route('/emotionDetector')
def detect_emotion():
    """Function for getting the emotion detection and returning the response."""
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the sentiment_analyzer function and store the response
    response = emotion_detector(text_to_analyze)
    dominant_emotion = response.pop('dominant_emotion')

    # If the dominant emotion is set to None, display a message instead
    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    # Remove the curly braces from the dictionary
    formatted_emotions = ', '.join(f"'{key}': {value}" for key, value in response.items())

    # Return a formatted string with the sentiment label and score
    return (
    f"For the given statement, the system response is {formatted_emotions}. "
    f"The dominant emotion is {dominant_emotion}"
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
