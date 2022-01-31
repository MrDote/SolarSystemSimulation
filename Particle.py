import numpy as np
import copy

class Particle:

    def __init__(self, position, velocity, acceleration, name, mass, color = "r"):
        """This method makes initial conditions an array of type float
           and is used in initialisation of every particle
        """
        self.position = np.array(position, dtype=float)
        self.velocity = np.array(velocity, dtype=float)
        self.acceleration = np.array(acceleration, dtype=float)
        self.name = np.array(name)
        self.mass = np.array(mass)
        self.color = color
        self.G = 6.67408E-11



    def eulerUpdatePositionVelocity(self, deltaT):
        """This method updates components of position and velocity using Euler method
        """
        self.position = self.position + self.velocity * deltaT
        self.velocity = self.velocity + self.acceleration * deltaT

    def eulerCromerUpdatePositionVelocity(self, deltaT):
        """This method updates components of position and velocity using Euler-Cromer method
        """
        self.velocity = self.velocity + self.acceleration * deltaT
        self.position = self.position + self.velocity * deltaT
    
    
    def verletUpdatePositionVelocity(self, deltaT):
        """This method updates components of position and velocity of a body using Verlet method
        """
        self.position = self.position + self.velocity * deltaT + 1/2 * self.accelerationInitial * (deltaT)**2
        self.velocity = self.velocity + 1/2 * (self.accelerationInitial + self.acceleration) * deltaT




    def updateGravitationalAcceleration(self, bodies):
        """This method updates gravitational acceleration of a body using 
        """
        self.accelerationInitial = copy.deepcopy(self.acceleration)
        self.acceleration = np.array([0.0, 0.0, 0.0])
        for i in range(0, len(bodies)):         # loops through all the bodies of the system

            if bodies[i].name != self.name:         # make sure acceleration of a body is updated only with respect to other bodies and not itself
                magnitudeOfPositionVector = 0
                differenceInCoordinates = self.position - bodies[i].position          #difference in x,y,z coordinates
                

                for j in range(0, len(differenceInCoordinates)):            
                    magnitudeOfPositionVector += (differenceInCoordinates[j])**(2)            #distance between object & body squared
                self.acceleration += -((self.G * bodies[i].mass/magnitudeOfPositionVector) * (differenceInCoordinates)/(magnitudeOfPositionVector)**(1/2))          # changes values of acceleration to calculated ones