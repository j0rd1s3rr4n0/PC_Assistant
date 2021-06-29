import os
import speech_recognition as sr
import datetime
#import wikipedia
import webbrowser
import sys
import platform
import smtplib
import pyfiglet

# Archivos
import Importatium
import speechrecon
import texto_voz

def Jarvis_logo():
	f = pyfiglet.Figlet(font='slant')
	print('===============================================')
	print(f.renderText('J.A.R.V.I.S'))
	print('===============================================')

#===============================================#
#			        OUTPUT                      #
#===============================================#
Jarvis_logo()
menu = int(input('\n[ 0 ] Install Modules\n[ 1 ] Inicialize\n[ 2 ] System Info\nSelection>'))
if menu == 0:
	print(f.renderText('Installing...'))
	Importatium.imports() # Importa los Modulos
elif menu == 1:
	Jarvis_logo()
	speechrecon.Escuchando()
	texto_voz.Hablar(text.speechrecon.Escuchando())


elif menu == 2:
	Importatium.info()