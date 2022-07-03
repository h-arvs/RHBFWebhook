import json
import os
import Checks

setup = True
config = ""
if os.path.exists("./config.json"):
    with open("config.json") as f:
        config = json.load(f)
        f.close()
else:
    print("There is no config.json, try unzipping the file again.")
    exit()


print("Running Config")
filecheck = Checks.LogFileCheck()
if filecheck is False:
    print("We guessed your log file dir and couldn't find it, please input it here:")
    inputting = True
    while inputting:
        i = input(r"dir: ")
        if Checks.AdvancedFileCheck(i) is True:
            print("File path valid, continuing")
        elif Checks.AdvancedFileCheck(i) is not True:
            print("Path invalid (must be txt file)")

elif filecheck is not False:
    print(f"Found your log file at {filecheck} (if this is wrong manually change it in config.json)")
    config["logdir"] = filecheck

print("Please enter your discord Webhook URL")
iurl = True
while iurl:
    i = input(r"URL: ")
    check = Checks.webhook_check(i)

    if check is True:
        print("Webhook valid")
        config["webhook"] = i
        iurl = False
    elif check is not True:
        print("Invalid webhook")

print("Type your user id")
inputting = True
while inputting:
    i = input(r"Int: ")
    if i.isdigit() and len(i) == 18:
        print("Valid ID")
        config["userid"] = i
        inputting = False
    else:
        print("Invalid ID")
with open("config.json", "w") as f:
    json.dump(config, f)
print("For extra customization, see config.json")
print("Setup is now done! You may run main")

