<p align = "center">
  <img src="/logos/BinaryBodyLogo.png" alt="BinaryBodyLogo" title="BinaryBodyLogo" style="width: 200px; height: 200px;">
</p>

# BinaryBody

<p>
  BinaryBody is an N-body simulation comparison application forming the basis of my final year Honours project.

  The application is built in Python, is CLI-based and allows the user to compare a naive Pairwise Interaction Algorithm and Barnes-Hut Quadtree against one another.

  The number of bodies can be entered by the user via a prompt. This applies to both simulations.
</p>

## START RUNNING SIMULATIONS

<p>
  Run "main.py"

  If main.py is running into any issues regarding libraries, you may need to install them from "requirements.txt".
  This can be done via the following:

  Install libraries from requirements.txt<br>
    - pip install -r requirements.txt <br>
  If this doesn't work, use this.<br>
    - pip3 install -r requirements.txt<br>
  
  When this is done, you can choose to run either the Pairwise Algorithm simulation, by selection option "1" or Barnes-Hut Quadtree simulation by selecting option "2".
  Both simulations, when executed, will activate the virtual environment (venv) contained within "venv/Scripts/activate.bat"

  When the Pairwise or Barnes-Hut simulations are executed, once the user has entered the number of bodies, the program will display how long it has taken that particular simulation to run in it's entirety, with the specified number of bodies, as well as how long it has spent on each section/function.
  within that script. Once this has been done, the program will close.

  If the user wishes to run another simulation, they will need to execute main.py.

  Once the user is done, execute main.py again and select option "3" to deactivate the virtual environment (venv).

  While main.py needs to be executed every time the user wants to run a new simulation, which activates the virtual environment (venv), as well as when they want to deactivate the virtual environment (venv), this is to avoid using "while(1)" to keep the script active.
  
  This is because it is not advisable to use it in real-world scenarios because it increases the CPU usage while also potentially blocking the code.
</p>
