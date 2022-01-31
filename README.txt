README.txt


Particle.py:

Contains numerical methods needed for simulation to run within the main class "Particle"



TwoBodyTest.py:

One of the testing files. Simplified version of Particle and Simulation files joined together. 
Checks an interaction between two bodies where one is a lot more massive than the other (so that the more massive one can be assumed to be stationary). 
Simplified version of Particle and Simulation files joined together. Contains class "TwoParticlesTest", which in turn contains 
methods to update Earth's velocity, position and acceleration using three numerical methods mentioned above. 
It also contains initial conditions of two objects of class "TwoParticlesTest" (Earth and Sun) and when run plots Earth's x-y positions on a graph.


ConstantAParticle.py:

One of the testing files. When run plots an x-y graph of position of the "Ball" particle defined in the file.


Simulation.py:

Contains bodies of the system with their initial conditions (set to what those are on 1st of January 2020 according to Ephemeris).
Also contains a function allowing user to add up to three new bodies to the system through the terminal, code to allow user to specify 
the number of days the simulation will be run for and which numerical method will be used (choice between Euler, Euler-Cromer and Verlet).
Contains a loop which updates gravitational acceleration, velocity and position of the bodies throughout the period of time specified and
saves information about every day of the system to "Multiple Bodies" file.



XYPositionGraph.py:

When run, plots a graph of x-y position of every body in the system.


PrintData.py:

When run, prints values of position and velocity of every planet every day of the simulation



AngularMomentumDifference.py:

Contains a method which calculates the magnitude of angular momentum of the system at a given state of the system.
Then it calculates % difference between final and initial momentum, which is what its output is when run.



!In order to run any files apart from ConstantAParticle.py and TwoBodyTest.py, Simulation.py and Particle.py have to be opened as well!