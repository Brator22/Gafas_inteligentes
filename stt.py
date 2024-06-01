# Speech To Text
# lmcapacho - 2023

import speech_recognition as sr
import os, sys, contextlib

# https://stackoverflow.com/a/70467199
@contextlib.contextmanager
def ignoreStderr():
    devnull = os.open(os.devnull, os.O_WRONLY)
    old_stderr = os.dup(2)
    sys.stderr.flush()
    os.dup2(devnull, 2)
    os.close(devnull)
    try:
        yield
    finally:
        os.dup2(old_stderr, 2)
        os.close(old_stderr)

class SpeechtoText():
    def __init__(self, timeout=2000):
        self.timeout = timeout
        self.recognizer = sr.Recognizer()        

    def getText(self):
        try:
            with ignoreStderr():
                with sr.Microphone() as source:
                    self.recognizer.adjust_for_ambient_noise(source)
                    print("Di algo...")
                    audio = self.recognizer.listen(source, timeout=self.timeout)
                
                print('Reconocimiento...')
                try:
                    text = self.recognizer.recognize_google(audio, language = "es-ES")
                    return True, text
                except sr.UnknownValueError:
                    return False, 'Audio no reconocido'
                except sr.RequestError as e:
                    return False, e
                
        except sr.WaitTimeoutError:
            return False, 'Audio no capturado'

# Test
if __name__ == "__main__":
    speech = SpeechtoText()
    ret, text = speech.getText()
    if ret:
        print('El texto es: ', text)
    else:
        print('Error: ', text)