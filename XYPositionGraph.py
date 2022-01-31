from Simulation import *
from os import path
from matplotlib import pyplot as plt


if path.exists("MultipleBodies.npy"):              # check if the file with data has been created
    print("The file MultipleBodies.npy has been created.")


DataIn = np.load("MultipleBodies.npy", allow_pickle=True)           # load the file with data



for i in range(0, len(DataIn)):         
    for j in range(1, len(bodies)+1):           # +1 to account for time at the 0th position of DataIn list
        if i == 0:             # makes sure legend is only printed once
            plt.plot(DataIn[i][j][0].position[0], DataIn[i][j][0].position[1], linestyle="None", marker="o", markersize=0.6, color=bodies[j-1].color, label=bodies[j-1].name)
        else:
            plt.plot(DataIn[i][j][0].position[0], DataIn[i][j][0].position[1], linestyle="None", marker="o", markersize=0.6, color=bodies[j-1].color)           # ploting a graph of x,y positions of all planets



plt.xlabel("x")             # labels x-axis of the graph
plt.ylabel("y")             # labels y-axis of the graph

plt.legend(loc='upper right')            # displays the legend
plt.show()                               # displays the graph