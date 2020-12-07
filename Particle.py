import numpy as np
import copy



class Particle:
    import copy

    def __init__(self, position, velocity, acceleration, name, mass):
        self.position = np.array(position, dtype=float)
        self.velocity = np.array(velocity, dtype=float)
        self.acceleration = np.array(acceleration, dtype=float)
        self.name = np.array(name)
        self.mass = np.array(mass)
        self.G = 6.67408E-11



    def __str__(self):
        return "Particle: {0}, Mass: {1:.3e}, Position: {2}, Velocity: {3}, Acceleration: {4}".format(self.name, self.mass,self.position, self.velocity, self.acceleration)

    def eulerUpdatePositionVelocity(self, deltaT):
        self.position = self.position + self.velocity * deltaT
        self.velocity = self.velocity + self.acceleration * deltaT

    def eulerCromerUpdatePositionVelocity(self, deltaT):
        self.velocity = self.velocity + self.acceleration * deltaT
        self.position = self.position + self.velocity * deltaT
    
    
    def verletUpdatePositionVelocity(self, deltaT):
        self.position = self.position + self.velocity * deltaT + 1/2 * self.accelerationInitial * (deltaT)**2
        self.velocity = self.velocity + 1/2 * (self.accelerationInitial + self.acceleration) * deltaT




    def updateGravitationalAcceleration(self, bodies):
        self.accelerationInitial = copy.deepcopy(self.acceleration)
        self.acceleration = np.array([0.0, 0.0, 0.0])
        for i in range(0, len(bodies)):

            if bodies[i].name != self.name:
                x_mag = 0
                r_xyz = self.position - bodies[i].position   #difference in x,y,z coordinates
                

                for j in range(0, len(r_xyz)):
                    x_mag += (r_xyz[j])**(2)   #distance between object & body **2
                self.acceleration += -((self.G * bodies[i].mass/x_mag) * (r_xyz)/(x_mag)**(1/2))



    def calculateKineticEnergy(self):
        return 1/2 * np.linalg.norm(self.mass) * np.linalg.norm(self.velocity)**2