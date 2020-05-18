from gtts import gTTS
from playsound import playsound

# Custome Modules
from remove_file import remove_file


def text_to_speech(text):
    audio_file = "audio.mp3"
    remove_file(audio_file)

    language = 'en'
    myobj = gTTS(text=text, lang=language, slow=False)
    myobj.save(audio_file)
    playsound(audio_file)
