import os

def shutdown():
    os.system("shutdown /s /t 0")

def ask_user():
    answer = input("Do you want to shut down the computer? (yes/no): ")
    if answer == "yes":
        shutdown()
    else:
        print("Okay, not shutting down.")

ask_user()



