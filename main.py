import os
import subprocess
import time

if not os.path.exists("media"):
    os.makedirs("media")

email = ""
n = int(input("How many people you want to add : "))

if(len(os.listdir("media")) == 0):
    email = input("Please enter Email Address : ")

    with open("email.txt","w") as file:
        file.write(email)
    file.close()

while len(os.listdir("media"))<n:
    print("!!! Drop the photos of family members in media folder !!!")
    time.sleep(5)

print("Starting Detector...")
subprocess.run(["python", "detector.py"])