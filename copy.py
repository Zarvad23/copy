import shutil
import keyboard
import os
import time


game = "C:\Games\FTLAdvancedEdition\FTL Advanced Edition\FTL Advanced Edition\FTLGame.exe"
prof_g = r'C:\Users\Student\Documents\My Games\FasterThanLight\ae_prof.sav'#Путь до сохранения профиля игры
prof_s = r'C:\Users\Student\Documents\My Games\Save\ae_prof.sav'#Путь до сохранения профиля игры в папке Save
save_g = r'C:\Users\Student\Documents\My Games\FasterThanLight\continue.sav'#Путь до сохранения игры
save_s = r'C:\Users\Student\Documents\My Games\Save\continue.sav'#Путь до сохранения игры в папке Save

while True:
	time.sleep(1)
	if keyboard.is_pressed('c'):
		os.system("TASKKILL /F /IM FTLGame.exe")
		time.sleep(2)
		shutil.copy(prof_g, prof_s)
		shutil.copy(save_g, save_s)

	elif keyboard.is_pressed('v'):
		os.system("TASKKILL /F /IM FTLGame.exe")
		time.sleep(2)
		shutil.copy(prof_s, prof_g)
		shutil.copy(save_s, save_g)
		time.sleep(2)
		os.startfile(game)
	elif keyboard.is_pressed('esc'):
		break
