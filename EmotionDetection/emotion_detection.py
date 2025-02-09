import requests, json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myinput = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, json = myinput, headers=headers)

    if response.status_code == 400:
        return {
        'anger': None,
        'disgust': None,
        'fear': None,
        'joy': None,
        'sadness': None,
        'dominant_emotion': None
        }
    
    data = json.loads(response.text)['emotionPredictions'][0]['emotion']

    return {
    'anger': data['anger'],
    'disgust': data['disgust'],
    'fear': data['fear'],
    'joy': data['joy'],
    'sadness': data['sadness'],
    'dominant_emotion': max(data, key=data.get)
    }