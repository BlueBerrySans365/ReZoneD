import json
import requests
import time
import os
#import coloredSigns as cS
import pypresence as pypr
import sys
import pymongo




version = "1.0.0b"
IsDebugTree = False
clear = lambda: os.system('cls')



if os.path.isfile("config.json") == False:
       print("Preparing app...")
       time.sleep(3)
       data = {
              "UserData": {
                     "Nickname": "None",
                     "ColoredT": "False",  # I will change it in future .w.
                     "Tag": None,
                     "AppID": "None",
                     "FirstRun": True
              },
              "ButtonsData": {
                     "inUse": False,
                     "button1": {
                            "lable": "",
                            "url": ""
                     },
                     "button2": {
                            "lable": "",
                            "url": ""
                     },
              },
              "AppData": {
                     "version": f"{version}",
                     "lang": None
              }
       }
       with open("config.json", "w") as outfile:
              json.dump(data, outfile)
       print("Successfully configured!")
       with open('config.json') as json_file:
            AppConf = json.load(json_file)
       time.sleep(3)
       clear()
else:
       with open('config.json') as json_file:
            AppConf = json.load(json_file)
       print("Loaded config.json!")
       time.sleep(3)
       clear()



with open('./lang/ru_RU.json', encoding="utf-8") as jsonfile:
    ruLang = json.load(jsonfile)



if AppConf['UserData']['FirstRun'] == True:
	lang = input("Select language\n1 - Ru, 2 - En\nYour choice | [>] ")
	if lang == "1":
		print("Вы выбрали русский язык!")
		lang = "ru"
	if lang == "2":
		print("You have chosen English!")
		lang = "en"
	if lang != "en" and lang != "ru":
		print("The language is selected incorrectly! I'll put it in English.")
		lang = "en"
	if lang == "ru":
		print(ruLang["starter"]["startStarter"])
		NicknameStartUp = input(ruLang['starter']['nicknameStarter'])
		TagQStartUp = input(ruLang['starter']['tagQStarter'])
		if TagQStartUp.lower() == "y":
			TagStartUp = input(ruLang['starter']['tagStarter'])
		elif TagQStartUp.lower() == "n":
			TagStartUp = None
		AppIDQStartUp = input(ruLang['starter']['AppIDQStarter'])
		if AppIDQStartUp.lower() == "y":
			AppIDStartUp = input(ruLang['starter']['AppIDStarter'])
		elif AppIDQStartUp.lower() == "n":
			AppIDStartUp = "619183056636477466"




	if lang == "en":
		print("Oh UwU \nLooks like this is your first run owo.\nLet's configure your account before starting. :3")
		NicknameStartUp = input("Your nickname? | [>] ")
		TagQStartUp = input("Do you want to make tag? [Y/N] | [>] ")
		if TagQStartUp.lower() == "y":
			TagStartUp = input("Your Tag? (4 numbers) | [>] ")
		elif TagQStartUp.lower() == "n":
			TagStartUp = None
		AppIDQStartUp = input("Do you want to use custom Discord Rich Presence? (Y/N) | [>] ")
		if AppIDQStartUp.lower() == "y":
			AppIDStartUp = input("Your AppID? | [>] ")
		elif AppIDQStartUp.lower() == "n":
			AppIDStartUp = "619183056636477466"
   
	data = {
		"UserData": {
				"Nickname": NicknameStartUp,
				"ColoredT": "False",
				"Tag": TagStartUp,
				"AppID": AppIDStartUp,
				"FirstRun": False
			},
		"ButtonsData": {
				"inUse": False,
				"button1": {
					"lable": "",
					"url": ""
				},
				"button2": {
					"lable": "",
					"url": ""
				},
		},
		"AppData": {
				"version": f"{version}",
				"lang": lang
		}
	}

	with open("config.json", "w") as outfile:
		json.dump(data, outfile)
	if lang == "ru":
		print(ruLang['systemStart']['successSConf'])
	else:
		print("Successfully saved!")
	with open('config.json') as json_file:
		AppConf = json.load(json_file)

rpc = pypr.Presence(AppConf['UserData']['AppID'])
rpc.connect()

def starter():
       rpc.update(state=ruLang['discordRPC']['startState'], details=ruLang['discordRPC']['startDetails'], large_image="chill_zone")
       print("")
       print("╔============================================================================╗")
       print("║ ChillZone.exe                                                  [ - ] [ x ] ║")
       print("╠============================================================================╣")      
       print("║  [Chill Zone App]                                          by NickSaltFoxu ║")
       print("╠============================================================================╣")
       print("║                           [ Information about app ]                        ║")
       print("║                                                                            ║")
       print("║                          This app currently in Beta                        ║")
       print("║                                  That's all                                ║")
       print("║                                                                            ║")
       print("║                             All commands in [help]                         ║")
       print("╠============================================================================╣")
       print("╚============================================================================╝")
       print("")
       print("")




def help():
       print("")
       print("╔============================================================================╗")
       print("║ ChillZone.exe                                                  [ - ] [ x ] ║")
       print("╠============================================================================╣")      
       print("║                               <==[Commands]==>                             ║")
       print("╠============================================================================╣")
       print("║                            config - Configure app                          ║")
       print("║                              help - This command                           ║")
       print("║                             check - Check for updates                      ║")
       print("║                            enable - Enable Discord Rich Presence           ║")
       print("║                           disable - Disable Discord Rich Presence          ║")
       print("║                             clear - Clear console                          ║")
       print("║                              exit - Exit app                               ║")
       print("║                                                                            ║")
       print("╠============================================================================╣")
       print("╚============================================================================╝")
       print("")

def dataconfig():
       dataconfi = input("What do you need to change? .w. (lowercase letters)")
       if dataconfi == "nickname":
              NicknameNew = input("Your new nickname? | [>] ")
       elif dataconfi == "tag":
              TagQNew = input("Do you want to make tag? [Y/N] | [>] ")
              if TagQNew == "Y" or TagQStartUp == "y":
                     TagNew = input("Your Tag? (4 numbers) | [>] ")
              elif TagQNew == "N" or TagQStartUp == "n":
                     TagNew = None


def menu():
    while True:
       commandI = input("> ")
       if commandI == "help":
              help()
       elif commandI == "clear":
              clear()
              starter()
       elif commandI == "info":
              print(f"| [App Version] > [{version}] |")
       elif commandI == "exit":
              print("")
              clear()
              print("{=][ Exiting... ][=}")
              sys.exit()
       elif commandI == "config":
              dataconfig()
       else:
              print("Wrong command. Try another one .w.")

try:
       starter()
       menu()
except KeyboardInterrupt:
       print("")
       clear()
       print("{=][ Exiting... ][=}")
       sys.exit()
