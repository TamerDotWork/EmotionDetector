from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 import Features, EmotionOptions
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
 

# Update API key and URL
API_KEY = 'ApiKey-3442f10e-52c4-450b-a20d-ffffcfff3b29'
URL = 'https://api.us-south.natural-language-understanding.watson.cloud.ibm.com/instances/your_instance_id'

# Set up Watson NLU
authenticator = IAMAuthenticator(API_KEY)
natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2021-08-01',
    authenticator=authenticator
)
natural_language_understanding.set_service_url(URL)

def analyze_emotion(text):
    response = natural_language_understanding.analyze(
        text=text,
        features=Features(emotion=EmotionOptions())
    ).get_result()

    emotions = response['emotion']['document']['emotion']
    return emotions

def format_emotions(emotions):
    formatted_emotions = "\n".join([f"{emotion}: {score:.2f}" for emotion, score in emotions.items()])
    return formatted_emotions
