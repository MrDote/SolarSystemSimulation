from Simulation import *
from os import path

def print_particle(particle):
    print("Particle: {}".format(particle.name))
    for attribute in ["position", "velocity"]:
        print("  {}: {}".format(attribute, particle.__getattribute__(attribute) + 0.0))  # add 0.0 to avoid negative zeros!


if path.exists("TwoBodyTest.npy"):
    print("The file TwoBodyTest.npy has been created.")


print("testing reading it back in")
DataIn = np.load("TwoBodyTest.npy", allow_pickle=True)




float_formatter = lambda x: "%.5e" % x
np.set_printoptions(formatter={'float_kind': float_formatter})



"""
for i in range(0, len(DataIn)):
    print("{}".format(int(DataIn[i][0])))  # time
    for j in range(1, len(bodies)):
        print_particle(DataIn[i][j][0])    # every planet's data
"""



from matplotlib import pyplot as plt
xValues = []
yValues = []
for i in range(0, len(DataIn)):
    for j in range(1, len(bodies)+1):
        xValues.append(DataIn[i][j][0].position[0])
        yValues.append(DataIn[i][j][0].position[1])


plt.plot(xValues, yValues, linestyle="None", marker="o", markersize=0.6)
plt.xlabel("x")
plt.ylabel("y")

plt.show()
# plt.legend()
