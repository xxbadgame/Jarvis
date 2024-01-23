import speech_recognition as sr
import requests
import pyttsx3

# Initialiser le moteur de reconnaissance vocale
recognizer = sr.Recognizer()

# Initialiser le moteur TTS
tts_engine = pyttsx3.init()

# Votre clé API OpenAI
api_key = "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"

def get_chatgpt_response(text):
    response = requests.post(
        "https://api.openai.com/v1/engines/davinci-codex/completions",
        headers={"Authorization": f"Bearer {api_key}"},
        json={"prompt": text, "max_tokens": 150}
    )
    return response.json()["choices"][0]["text"].strip()

while True:
    try:
        with sr.Microphone() as source:
            print("Je vous écoute...")
            audio = recognizer.listen(source)
            text = recognizer.recognize_google(audio)
            print(f"Vous avez dit: {text}")

            response = get_chatgpt_response(text)
            print(f"Réponse de ChatGPT: {response}")
            tts_engine.say(response)
            tts_engine.runAndWait()
    except Exception as e:
        print(f"Erreur: {e}")
