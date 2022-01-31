from Simulation import *
from os import path

if path.exists("MultipleBodies.npy"):              # check if the file with data has been created
    print("The file MultipleBodies.npy has been created.")


DataIn = np.load("MultipleBodies.npy", allow_pickle=True)


def print_particle(particle):
    print("Particle: {}".format(particle.name))
    for attribute in ["position", "velocity"]:
        print("  {}: {}".format(attribute, particle.__getattribute__(attribute) + 0.0))  # add 0.0 to avoid negative zeros!



for i in range(0, len(DataIn)):
    print("{}".format(int(DataIn[i][0])))           # prints time from DataIn list
    for j in range(1, len(bodies)+1):               # +1 to account for time at the 0th position of DataIn list
        print_particle(DataIn[i][j][0])             # prints every planet's data from DataIn list