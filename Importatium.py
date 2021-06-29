import os
import platform

##### SYSTEM ##### DETECTION #####
sistema = platform.system()
sistema = sistema.lower()
if sistema == 'linux':
	clear = 'clear'
elif sistema == 'windows':
	clear = 'cls'
elif sistema == 'darwin':
	clear = 'clear'
os.system(clear)
##### IMPORT ##### PACKAGES #####
def info():
	inf = str(platform.uname())
	rp = [',','uname_result(','=\'','\'',')','version','system','machine','release','node']
	rr = ['\n',' ',': ','','','# Version','# System','# Machine','# Release','# Node']
	ff = 0
	for d in rp:
		#print(ff)
		inf = inf.replace(rp[int(ff)],rr[int(ff)])
		ff+=1
	print('\n #########################################')
	print(' #              SYSTEM INFO')
	print(' #########################################')
	print(inf)
	print(' #########################################\n')
	

def imports():
	gg = 0
	packages = ['pyttsx3','SpeechRecognition','datetime','wikipedia','webbrowser','pyfiglet','colorama']
	lenn = len(packages)
	for x in packages:
		os.system('pip3 install '+packages[int(gg)])
		gg+=1
	os.system(clear)
	print('Needed modules Installed Succesfully')
