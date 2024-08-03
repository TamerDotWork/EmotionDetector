from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 import Features, EmotionOptions
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from flask import Flask, request, jsonify
import logging
# Set up IBM Watson NLU credentials
api_key = 'cyEJ8kUS7fv66WDXDHpkmkQcV9gL3ZHtNsXym3p_vtlV'
service_url = 'https://api.au-syd.natural-language-understanding.watson.cloud.ibm.com/instances/c2e19256-8e33-42a7-a19d-1f49833f8fa5'
 
# Authenticate
authenticator = IAMAuthenticator(api_key)
natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2021-08-01',
    authenticator=authenticator
)
natural_language_understanding.set_service_url(service_url)


def detect_emotions(text):
    if len(text.strip()) < 5:
        raise ValueError("Text too short to analyze emotions.")
    
    try:
        response = natural_language_understanding.analyze(
            text=text,
            features=Features(emotion=EmotionOptions())
        ).get_result()
        
        return response['emotion']['document']['emotion']
    except Exception as e:
        logging.error(f"Error in detect_emotions: {e}")
        return {}


app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <h1>Emotion Detection</h1>
        <form action="/detect_emotion" method="post">
            <textarea name="text" rows="4" cols="50"></textarea><br>
            <input type="submit" value="Detect Emotion">
        </form>
    '''

@app.route('/detect_emotion', methods=['POST'])
def detect_emotion():
    text = request.form['text']
    emotions = detect_emotions(text)
    return jsonify(emotions)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)