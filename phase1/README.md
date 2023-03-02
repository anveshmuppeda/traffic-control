What is Q-learning?
# Objective:
RL Based traffic signal Controller to maximize the traffic flow in the network which minimizes the risk of the trafficjams.

Key Points
## Key Points
1. Sumo
2. Distributed Reinforcement Learning
3. QR

## Conclustion:
We simulate our algorithm using SUMO (Simulation of Urban MObility) on a real-world road network and compare it against the traditional Static Signalling (SS), Longest Queue First (LQF), and another RL-based approach of predictive n- step SARSA [1]. We evaluate these algorithms based on traffic parameters such as waiting time, queue length, and traffic dispersion time.

## Install Gitbash on Windows

## Install Linux on Windows with WSL.  
### Install WSL command.  
Open PowerShell or Windows Command Prompt in administrator mode by right-clicking and selecting "Run as administrator", enter.  
```wsl --install```  
This command will enable the features necessary to run WSL and install the Ubuntu distribution of Linux.  
The above command only works if WSL is not installed at all, if you run wsl --install and see the WSL help text, please try running wsl --list --online to see a list of available distros and run wsl --install -d <DistroName> to install a distro.  
  
### **Setup Linux Username and Password**
Once the process of installing your Linux distribution with WSL is complete, open the distribution (Ubuntu by default) using the Start menu. You will be asked to create a User Name and Password for your Linux distribution.   
  
  
## **SUMO Setup:**  
Install Python  
  ```sudo apt-get install python```  
Install git  
  ```sudo apt-get install git```  
Install cmake  
  ```sudo apt-get install cmake```  
Install g++  
  ```sudo apt-get install g++```  
Install lib dependecies  
  ```sudo apt-get install libxerces-c-dev libfox-1.6-dev libgdal-dev libproj-dev libgl2ps-dev swig default-jdk libeigen3-dev```  
Install maven  
  ```sudo apt-get install maven```  
Install python dependent versions  
  ```sudo apt-get install python3 python3-dev```  

Then clone the sumo code from the git  
  ```git clone --recursive https://github.com/eclipse/sumo```  
Then export the SUMO path  
 ```export SUMO_HOME="$PWD/sumo"```  
Create a directorires for cmake build  
  ```mkdir sumo/build/cmake-build && cd sumo/build/cmake-build```  
Then run the make files  
 ```cmake ../..```  
Execute the all the files  
 ```make -j$(nproc)``` 
 
 Installing required tools and libraries.  
 1. For the build infrastructure you will need cmake together with a moderately recent g++ (4.8 will do) or clang++ (or any other C++11 enabled compiler).   
 2. The library Xerces-C is always needed.   
 3. Optionally you may want to add.  
    ccache (to speed up builds).  
 4. ffmpeg-devel (for video output),   
    libOpenSceneGraph-devel (for the experimental 3D GUI),   
    gtest (for unit testing)  
    gettext (for internationalization)  
    texttest, xvfb and tkdiff (for the acceptance tests)  
    flake, astyle and autopep for style checking.  
 
 Install VS Code: It is a coding editor.
Steps to install VS Code:   
    1. Download it from "https://code.visualstudio.com/docs?dv=win".  
    2. Run the installer.  
    3. By default, it will be installed under "C:\Users\User_Name\AppData\Local\Programs\Microsoft VS Code" path.   
    4. If there are any errors in the installation check the path in the environment variables.   
### optional libraries and tools is:   
```
sudo apt-get install ccache libavformat-dev libswscale-dev libopenscenegraph-dev python3-pip python3-setuptools
sudo apt-get install libgtest-dev gettext tkdiff xvfb flake8 astyle python3-autopep8
pip3 install texttest
```
To install the most common dependencies with your package manager on ubuntu do:   
```sudo apt-get install python3-pandas python3-rtree python3-pyproj```

### Getting the source code.  
The following commands should be issued:   
```
git clone --recursive https://github.com/eclipse/sumo
cd sumo
git fetch origin refs/replace/*:refs/replace/*
pwd
```
#### Definition of SUMO_HOME
  ```export SUMO_HOME="/home/<user>/sumo-<version>"```.  
  You can check that SUMO_HOME was successfully set if you type.   
  ```echo $SUMO_HOME```.  
### Building the SUMO binaries with cmake.  
Create a build folder for cmake.   
```
mkdir build/cmake-build
cd build/cmake-build
cmake ../..
cmake -D CMAKE_BUILD_TYPE=Debug ../..
make -j $(nproc)
```
