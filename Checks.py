import validators
import requests
import json
import os
import win32gui

config = ""
if os.path.exists("./config.json"):
    with open("config.json") as f:
        config = json.load(f)
        f.close()


def webhook_check(url):
    if validators.url(url):
        h = {
            'username': config.get("user").get("name"), 'content': f'<@{config.get("userid")}>',
            'avatar_url': config.get("user").get("avatar url"),
            "embeds": [
                {"title": "Checking your webhook",
                 "description": "Looks fine to me"}]

        }
        r = requests.post(url, json=h)
        if r.status_code == 401:
            print(r.text)
            return False
        elif r.status_code == 204:
            return True
        else:
            print(r.text)
            return r.status_code

    else:
        return "Not a URL"


def LogFileCheck():
    LogFileDir = os.getenv("APPDATA") + "\\.minecraft\\rusherhack\\BaseFinder\\Log.txt"

    if os.path.exists(LogFileDir):
        return LogFileDir
    else:
        return False


def AdvancedFileCheck(i):
    if os.path.exists(i):
        if i.endswith(".txt"):
            return True
        else:
            return False
    else:
        return False


def CheckForWindow(name: str):

    if win32gui.FindWindow(None, name) != 0:
        return True
    else:
        return False
