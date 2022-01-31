import numpy as np
from matplotlib import pyplot as plt
import copy


class Particle:

    def __init__(self, position=np.array([0, 0, 0], dtype=float), velocity=np.array([0, 0, 0], dtype=float), acceleration=np.array([0, -10, 0], dtype=float), name='Ball', mass=1.0):
        self.position = np.array(position, dtype=float)
        self.velocity = np.array(velocity, dtype=float)
        self.acceleration = np.array(acceleration, dtype=float)
        self.name = np.array(name)
        self.mass = np.array(mass)



    def __str__(self):
        return "Particle: {0}, Mass: {1:.3e}, Position: {2}, Velocity: {3}, Acceleration: {4}".format(self.name, self.mass,self.position, self.velocity, self.acceleration)

    def updateEuler(self, deltaT):
        self.position = self.position + self.velocity * deltaT
        self.velocity = self.velocity + self.acceleration * deltaT

    def updateEulerCromer(self, deltaT):
        self.velocity = self.velocity + self.acceleration * deltaT
        self.position = self.position + self.velocity * deltaT

    

Ball = Particle(
    position=np.array([0, 0, 0]),
    velocity=np.array([1, 50, 0]),
    acceleration=np.array([0, -10, 0]),
    name="Ball",
    mass=1
)

BallInitial1 = copy.deepcopy(Ball)          # create 3 copies of initial conditions so that initial data is not changed when parameters are updated
BallInitial2 = copy.deepcopy(Ball)
BallInitial3 = copy.deepcopy(Ball)


deltaT = 0.5          # for Euler and Euler-Cromer methods
totalTime = 10          # total time of simulation


xValuesEuler = []
yValuesEuler = []


i = 0
while i < (totalTime + deltaT):         # loops through time
    xValuesEuler.append(BallInitial1.position[0])           # appends x-values
    yValuesEuler.append(BallInitial1.position[1])           # appends y-values
    BallInitial1.updateEuler(deltaT)            # updates position and velocity using Euler method
    i += deltaT




xValuesEulerCromer = []
yValuesEulerCromer = []


k = 0
while k < (totalTime + deltaT):         # loops through time
    xValuesEulerCromer.append(BallInitial2.position[0])         # appends x-values
    yValuesEulerCromer.append(BallInitial2.position[1])         # appends y-values
    BallInitial2.updateEulerCromer(deltaT)          # updates position and velocity using Euler method
    k += deltaT




time = np.linspace(0, BallInitial3.velocity[0] * totalTime, 1000)
yValueSuvat = 50 * time + 1/2 * BallInitial3.acceleration[1] * time**(2)



plt.plot(time, yValueSuvat, markersize=1, color="b", label="Suvat")         # plots x-y values for 
plt.plot(xValuesEuler, yValuesEuler, markersize=1, color="k", label="Euler")
plt.plot(xValuesEulerCromer, yValuesEulerCromer, markersize=1, color="r", label="Euler-Cromer")

plt.xlabel("x")
plt.ylabel("y")

plt.legend()
plt.show()