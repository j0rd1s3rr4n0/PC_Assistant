import os
'''
os.system('pip install SpeechRecognition')
os.system('pip install gTTS')
os.system('pip install playsound')
os.system('pip install PyAutoGUI')
'''

import speech_recognition as dd
from gtts import gTTS 
from playsound import playsound 
import socket
import urllib.request
import time
import math
import getpass
import pyautogui
pi = 3,14159265358979323846264338327950288419716939937510582097494459230781640628620
a = False
decir = ''
textrecon = ''

def Hablar():
	var = gTTS(text = decir,lang = 'es')
	var.save('audio.mp3')
	playsound('.\\audio.mp3')
	os.remove('.\\audio.mp3')

r = dd.Recognizer()
def Escuchando():
	with dd.Microphone() as source:
		print('>')
		audio = r.listen(source)

	try:
		global textrecon
		textrecon = r.recognize_google(audio,language="es-ES")
		textrecon = textrecon.lower()
		print('Dijo: {}'.format(textrecon))
		time.sleep(1.5)
		textrecon = textrecon.split()
	except:
		print('No se pudo procesar')
		textrecon=''

def Menu():
	os.system('cls')
	time.sleep(3)
	print('Puedes,\n- Abrir programas	"Abrir + El programa"\n- Cerrar programas	"Cerrar + El programa"\n- Cual es mi ip\n-Dictame el numero pi')
	global decir
	global textrecon
	Escuchando()
	if textrecon[0] == 'abrir':
		try:
			aplicacion = textrecon[1]
			if aplicacion == 'calculadora':
				decir = 'Abriendo'+aplicacion+'...';Hablar()
				aplicacion = 'calc'
			elif aplicacion == '':
				decir = 'No se Pudo Procesar';Hablar()
			elif aplicacion in ['chrome','google']:
				decir = 'Abriendo Google Chrome...';Hablar()
				aplicacion = 'chrome'
			else:
				decir = 'Cerrando'+aplicacion+'...';Hablar()
			aplicacion = aplicacion+'.exe'
			os.system('start '+aplicacion)
		except:
			decir = 'No se pudo procesar';Hablar()
			pass

	elif textrecon[0] == 'cerrar':
		try:
			aplicacion = textrecon[1]
			if aplicacion == 'calculadora':
				decir = 'Cerrando'+aplicacion;Hablar()
				aplicacion = 'calculator'
			elif aplicacion == '':
				decir = 'No se Pudo Procesar';Hablar()
			elif aplicacion == 'google' and textrecon[2] == 'chrome':
				decir = 'Cerrando Google Chrome';Hablar()
				aplicacion = 'chrome'
			else:
				decir = 'Cerrando'+aplicacion;Hablar()
			aplicacion = aplicacion+'.exe'
			os.system('taskkill /F /IM '+aplicacion)
		except:
			decir = 'No se pudo procesar';Hablar()
			pass
	

	elif textrecon == ['cuál','es','mi','ip']:
		hostname = socket.gethostname() #capturar hostname
		ip_address1 = socket.gethostbyname(hostname) # extraer ip privada
		ip_publica = urllib.request.urlopen('https://ident.me').read().decode('utf-8')# extraer ip publica
		print("HOST: "+str(hostname))
		decir = "Su Dispositivo es:"+str(hostname);Hablar()
		print("Su IP Privada: " +str(ip_address1))
		decir = "Su ipe Privada es:" +str(ip_address1);Hablar()
		print("Su IP Pública: " +str(ip_publica))
		decir = "Su ipe Pública es: " +str(ip_publica);Hablar()
	elif textrecon == ['dictame', 'el', 'número', 'pi']:
		decir ="El numero pi es: "+str(pi);Hablar()
		print("El numero pi es: "+str(pi))
	elif textrecon[0]=='imprime':
		print(textrecon[1:])
		time.sleep(10)
	elif textrecon[0]=='salir':
		global a
		decir ='Llámame cuando lo necesites...';Hablar()
		a = True
		Exit()
	elif textrecon == ['pon', 'música', 'en', 'spotify']:
		user_equip = getpass.getuser()
		os.system('start C:\\Users\\'+user_equip+'\\AppData\\Roaming\\Spotify\\Spotify.exe')
		pyautogui.keyDown('playpause')
	elif textrecon[0] == 'pausa':
		pyautogui.keyDown('playpause')
	elif textrecon[0] == 'continuar': 
		pyautogui.keyDown('playpause')
	else:
		k = 1
while a == False:
	try:
		Menu()
	except:
		pass