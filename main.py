import requests
import json
#It took me over 30 minutes to install pycharm on Kali lol
#This is my code
print("Welcome to PYTHON 3.0 But as a mimic of an OS: Created by SlideShowGames! AKA Burn Google!")
print("I guess do whatever it is that you're here for.")
print("Did you know this was originally made for a test?")
print("")
print(".[1] Steal API .[2] Fake Terminal .[3] Exit")
menu = input("")
if menu == "1":
    api1 = input("type the website's name")
    api = requests.get(api1)
    print("Status Code")
    print(api.status_code)
    if api.status_code == 200:
        print("Request received")
    if api.status_code == 404:
        print("Site not found")
    if api.status_code == 503:
        print("Not Ready to send")
    if api.status_code == 301:
        print("URL is a redirect")
    if api.status_code == 400:
        print("Bad request")
    if api.status_code == 401:
        print("You are not verified")
    if api.status_code == 403:
        print("Forbidden")
    print("Response")
    print(api.json())
    print("Why use a python script you could've just used burpsuite community")
    exit()
if menu == "3":
    exit()
if menu == "2":
    print("Welcome to fake terminal")
    print("blah blah blah")
    pkgs = input("main.py $ pseudo: type help for help")
    if pkgs == "help":
        print("help = displays cmds. ls = lists variables. fakefetch = displays neofetch text. notes = prints notes.")
    if pkgs == "notes":
        print("#It took me over 30 minutes to install pycharm on Kali lol")
        print("#This is my code")
        print("#I dont think I needed to add exit()")
    if pkgs == "ls":
        print(menu)
        print(pkgs)
        print("There are two variables menu and pkgs.")
        print("pkgs is your fake terminal option.")
        print("menu is your menu option")
    if pkgs == "fakefetch":
        print("lol I am not adding this I am already off track")
#I dont think I needed to add exit()