import numpy as np
import copy
from Particle import Particle


"""
def calculateInitialVelocity(largeBody, smallBody):
    positionMagnitude = 0
    for i in range(0, len(smallBody.position)):
            positionMagnitude += (smallBody.position[i])**(2)
    
    initialVelocity = np.sqrt(Earth.G * largeBody.mass / positionMagnitude**(1/2))
    return initialVelocity
"""


earthRadius = 6.371e6
sunRadius = 6.9634e8



Sun = Particle(
    position=np.array([-5.682653841092885e8, 1.112997165528592e9, 3.445256675517594e6]),
    velocity=np.array([-1.446153643855376e1, -3.447507130430867, 3.988611997595555e-1]),
    acceleration=np.array([0, 0, 0]),
    name="Sun",
    mass=1.989e30
)



Earth = Particle(
    position=np.array([-2.545323708273825e10, 1.460913442868109e11, -2.726527903765440e6]),
    velocity=np.array([-2.986338200235307e4, -5.165822246700293e3, 1.135526860257752]),
    acceleration=np.array([0, 0, 0]),
    name="Earth",
    mass=5.972e24
)


Mars = Particle(
    position=np.array([-1.980535522170065e11, -1.313944334060654e11, 2.072245594990239e9]),
    velocity=np.array([1.439273929359666e4, -1.805004074289640e4, -7.312485979614864e2]),
    acceleration=np.array([0, 0, 0]),
    name="Mars",
    mass=6.39e23
)


Jupiter = Particle(
    position=np.array([7.814210740178683e10, -7.769489405106364e11, 1.474081608751178e9]),
    velocity=np.array([1.283931035247975e4, 1.930357070566108e3, -2.952599473712843e2]),
    acceleration=np.array([0, 0, 0]),
    name="Jupiter",
    mass=1.898e27
)



Moon = Particle(
    position= np.array([-2.506305144417207e10, 1.459930035240048e11, -3.717618948633224e7]),
    velocity= np.array([-2.961465427844801e4, -4.230085049928977e3, -3.390576606358819e1]),
    acceleration=np.array([0, 0, 0]),
    name="Moon",
    mass=7.349e22 
)



Saturn = Particle(
    position= np.array([5.674914809473343e11, -1.388366463018738e12, 1.549265783457875e9]),
    velocity= np.array([8.406493531200095e3, 3.627774839464044e3, -3.983651341797232e2]),
    acceleration=np.array([0, 0, 0]),
    name="Saturn",
    mass=5.6834e26 
)



Venus = Particle(
    position= np.array([1.076209595805564e11, 8.974122818036491e9, -6.131976661929069e9]),
    velocity= np.array([-2.693485084259549e3, 3.476650462014290e4, 6.320912271467272e2]),
    acceleration=np.array([0, 0, 0]),
    name="Venus",
    mass=4.8685e24
)



Mercury = Particle(
    position= np.array([-1.004302793346122e10, -6.782848247285485e10, -4.760889633162629e9]),
    velocity= np.array([3.847265155592926e4, -4.158689546981208e3, -3.869763647804497e3]),
    acceleration=np.array([0, 0, 0]),
    name="Mercury",
    mass=3.302e23
)


bodies = [Sun, Earth, Mars, Jupiter, Moon, Saturn, Venus, Mercury]





def calculateAngularMomentum(bodies):   # check if angular momentum changes with time
        L = 0
        for i in range(0, len(bodies)):

            speed_squared = 0
            distance_squared = 0

            for j in range(0, len(bodies[i].velocity)):
                speed_squared += (bodies[i].velocity[j])**(2)
                distance_squared += (bodies[i].position[j])**(2)
                L += bodies[i].mass*(speed_squared)**(1/2)*(distance_squared)**(1/2)

        return L





days = int(input("Enter the number of days (Starting date: 1st of January 2020):   "))
deltaT = 3600
secinday = 86400
Data = []



y = int(input("""Which numerical method would you like to use? ["1" for Euler, "2" fof Euler-Cromer, "3" for Euler-Richardson.]:   """))
while y not in range(1,4):   # limit the range of input (1-3 allowed only)
    y = int(input("""Try again! Which numerical method would you like to use? [Enter "1" for Euler, "2" fof Euler-Cromer, "3" for Euler-Richardson.]:   """))


time = 1


for i in range(0, int(days*secinday), deltaT):
    for j in range(0, len(bodies)):
            bodies[j].updateGravitationalAcceleration(bodies)
    for x in range(0, len(bodies)):
        if y == 1:
            bodies[x].eulerUpdatePositionVelocity(deltaT)  # Updates position and velocity of a planet using Euler method
        elif y == 2:
            bodies[x].eulerCromerUpdatePositionVelocity(deltaT)
        elif y == 3:
            bodies[x].verletUpdatePositionVelocity(deltaT)



    if i % (secinday/6) == 0:   #update DeepCopy
        Data1 = []
        Data1.append([time])
        time += 1
        
        for j in range(0, len(bodies)):
            Data1.append([copy.deepcopy(bodies[j])])
        
        Data.append(Data1)
        

np.save("TwoBodyTest", Data, allow_pickle=True)