# AIR PRESSURE DROP CALCULATOR (apd calculator)

apd
: air pressure drop in pascal.

## Description

This small software allow you to calculate the air drop pressure in air duct network.
You can add multiple duct sections and configure each section with its own characteristics.
Air characteristics are configurable too.
See the user manual below.
<img src="./Readme%20visuals/mainwindow.PNG" height=420 alt="A software window"/>

### Aeraulic method of calculation
The calculations methods used in this software is strongly inspired by [COSTIC methods](https://www.costic.com).  
The formula used for the linear air pressure drop calculation is the [Colebrook equation](https://www.engineeringtoolbox.com/colebrook-equation-d_1031.html).

## Python version used
* Python 3.9
* pip 21.3.6

## Packages used (see requirement.txt)
* PySide6 (6.2.3)
* shiboken6 (6.2.3)

## How to launch
You must first create a virtual environment, activate it and install the necessary packages from the requirement file.
To launch the software type the following code in a terminal locate in the root folder of the project :
`python APDcalculator.py`
  
----
  
## User manual

### Main Window
Here let's see the main window interface.  
On the left, there is all the globals datas : air characteristics, totals additional apd and totals apd.
On the right, there is the management of duct sections : add, remove duct section and for each section the
characteristics adjusting.
![alt text][main window 01]  
Legend :
1. Air characteristics setting
2. Additionals apd (resume of duct sections additional apd + input a global additional apd)
3. Total air pressure drop of the air duc network
4. Duct sections management

### Duct section
The duct section management begin with one section set with defaults datas. Every new duct section will be set with the
sames default datas.  
![alt text][duct section window] ![alt text][rectangular case]  
Legend :
1. Buttons for add or remove a duc section8. Result of fmow speed in duct section
2. Choice of duc section shape
3. Choice of duct section material
4. Choice of diameter if shape is circular (in mm). displaying height and width inputs (in mm) if shape is rectangular.
5. Result of section of the duct (in m²)
6. Input for flow rate inside this duct section (in m³/h)
7. Input for linear duct section length (in m)
8. Result of flow speed in duct section (in m/s)
9. Result of the linear air pressure drop in this duct section (in Pa)
10. Button for displaying the singularities window
11. Table displaying the singularities already select in this duct section
12. Result of singular air pressure drop in this duct section (in Pa)
13. Input for adding an optional apd  

### Changing air characteristics
It is possible to change the air characteristics (temperature and altitude). These characteristics influence the results.  
By default, the temperature is set to 20°C and altitude is set to 0m below sea level.  
For changing the setting you have to tick the "change default datas" box. The temperature and altitude fields will be enabled.
![alt text][modif air]

### Adding singularities
For each duct section, different singularities could be added. The "add singularities" button open a window with the most
principals singularities for the duct shape chosen for the current duct section.
Just input the number of each singularity you want to add.  
![alt text][singularities window]  

The singularities chosen are postponed in the table of the current duct section. The result is added to the total results.
![alt text][singularities table]  

### Other screenshots
View with more than one duct section.  
![alt text][more duct section]

View with material choice.  
![alt text][material choice]


[main window 01]: ./Readme%20visuals/mainwindow01.png "A software window"
[duct section window]: ./Readme%20visuals/ductsectionwindow.png "A software window"
[rectangular case]: ./Readme%20visuals/rectangularcase.png "A software window"
[modif air]: ./Readme%20visuals/modifair.png "A software window"
[singularities window]: ./Readme%20visuals/singularitieswindow.png "A software window"
[singularities table]: ./Readme%20visuals/singularitiestable.png "A software window"
[more duct section]: ./Readme%20visuals/moreductsections.png "A software window"
[material choice]: ./Readme%20visuals/materials.png "A software window"


