from matplotlib import markers
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

def createPlot(pointList):
    ax = plt.axes(projection = "3d")
    x = []
    y = []
    z = []

    allx = [0]
    ally = [0]
    allz = [0]

    ax.scatter3D([0],[0],[0],color = "red",marker = '^')
    #ax.scatter3D(x,y,z,color = "red")
    
    for point in pointList:
        x.append(point[0])
        y.append(point[1])
        z.append(point[2])

        allx.append(point[0])
        ally.append(point[1])
        allz.append(point[2])

    allx.append(0)
    ally.append(0)
    allz.append(0)
    """
    """

    

    ax.scatter3D(x,y,z,alpha = 0.8)
    ax.plot3D(allx,ally,allz,color = "green")
    plt.show()