import os
import operator
import pyttsx3

system = pyttsx3.init()
voice = system.getProperty('voices')
system.setProperty('voice', voice[1].id)
pyttsx3.speak("HI, my long lost buddy! Welcome to my program... I am here to help open some applications for you. Please enter any program of your choice.")

chrome_list = ["chrome", "internet", "google", "browser"]
notepad_list = ["notepad", "text editor", "editor", "text", "notes"]
cmd_list = ["cmd prompt", "cmd", "command prompt", "command", "prompt"]
player_list = ["music", "wmplayer", "music player", "songs"]
youtube_list = ["youtube", "utube", "Youtube"]
linkedin_list = ["linkedin", "Linkedin", "LinkedIn"]
mail_list = ["mail", "gmail", "inbox", "messages"]

while True:
 user = (input("Enter your requirement:\t\n"))
 user = user.split()
 #os.system(user)
 if bool(set(user).intersection(chrome_list))==True:
  os.system("start chrome")
  pyttsx3.speak("Opening google chrome.")
 elif bool(set(user).intersection(notepad_list))==True:
  os.system("start notepad")
  pyttsx3.speak("Opening notepad.")
 elif bool(set(user).intersection(cmd_list))==True:
  os.system("start cmd")
  pyttsx3.speak("Opening command prompt.")
 elif bool(set(user).intersection(player_list))==True:
  os.system("start wmplayer")
  pyttsx3.speak("Starting music player.")
 elif bool(set(user).intersection(youtube_list))==True:
  os.system("start https://www.youtube.com/")
  pyttsx3.speak("Starting youtube.")
 elif bool(set(user).intersection(linkedin_list))==True:
  os.system("start https://www.linkedin.com/")
  pyttsx3.speak("Opening Linkedin.")
 elif bool(set(user).intersection(mail_list))==True:
  os.system("start https://mail.google.com/mail/u/0/#inbox")
  pyttsx3.speak("Opening your gmail inbox.")
 elif ("exit" in user) or ("quit" in user):
  pyttsx3.speak("Good friends never say goodbye, they simply say, see you soon!")
  break
 else:   
   print("ERROR: Do not support. Please try again!")
   pyttsx3.speak("Please Try Again")