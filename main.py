from subprocess import call, Popen
import os
import time


# Python doesn't have a native clear function
# we need to define one and then call it
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
print("An N-body simulation comparison application")
print("********************************************************")
print("Press '1' to execute the UNTHREADED Pairwise Force Algorithm.")
print("Press '2' to execute the THREADED Pairwise Force Algorithm.")
print("Press '3' to execute the UNTHREADED Barnes-Hut Tree Algorithm.")
print("Press '4' to execute the THREADED Barnes-Hut Tree Algorithm.")
print("Press '5' to exit and the virtual environment.\n\n")

option = int(input("Enter your choice: "))
if option == 1:
    clear()
    print("********************************************************")
    print("UNTHREADED PAIRWISE PYTHON VIRTUAL ENVIRONMENT ACTIVATED")
    print("********************************************************")
    time.sleep(1)
    Popen("activate_venv_unthreaded_pairwise.bat")
    input()

elif option == 2:
    clear()
    print("********************************************************")
    print("THREADED PAIRWISE PYTHON VIRTUAL ENVIRONMENT ACTIVATED")
    print("********************************************************")
    time.sleep(1)
    Popen("activate_venv_threaded_pairwise.bat")
    input()

elif option == 3:
    clear()
    print("********************************************************")
    print("UNTHREADED BARNES-HUT PYTHON VIRTUAL ENVIRONMENT ACTIVATED")
    print("********************************************************")
    time.sleep(1)
    Popen("activate_venv_unthreaded_barnes_hut.bat")
    input()

elif option == 4:
    clear()
    print("********************************************************")
    print("THREADED BARNES-HUT PYTHON VIRTUAL ENVIRONMENT ACTIVATED")
    print("********************************************************")
    time.sleep(1)
    Popen("activate_venv_threaded_barnes_hut.bat")
    input()

elif option == 5:
    clear()
    print("********************************************************")
    print("BARNES-HUT PYTHON VIRTUAL ENVIRONMENT DEACTIVATED")
    print("********************************************************")
    time.sleep(1)
    Popen("venv\Scripts\deactivate.bat")
    print("Thank you for using this application.")
    input()

else:
    print("Please enter a valid option")
