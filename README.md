# RHBFWebhook
Rusher Hack (Minecraft Java 1.12.2 payed hacked client link - https://rusherhack.org/) Base Finder (A module in Rusher Hack https://rusherhack.org/features/basefinder.html)  Webhook (discord webhook) is a tool that utilizes the log file of basefinder to send messages to a discord webhook that 
gives neccasary data such as: server, time, date, what was found and related cords (e.g. There is a bed near X:-131313, Y:120, Z:-293912).
It also provides a screenshot of the minecraft window. Its coded in purely python (with an exception of the config json).

# Screenshot feature
The screenshot feature is unique as you know if you have found something worth going back to, it maximizes and brings the minecraft window infront everything else using a combination of win32gui and win32con (both part of the pywin32 package) and pyautogui's screenshot function to take a full screen screenshot and saves it to the local folder. It then sends it in an embed (so it looks beautiful) to the webhook (this took me way too long to code as it has nearly no ducumentation of it online).

# Requirements to run python yourself
Python IDE - such as visual studio code or pycharm (I used pycharm for this project)
Python - https://www.python.org/downloads/
Installed Packages - download requirements.txt, open a terminal in the directory the file is found in and run "pip install -r requirments.txt" or "pip3 install -r requirments.txt"
A brain - may be useful for this process

# How to configure
If you installed the compiled version from releases then you need to:
1. Unzip the file
2. run setup.exe
3. go through the process of setup.exe
4. run main.exe
5. It should work after that, it will say if you need to do anything further. Any issues or errors you can report in the issues tab

If you installed the python files you need to:
1. Run setup.py
2. go through the process of setup.py
3. Run main.py
4. It also should work the same as the compiled exe files, you may also edit the code all you want to configure it to your liking this way
5. basically the same as the exe


