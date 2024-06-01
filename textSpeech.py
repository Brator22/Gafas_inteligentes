from gtts import gTTS
import pygame
import requests
from stt import SpeechtoText

EDPOINT_URL="https://api.openai.com/v1/chat/completions"
API_KEY="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"

headers = {
    "Authorization": "Bearer " + API_KEY,
    "Content-Type": "application/json"
}

def  getAnswer(question):
    #question = 'cuantos estados tiene estados unidos '

    data={

        "model":"gpt-3.5-turbo",
        "messages":[
            {
                "role":"user",
                "content":"en un parrafo de no mas de 40 palabras,"+question
            }
        ]
    }
    response=requests.post(EDPOINT_URL,
                            json=data,
                            headers=headers)
                            
    result = response.json()['choices'][0]['message']['content']
    print(result)

    return result

class TTS():
    def __init__(self):
        pygame.init()

    def playText(self,text):
        tts = gTTS(text, lang ='es')
        tts.save('file.mp3')

        pygame.mixer.music.load("file.mp3")
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            continue

if __name__ == "__main__":
    tts = TTS()

    speech = SpeechtoText()
    ret, text = speech.getText()
    if ret:
        print('El texto es: ', text)
        result = getAnswer(text)
        tts.playText(result)
    else:
        print('Error: ', text)
        tts.playText(text)

    
