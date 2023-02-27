# 2D curling simulation

This repository represents 2D simulation of curling game made as a project for course of _Numerical software and numerical algorithms_.  
Link to demonstration: https://youtu.be/SW-28sZb-ZY

### Game of curling
Curling is Olympic winter sport played on ice. Consisting of two teams which members are rolling stones on ice, the goal is to place stones as close as possible to the center drawn on court - house. More informations on this sport can be found using link https://worldcurling.org/about/.

As an idea for this project, curling was chosen because of the way it is played - main parts being contacts between stones themselves as well as stones contacts with court borders. Stones motion is also affected by ice and abrasion. Considering this, we can conclude that physics is playing a big part in this game, which is the main purpose of this numerical course.

### Application flow
Whole application is ran through the same window, while the elements of GUI are being removed and added for every fragment of it.  
First fragment being shown contains curling wallpaper and button for switching to next fragment.  
Second fragment contains 4 custom text areas for changing parameters of the game - mass, µ, number of rounds, number of stones. If user is satisfied with set values of parameters, game can be started by clicking on Start button.  
After that, the main fragment containing curling court and current score is shown. First user gets the green stone and he can launch it by clicking on the court with mouse. For aiming the direction of stone, there is a line that follows current position of mouse. After the click has happened, pop up for choosing the velocity of stone is displayed. When the current stone stops moving, the next stone is shown and game continues the way previously described.  
When both users have launched all stones they have, result of the round is being calculated and shown in next fragment. It also shows score in previous rounds and summed current score.  
For previously set number of rounds this flow is being repeated.  
When all rounds have been played, fragment with winner announcement and ending result is shown.  

### Physics in project
- _Oyler method_ is used for solving basic differential equation of motion - _dx/dt = v_. 
- _RK4N method_ is used for solving equation of Newton's 2nd law - _dv/dt = F/m_. 
- Equation used for calculating force value is _F = µmg_. 
- Detection of collision is being checked by comparing distances between elements. Mechanism of _sweep and prune_ is also used for collision detection, but it's main idea is to limit the number of pairs of solids that need to be checked for collision. 
- Motion after collision is determinated by the _law of conservation of energy_ and the _law of conservation of impulse_.

### Project structure
Project is divided into folders/packages with ``main.py`` module for running the application.

##### game package
Most important package of project contains:
- ``collisions.py`` - contains functions for checking collision and sweep and prune method
- ``Match.py`` - contains class ``Match.py`` which methods are used for representing score and winner at the end
- ``Parameters.py`` - contains class ``Parameters.py`` used for loading parameters selected by user (mass of stone, number of rounds...)
- ``Round.py`` - contains class ``Round.py`` with method ``run()`` displaying stones and their movement and calling helper functions for collisions, angle of stones... Other methods are showing current score and checking for end of the round and it's result.
- ``Stone.py`` - contains class ``Stone.py`` with methods calculating velocity of stone, it's position and angle after collision, distance from other stones and center.
##### gui package
Contains modules ``Button.py``, ``MainMenu.py``, ``Slider.py``, ``TextArea.py`` used for implementing GUI of application. 
Only ``Slider`` class is implemented through ``PyQt5`` library, while the other classes are implemented through _pygame_ library.
##### data package 
Consisting of images, mp3 files and fonts.
##### helper package
Contains two modules
- ``constants.py`` - declared parameters which affect motion, GUI parameters, colors, etc...
- ``methods.py`` - contains only _RK4N method_ 


### Libraries
Three main libraries are used in this project:
- ``pygame`` - used for application GUI 
- ``numpy``- used for RK4N method, array and vectors and everything that includes physics and motion
- ``PyQt5`` - used for implementing slider widget for choosing stone's velocity

### Imports and running the application
After creating of virtual environment, it is necessary to install libraries in terminal:
```sh
pip install pygame
```
```sh
pip install numpy
```
```sh
pip install pyqt5
```
When the requirements above are satisfied, application can be ran from ``main.py``. 

### Endnotes
This project was made in my second year of faculty during winter semestar. At that time I haven't been using git and GitHub and that is the reason why the first and only one commit consists the whole project.  
This project needs to be improved and things changed such as arhitecture and structure of code. There are some limitations that can be changed to make this application better.  
In future, I would like to include some AI code in this project. Right now, it's limited to only two humanic players without option for one to play against computer.  
Documentation in Serbian is placed in documentation folder.
