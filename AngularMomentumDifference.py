from Simulation import *


def calculateAngularMomentum(bodiesList):
    """This method calculates magnitude of angular momentum of the system.
    An argument of this function is "bodiesList" which is a list containing the bodies of the system.
    Method extracts positions and velocities of bodies and applies formula for angular momentum (L=m*v*r).
    """
    L = 0

    for numberOfBodies in range(1, len(bodies)+1):
        LVector = 0
        L_Value = 0
        momentum = bodiesList[numberOfBodies][0].mass * bodiesList[numberOfBodies][0].velocity
        LVector = np.cross(bodiesList[numberOfBodies][0].position, momentum)

        for i in range(0, len(LVector)):
            L_Value += (LVector[i])**2
        L += L_Value

    return L**(1/2)




DataIn = np.load("MultipleBodies.npy", allow_pickle=True)



initialAngularMomentum = calculateAngularMomentum(DataIn[0])              # calculates final angular momentum using function "calculateAngularMomentum" and the first list of DataIn file

finalAngularMomentum = calculateAngularMomentum(DataIn[-1])



differenceInAngularMomentum = abs(finalAngularMomentum - initialAngularMomentum)            # calculates difference between initial and final angular momentum




percentageAngularMomentumDifference = (differenceInAngularMomentum / initialAngularMomentum) * 100              # calculates percentage difference in angular momentum


print("Initial and final momentum of the system differ by " + str(percentageAngularMomentumDifference) + "%" + " after " + str(days) + "days.")