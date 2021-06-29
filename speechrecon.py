import speech_recognition as dd

r = dd.Recognizer()
def Escuchando():
	with dd.Microphone() as source:
		print('Hablar : ')
		audio = r.listen(source)

	try:
	    textrecon = r.recognize_google(audio,language="es-ES")
	    print('Dijo: {}'.format(textrecon))
	except:
	    print('No se pudo procesar')
	    textrecon=''
	
