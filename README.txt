**********************************************************

  ____  _                        ____            _       
 |  _ \(_)                      |  _ \          | |      
 | |_) |_ _ __   __ _ _ __ _   _| |_) | ___   __| |_   _ 
 |  _ <| | '_ \ / _` | '__| | | |  _ < / _ \ / _` | | | |
 | |_) | | | | | (_| | |  | |_| | |_) | (_) | (_| | |_| |
 |____/|_|_| |_|\__,_|_|   \__, |____/ \___/ \__,_|\__, |
                            __/ |                   __/ |
                           |___/                   |___/ 

**********************************************************


BinaryBody is an N-body simulation comparison application forming the basis of my final year Honours project. 
The application is built in Python 3.9, is CLI-based and allows the user to compare a naive Pairwise Interaction Algorithm and 
Barnes-Hut Quadtree against one another. The number of bodies can be entered by the user via a prompt. 
This applies to both simulations.


***********
GET STARTED
***********


*************************
RUN YOUR FIRST SIMULATION
*************************
Run "main.py"

If main.py is running into any issues regarding the libraries installed to the venv, you may need to re-install them from 
"requirements.txt". This can be done via the following:

Install libraries from requirements.txt<br>
  - pip install -r requirements.txt <br>
If this doesn't work, use this.<br>
  - pip3 install -r requirements.txt<br>


**********************
CHOOSE YOUR SIMULATION
**********************
When this is done, you can choose to run either: 
The Pairwise Algorithm simulation, by selection option "1"
OR
The Barnes-Hut Quadtree simulation by selecting option "2"


***************
VENV ACTIVATION
***************
Both simulations when executed will activate the virtual environment (venv) contained within "venv/Scripts/activate.bat"


***************************************
UPON EXECUTION OF THE CHOSEN SIMULATION
***************************************
When the Pairwise or Barnes-Hut simulations are executed, the venv will activate. 
The user will then be prompted to enter the number of bodies to insert into the sim. 
The program will display how long it has taken that particular simulation to run in it's entirety, 
with the specified number of bodies, as well as how long it has spent on each section/function within that script. 
Once this has been done, the program will close.


************************
RUNNING A NEW SIMULATION
************************
If the user wishes to run another simulation, they will need to execute main.py again.


***************   
DEACTIVATE VENV
***************  
Once the user is done, execute main.py again and select option "3" to deactivate the virtual environment (venv).


**************
THINGS TO NOTE
**************
While main.py needs to be executed every time the user wants to run a new simulation, which activates the virtual environment (venv), as well as when they want to deactivate the virtual environment (venv), this is to avoid using "while(1)" to keep the script active. This is because it is not advisable to use it in real-world scenarios because it increases the CPU usage while also potentially blocking the code.
