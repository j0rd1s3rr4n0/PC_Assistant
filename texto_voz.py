from gtts import gTTS 
from playsound import playsound 
text = input('>')
def Hablar():
	var = gTTS(text = text,lang = 'es')
	var.save('audio.mp3')
	playsound('.\\audio.mp3')
Hablar()