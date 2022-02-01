import cv2 as cv
from numpy.lib.index_tricks import nd_grid
import objectCenters
import math
import DM1d
import plot

"""
Global Variables
"""
#horizontal and virtical angle covered by camera
viewingAngleHorizontal = 1.117
viewingAngleVartical = 0.866

totalPixelInX = 0
totalPixelInY = 0

cameraDistance = 89.6

#scalingSize = 0.27
scalingSize = 0.2

negotiableVarticalAngle = 5

"""
Functions
"""
#finds the angle of a point 
def getAngle(ax,ay):
    #initial_angle_horizontal = math.pi/2 - viewingAngleHorizontal/2
    #initial_angle_vartical = math.pi/2 - viewingAngleVartical/2
    initial_angle_horizontal = 0
    initial_angle_vartical = 0

    angH = initial_angle_horizontal + (viewingAngleHorizontal*ax) / totalPixelInY
    angV = initial_angle_vartical + (viewingAngleVartical*ay) / totalPixelInX
    #angV = (ay*viewingAngleVartical)/totalPixelInY
    #return (angH,angV)
    return (angV,angH)


def rescale(img,scale):
    h,w,_ = img.shape
    img = cv.resize(img,(int(w*scale),int(h*scale)))
    return img

def checkVarticalPixelsForPairing(a,b):
    if abs(a-b)<=negotiableVarticalAngle:
        return True
    return False

"""
Main Code
"""

primaryImage = cv.imread(r"F:\Projects\3D Representation\Resource\a1.jpg")
primaryImage = rescale(primaryImage,scalingSize)
totalPixelInX,totalPixelInY,_ = primaryImage.shape
print(totalPixelInX)
print(totalPixelInY)
primaryPoints = objectCenters.getCenterPoints(primaryImage)
for (x,y) in primaryPoints:
    cv.circle(primaryImage,(x,y),1,(0,255,0),thickness=5)
#cv.imshow("Primary",primaryImage)

seconndaryImage = cv.imread(r"F:\Projects\3D Representation\Resource\a2.jpg")
seconndaryImage = rescale(seconndaryImage,scalingSize)
Secondarypoints = objectCenters.getCenterPoints(seconndaryImage)
for (x,y) in Secondarypoints:
    cv.circle(seconndaryImage,(x,y),1,(0,0,255),thickness=5)
#vcv.imshow("Secondary",seconndaryImage)

cordinateList = []

for (px,py) in primaryPoints:
    (pax,pay) = getAngle(px,py)
    for (sx,sy) in Secondarypoints:
        if checkVarticalPixelsForPairing(py,sy) == False:
            continue
        (sax,say) = getAngle(sx,sy)
        cor = DM1d.getCoordinate(pax,sax,pay,cameraDistance)

        #invalid pair
        if cor[0]==-1 and cor[1] == -1 and cor[2] == -1: 
            continue

        print("[CURRENT PAIRS]....")
        print((pax,pay))
        print((sax,say))
        cordinateList.append(cor)
        print("[COORDINATE]...")
        print(cor[0])
        print(cor[1])
        print(cor[2])
        print("[DISTANCE FROM CAMERA]...")
        print(math.sqrt(cor[0]*cor[0] + cor[1]*cor[1] + cor[2]*cor[2]))

plot.createPlot(cordinateList)

cv.waitKey(0)
