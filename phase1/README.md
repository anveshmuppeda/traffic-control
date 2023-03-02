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

![image](https://user-images.githubusercontent.com/115966808/222545770-904120ca-f52f-4f14-9ea0-22d1b26d2658.png)


SUMO Setup:
Install Python  
  ```sudo apt-get install python```.  
Install git
  sudo apt-get install git
Install cmake
  sudo apt-get install cmake
Install g++
  sudo apt-get install g++
Install lib dependecies
  sudo apt-get install libxerces-c-dev libfox-1.6-dev libgdal-dev libproj-dev libgl2ps-dev swig default-jdk libeigen3-dev
Install maven
  sudo apt-get install maven
Install python dependent versions
  sudo apt-get install python3 python3-dev

Then clone the sumo code from the git
  git clone --recursive https://github.com/eclipse/sumo
Then export the SUMO path
 export SUMO_HOME="$PWD/sumo"
Create a directorires for cmake build
  mkdir sumo/build/cmake-build && cd sumo/build/cmake-build
Then run the make files
 cmake ../..
Execute the all the files
 make -j$(nproc)
