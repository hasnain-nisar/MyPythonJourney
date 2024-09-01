# pyttsx3 is a text to speech module. Every information is available on website.

import pyttsx3
engine = pyttsx3.init()
engine.say("I will speak this text")
engine.runAndWait()

# Write a python programme to print the contents of a directory using OS module.

import os

# Specify the directory you want to list.
directory_path = r'C:\Users\Hasnain\OneDrive\Desktop\py'

# List al files and directories in the specified order.
contents = os.listdir(directory_path)

# Print each file and directory name.
for items in contents:
    print(items)