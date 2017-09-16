from gtts import gTTS
import os
class tp1:
    def speech(self,v):

        tts = gTTS(text=v, lang='en')
        tts.save("good.mp3")
        os.system("mpg321 good.mp3")