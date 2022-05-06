from subprocess import call, Popen
import os
import time


# Python doesn't have a native clear function, so we need to define one and then call it
def clear():
    # For Windows systems
    if os.name == "nt":
        _ = os.system("cls")
  
    # For Mac and Linux(here, os.name is 'posix')
    else:
        _ = os.system("clear")


print("********************************************************")
print(" ____  _                        ____            _       ")
print("|  _ \(_)                      |  _ \          | |      ") 
print("| |_) |_ _ __   __ _ _ __ _   _| |_) | ___   __| |_   _ ")
print("|  _ <| | '_ \ / _` | '__| | | |  _ < / _ \ / _` | | | |")
print("| |_) | | | | | (_| | |  | |_| | |_) | (_) | (_| | |_| |")
print("|____/|_|_| |_|\__,_|_|   \__, |____/ \___/ \__,_|\__, |")
print("                           __/ |                   __/ |")
print("                          |___/                   |___/ ")
print("********************************************************")
print("An N-body simulation comparison program")
print("********************************************************")
print("Press '1' to execute the Pairwise Force Algorithm.")
print("Press '2' to execute the Barnes-Hut Tree Algorithm.")
print("Press '3' to exit the application and kill the virtual environment.\n\n")

option = int(input("Enter your choice: ")) 

if option == 1:
    clear()
    print("********************************************************")
    print("PAIRWISE PYTHON VIRTUAL ENVIRONMENT ACTIVATED")
    print("********************************************************")
    time.sleep(2)
    Popen("activate_venv_pairwise.bat")
    input("Press ENTER to exit")

elif option == 2:
    clear()
    print("********************************************************")
    print("BARNES-HUT PYTHON VIRTUAL ENVIRONMENT ACTIVATED")
    print("********************************************************")
    time.sleep(2)
    Popen("activate_venv_barnes_hut.bat")
    input("Press ENTER to exit")

elif option == 3:
    clear()
    print("********************************************************")
    print("BARNES-HUT PYTHON VIRTUAL ENVIRONMENT DEACTIVATED")
    print("********************************************************")
    time.sleep(2)
    Popen("venv\Scripts\deactivate.bat")
    print("Thank you for using this application.")
    input("Press ENTER to exit")

else:
    print("Please enter a valid option")


