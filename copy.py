import shutil
import keyboard
import os
import time


game = r'D:\Games\FTL Advanced Edition\FTLGame.exe'
prof_g = r'D:\Documents\My Games\FasterThanLight\ae_prof.sav'#Путь до сохранения профиля игры
prof_s = r'D:\Desktop\Save\ae_prof.sav'#Путь до сохранения профиля игры в папке Save
save_g = r'D:\Documents\My Games\FasterThanLight\continue.sav'#Путь до сохранения игры
save_s = r'D:\Desktop\Save\continue.sav'#Путь до сохранения игры в папке Save
directory = r'C:\Users\Student\Desktop\Saves'#ут указываешь путь до папки в которой будут хранится папки с сейвами


while True:
	time.sleep(0.1)
	if keyboard.is_pressed('shift+c'):
		os.system("TASKKILL /F /IM FTLGame.exe")
		time.sleep(2)
		shutil.copy(prof_g, prof_s)
		shutil.copy(save_g, save_s)
	elif keyboard.is_pressed('shift+`'):
		name = input('Введите название папки')
		fullname = os.path.join(directory, name)
		os.mkdir(fullname)
	elif keyboard.is_pressed('shift+v'):
		os.system("TASKKILL /F /IM FTLGame.exe")
		time.sleep(2)
		shutil.copy(prof_s, prof_g)
		shutil.copy(save_s, save_g)
		time.sleep(2)
		os.startfile(game)
	elif keyboard.is_pressed('shift+esc'):
		break
