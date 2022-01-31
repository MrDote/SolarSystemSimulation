import numpy as np
import copy


class TwoParticlesTest:
    import copy

    def __init__(self, position, velocity, acceleration, name, mass):
        self.position = np.array(position, dtype=float)
        self.velocity = np.array(velocity, dtype=float)
        self.acceleration = np.array(acceleration, dtype=float)
        self.name = np.array(name)
        self.mass = np.array(mass)
        self.G = 6.67408E-11
    

    def updateGravitationalAcceleration(self, body):
        self.acceleration = np.array([0.0, 0.0, 0.0])
        x_mag = 0
        r_xyz = self.position - body.position   #difference in x,y,z coordinates
        

        for j in range(0, len(r_xyz)):
            x_mag += (r_xyz[j])**(2)   #distance between object & body **2
        self.acceleration += -((self.G * body.mass/x_mag) * (r_xyz)/(x_mag)**(1/2))


    def eulerUpdatePositionVelocity(self, deltaT):
        self.position = self.position + self.velocity * deltaT
        self.velocity = self.velocity + self.acceleration * deltaT

    def eulerCromerUpdatePositionVelocity(self, deltaT):
        self.velocity = self.velocity + self.acceleration * deltaT
        self.position = self.position + self.velocity * deltaT





Earth = TwoParticlesTest(
    position=np.array([-2.545323708273825e10, 1.460913442868109e11, -2.726527903765440e6]),
    velocity=np.array([-2.986338200235307e4, -5.165822246700293e3, 1.135526860257752]),
    acceleration=np.array([0, 0, 0]),
    name="Earth",
    mass=5.972e24
)

Sun = TwoParticlesTest(
    position=np.array([-5.682653841092885e8, 1.112997165528592e9, 3.445256675517594e6]),
    velocity=np.array([-1.446153643855376e1, -3.447507130430867, 3.988611997595555e-1]),
    acceleration=np.array([0, 0, 0]),
    name="Sun",
    mass=1.989e30
)


Earth1 = copy.deepcopy(Earth)           # Earth's initial data copy for Euler-Cromer calculations
Earth2 = copy.deepcopy(Earth)           # Earth's initial data copy for initial momentum calculations

deltaT = 180
days = 365
secinday = 86400

xValues = []
yValues = []

for i in range(0, int(days*secinday), deltaT):      # updates velocity and position using Euler's method
    Earth.updateGravitationalAcceleration(Sun)
    Earth.eulerUpdatePositionVelocity(deltaT)
    xValues.append(Earth.position[0])
    yValues.append(Earth.position[1])

xValues1 = []
yValues1 = []

for i in range(0, int(days*secinday), deltaT):      # updates velocity and position using Euler-Cromer method
    Earth1.updateGravitationalAcceleration(Sun)
    Earth1.eulerCromerUpdatePositionVelocity(deltaT)
    xValues1.append(Earth1.position[0])
    yValues1.append(Earth1.position[1])


# calculates initial angular momentum of the system
LInit = 0
momentumInit = Earth2.mass * Earth2.velocity

LVectorInit = np.cross(Earth2.position, momentumInit)
for i in range(0, 3):
    LInit += (LVectorInit[i])**2
LInit = LInit**(1/2)



# calculates final angular momentum of the system
LFinal = 0
momentumFinal = Earth1.mass * Earth1.velocity

LVectorFinal = np.cross(Earth1.position, momentumFinal)
for i in range(0, 3):
    LFinal += (LVectorFinal[i])**2
LFinal = LFinal**(1/2)

print("Difference between final and initial momentum is " + str(abs((LFinal-LInit)/LInit)*100) + "%") # prints % difference between initial and final momentum




from matplotlib import pyplot as plt


plt.plot(xValues, yValues, linestyle="None", marker="o", markersize=0.6, color="r", label="Earth")
plt.plot(Sun.position[0], Sun.position[1], linestyle="None", marker="o", markersize=2, color="y", label="Sun")
plt.plot(xValues1, yValues1, linestyle="None", marker="o", markersize=0.6, color="k", label="Earth (Euler-Cromer)")



plt.xlabel("x")
plt.ylabel("y")


plt.legend(loc='upper right')
plt.show()
