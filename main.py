from subprocess import call
from os import name, system


# Python doesn't have a native clear function, so we need to define one and then call it
def clear():
    # For Windows systems
    if name == "nt":
        _ = system("cls")
  
    # For Mac and Linux(here, os.name is 'posix')
    else:
        _ = system("clear")


print("*****************************************************")
print("BinaryBody - An N-body simulation comparison program")
print("*****************************************************")
print("Press '1' to execute the Pairwise Force Algorithm.")
print("Press '2' to execute the Barnes-Hut Tree Algorithm.")
print("Press '3' to exit the application.\n\n")

option = int(input("Enter your choice: ")) 

if option == 1:
    clear()
    call("python pairwise/pairwise_non_vectorized_NOVIS.py", shell=True)
    input("Press ENTER to exit")

elif option == 2:
    clear()
    call("python barnes_hut/barnes_hut_quadtree_NOVIS.py", shell=True)
    input("Press ENTER to exit")

elif option == 3:
    print("Thank you for using this application. Press any key to continue")
    input("Press ENTER to exit")

else:
    print("Please enter a valid option")


