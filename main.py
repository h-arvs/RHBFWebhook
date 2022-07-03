import Checks
import os
import json
import requests
import WindowSSHandler
import sys
from FileModHandler import FileModified

config = ""
if os.path.exists("./config.json"):
    with open("config.json") as f:
        config = json.load(f)
        f.close()
else:
    print("There is no config.json, try unzipping the file again.")
    input(r"press enter to close: ")
    sys.exit()

if Checks.webhook_check(config.get("webhook")) is not True:
    print("Webhook is invalid, have you run setup?")
    input(r"press enter to close: ")
    sys.exit()

if Checks.AdvancedFileCheck(config.get("logdir")) is not True:
    print("Log dir is invalid, try running setup again")
    input(r"press enter to close: ")
    sys.exit()

if Checks.CheckForWindow("Minecraft 1.12.2") is False:
    print("Minecraft java is not open, please open it.")
    input(r"press enter to close: ")
    sys.exit()

print("Watching log file")


def send_webhook():
    file = open(config.get("logdir"))
    lines = file.readlines()
    last_line = lines[-1:]
    file = WindowSSHandler.ScreenShotWindow("Minecraft 1.12.2")

    server = last_line[0][last_line[0].find("[") + 1:last_line[0].find("]")]
    timeanddate = last_line[0][last_line[0].find("][") + 2:last_line[0].find("] ")]
    found = " ".join(last_line[0].split(" ")[2:])
    jsonstr = json.dumps({'username': config.get("user").get("name"), 'content': f'<@{config.get("userid")}>',
                          'avatar_url': config.get("user").get("avatar url"),

                          'embeds': [
                              {
                                  'type': 'rich',
                                  'title': f'{server}',
                                  'description': f'{found}',
                                  'footer': {'text': f'{timeanddate}'},

                                  'image': {"url": f"attachment://{file}"}
                              }
                          ]})
    h = {
        'payload_json': jsonstr
    }

    r = requests.post(config.get("webhook"), data=h, files=dict(file=open(file, 'rb')))
    if r.status_code == 200:
        print("Sent Data")
    else:
        print(r.json())
        print(f"Failed to send Data ({r.status_code})")

    if config.get("KeepScreenshots") is False:
        os.remove(file)


filemodhandler = FileModified(fr"{config.get('logdir')}", send_webhook)
filemodhandler.start()
