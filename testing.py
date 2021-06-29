import speech_recognition as dd
import time as tm

a = False
r = dd.Recognizer()
def Escuchando():
	with dd.Microphone() as source:
		audio = r.listen(source)

	try:
	    textrecon = r.recognize_google(audio,language="es-ES")
	    textrecon = textrecon.strip().lower()
	    print(textrecon)
	    if textrecon == ['tau']:
	    	print('Me llamo TAU')
	except:
	    print('No se pudo procesar')
	    textrecon=''
while a == False:
	date = str(int(tm.time()))
	print('< '+date+' >')
	Escuchando()