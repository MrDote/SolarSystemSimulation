import numpy as np
import copy
from Particle import Particle


# initializing all initial bodies as objects of a Particle() class
Sun = Particle(
    position=np.array([-5.682653841092885e8, 1.112997165528592e9, 3.445256675517594e6]),
    velocity=np.array([-1.446153643855376e1, -3.447507130430867, 3.988611997595555e-1]),
    acceleration=np.array([0, 0, 0]),
    name="Sun",
    mass=1.989e30,
    color="y"
)


Earth = Particle(
    position=np.array([-2.545323708273825e10, 1.460913442868109e11, -2.726527903765440e6]),
    velocity=np.array([-2.986338200235307e4, -5.165822246700293e3, 1.135526860257752]),
    acceleration=np.array([0, 0, 0]),
    name="Earth",
    mass=5.972e24,
    color="b"
)


Mars = Particle(
    position=np.array([-1.980535522170065e11, -1.313944334060654e11, 2.072245594990239e9]),
    velocity=np.array([1.439273929359666e4, -1.805004074289640e4, -7.312485979614864e2]),
    acceleration=np.array([0, 0, 0]),
    name="Mars",
    mass=6.39e23,
    color="r"
)


Jupiter = Particle(
    position=np.array([7.814210740178683e10, -7.769489405106364e11, 1.474081608751178e9]),
    velocity=np.array([1.283931035247975e4, 1.930357070566108e3, -2.952599473712843e2]),
    acceleration=np.array([0, 0, 0]),
    name="Jupiter",
    mass=1.898e27,
    color="tab:brown"
)


Moon = Particle(
    position= np.array([-2.506305144417207e10, 1.459930035240048e11, -3.717618948633224e7]),
    velocity= np.array([-2.961465427844801e4, -4.230085049928977e3, -3.390576606358819e1]),
    acceleration=np.array([0, 0, 0]),
    name="Moon",
    mass=7.349e22,
    color="tab:gray"
)


Saturn = Particle(
    position= np.array([5.674914809473343e11, -1.388366463018738e12, 1.549265783457875e9]),
    velocity= np.array([8.406493531200095e3, 3.627774839464044e3, -3.983651341797232e2]),
    acceleration=np.array([0, 0, 0]),
    name="Saturn",
    mass=5.6834e26,
    color="tab:cyan"
)


Venus = Particle(
    position= np.array([1.076209595805564e11, 8.974122818036491e9, -6.131976661929069e9]),
    velocity= np.array([-2.693485084259549e3, 3.476650462014290e4, 6.320912271467272e2]),
    acceleration=np.array([0, 0, 0]),
    name="Venus",
    mass=4.8685e24,
    color="purple"
)


Mercury = Particle(
    position= np.array([-1.004302793346122e10, -6.782848247285485e10, -4.760889633162629e9]),
    velocity= np.array([3.847265155592926e4, -4.158689546981208e3, -3.869763647804497e3]),
    acceleration=np.array([0, 0, 0]),
    name="Mercury",
    mass=3.302e23,
    color="k"
)


bodies = [Sun, Earth, Mars, Jupiter, Moon, Saturn, Venus, Mercury]          # list of all the bodies of the system



def newObject():
    """This function allows the user to add up to 3 new bodies to the system
    It uses a while loop to check an input is an integer between 0 and 4 and
    takes in initial conditions supplied and initialises the new object
    """


    newObject1=0
    newObject2=0
    newObject3=0
    newObjectNames = [newObject1, newObject2, newObject3]
    
    howManyNewBodies = int(input("Enter the number of bodies you wish to add to the system (0-3):   "))

    while howManyNewBodies > 3 or howManyNewBodies < 0 or not type(howManyNewBodies) is int:
        howManyNewBodies = int(input("""Input has to be an integer between "1" and "4"! Try again!Enter the number of bodies you wish to add to the system (0-3):   """))
    for i in range(0, howManyNewBodies):
        newObjectNames[i] = Particle(
            position= np.array([input("Enter x-component of initial position:   "), input("Enter y-component of initial position:   "), input("Enter z-component of initial position:   ")], dtype=float),
            velocity= np.array([input("Enter x-component of initial velocity:   "), input("Enter y-component of initial velocity:   "), input("Enter z-component of initial velocity:   ")], dtype=float),
            acceleration=np.array([0, 0, 0], dtype=float),
            name=input("What do you want to name this body: "),
            mass=float(input("Enter mass of the body:   "))
            )
        bodies.append(newObjectNames[i])

newObject()


days = int(input("Enter the number of days (Starting date: 1st of January 2020):   "))          # takes in an input by user and stores it in variable "days"
while not days in range(1,36501):        # limit the type of input to integer and range to 100 years
    days = int(input("""Input has to be an integer between "1" and "36501"! Try again! Enter the number of days (Starting date: 1st of January 2020):      """))


secinday = 86400            # number of seconds in a day
deltaT = 720                   # time step in seconds
Data = []



numericalMethodNumber = int(input("""Which numerical method would you like to use? ["1" for Euler, "2" for Euler-Cromer, "3" for Verlet]:   """))          # takes in an input and stores it in a variable "numericalMethodNumber"
while not type(numericalMethodNumber) is int or not numericalMethodNumber in range(1,4):        # limit the range of input (1-3 allowed only)
    numericalMethodNumber = int(input("""Input has to be an integer between "1" and "3"! Try again! Which numerical method would you like to use? [Enter "1" for Euler, "2" for Euler-Cromer, "3" for Verlet.]:   """))


time = 1            # registers time in days starting from 1
timestep = 0

while timestep < int(days*secinday):            # loops through 
    for j in range(0, len(bodies)):             # loops through every object in "bodies"
            bodies[j].updateGravitationalAcceleration(bodies)
    for x in range(0, len(bodies)):
        if numericalMethodNumber == 1:
            bodies[x].eulerUpdatePositionVelocity(deltaT)       # Updates position and velocity of a planet using Euler method
        elif numericalMethodNumber == 2:
            bodies[x].eulerCromerUpdatePositionVelocity(deltaT)         # Updates position and velocity of a planet using Euler-Cromer method
        elif numericalMethodNumber == 3:
            bodies[x].verletUpdatePositionVelocity(deltaT)          # Updates position and velocity of a planet using Verlet method
        else:
            raise ValueError("Something's wrong")           # never meant to reach this point (2nd test on 0<y<4)




    if timestep % secinday == 0:                     #if timestep % (secinday) == 0:
        DataTime = []              # creating a new list (for easier access of specific data parts later)
        DataTime.append([time])            # adding time to the list
        time += 1
        
        for j in range(0, len(bodies)):
            DataTime.append([copy.deepcopy(bodies[j])])            # update DeepCopy for every day of the simulation
        
        Data.append(DataTime)          # merging lists with time and lists with planetary data
    timestep += deltaT

        

np.save("MultipleBodies", Data, allow_pickle=True)