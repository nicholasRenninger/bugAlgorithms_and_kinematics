# Motion Planning - Bug Algorithms and Kinematics
*For optimal viewing of this document (and all `*.md` files), try opening it in a text editor that supports syntax highlighting for markdown `*.md` files (e.g. Sublime Text 2+).*

Implementation of Bug Algorithms and Basic Forwards / Inverse Kinematics Equations. Results of the implentation include:

* plots of the path performance of the different **bug planning algorithms** on multiple environments
* plots of the results of running **forwards / inverse kinematics on a user specified 2-link manipulator**

[Nicholas Rennninger](https://github.com/nicholasRenninger)

---

## How to Run the Code

This repository uses python 3, which is managed with an anaconda environment.

### Dependencies
In order to obtain all dependencies, you simply need to install anaconda for your OS, and then run from any shell with the `conda` command on its path:

`$(REPO_DIR_LOCATION) $ conda env create -f conda/environment.yml`


### Running the Source Code

To run the code:

* Activate the `conda` environment you just created in the "Dependencies" section:
`$(REPO_DIR_LOCATION) $ conda activate motionPlanning1`

* Run the main python module to run both the bug algorithms and kinematics codes:
`$(REPO_DIR_LOCATION) $ python main.py`


### Configuring the Code

#### Bug Algorithm Configuration
To change the scenarios for the bug algorithm code, simply modify one of the `$(REPO_DIR_LOCATION)/config/bug_scenarioX.yaml` files to create a new set of obstacles, or to change the location of the start / goal points.

#### Forwards / inverse Kinematics on a 2-link manipulator
To change the scenarios for the manipulator code, simply modify one of the `$(REPO_DIR_LOCATION)/config/manipulator_scenarioX.yaml` files to change the arm link lengths, the joint offset, the forward kinematics desired angle set, or the inverse kinematic desired end effector location.

---

## Results


### Bug1 Algorithm, Environment 1
<img src="https://github.com/nicholasRenninger/bugAlgorithms_and_kinematics/blob/master/figures/bug_scenario1-bug1.png" alt="Bug1 Algorithm, Environment 1"/>

### Bug2 Algorithm, Environment 1
<img src="https://github.com/nicholasRenninger/bugAlgorithms_and_kinematics/blob/master/figures/bug_scenario1-bug2.png" alt="Bug2 Algorithm, Environment 1"/>

### Bug1 Algorithm, Environment 2
<img src="https://github.com/nicholasRenninger/bugAlgorithms_and_kinematics/blob/master/figures/bug_scenario2-bug1.png" alt="Bug1 Algorithm, Environment 2"/>

### Bug2 Algorithm, Environment 2
<img src="https://github.com/nicholasRenninger/bugAlgorithms_and_kinematics/blob/master/figures/bug_scenario2-bug2.png" alt="Bug2 Algorithm, Environment 2"/>

### Forward Kinematics, Desired Angles = [pi/4, pi/2, -pi/6]
<img src="https://github.com/nicholasRenninger/bugAlgorithms_and_kinematics/blob/master/figures/manipulator_scenario1-forward_kin_0.785_1.57_-0.524.png" alt="Forward Kinematics"/>

### Inverse Kinematics, Desired End Effector Location = [0, 4]
<img src="https://github.com/nicholasRenninger/bugAlgorithms_and_kinematics/blob/master/figures/manipulator_scenario1-inverse_kin_0_4.png" alt="Inverse Kinematics"/>
