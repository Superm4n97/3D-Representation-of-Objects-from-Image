import math
def Case1(angP,angS,CameraDis): #angP<90 & angS<90
    if (angP>=angS):
        return -1 #invalid test case

    a = (CameraDis * math.tan(angP)) / (math.tan(angS) - math.tan(angP))
    r = (CameraDis + a) / (math.cos(angP))
    return r



def Case2(angP,angS,CameraDis): #angP<90 & angS=90
    #print("case2")
    r = CameraDis / math.cos(angP)
    return r



def Case3(angP,angS,CameraDis): #angP<90 & angS>90
    #print("case3")
    if angS >= math.pi:
        return -1 

    a = (CameraDis * math.tan(angP)) / (math.tan(math.pi - angS) + math.tan(angP))
    
    if a>CameraDis:
        return -1
    
    r = (CameraDis - a) / math.cos(angP)
    return r



def Case4(angP,angS,CameraDis): #angP=90 & angS>90
    #print("case4")
    if angS >= math.pi:
        return -1 

    r = (CameraDis * math.tan(math.pi - angS))
    return r



def Case5(angP,angS,CameraDis): #angP<90 & angS<90
    #print("case5")
    if angS>=math.pi or angP>=math.pi or angS<=angP:
        return -1
    
    a = (CameraDis * math.tan(math.pi - angP)) / (math.tan(math.pi - angP) - math.tan(math.pi - angS))
    
    if CameraDis >= a:
        return -1
    
    r = (a - CameraDis) / (math.cos(math.pi - angP))
    return r

def findZAxis(angV, half, r):
    if angV < half:
        return (r / math.tan(angV)) * (-1)
    elif angV == half:
        return 0
    else:
        return r / (math.tan(math.pi-angV))
    
def getZ(angV,r,halfOfpi):
    if angV == halfOfpi:
        return 0
    elif angV>halfOfpi:
        return r / (math.tan(halfOfpi - angV))
    else:
        return -(r / (math.tan(angV)))


def getCoordinate(angP,angS,angV,CameraDis,radian = True):
    invalid = -1
    roundingDigit = 3

    print("[VIRTICAL ANGLE]...")
    print(angV)

    if radian == False:
        angP = (angP*math.pi)/180.0
        angS = (angS*math.pi)/180.0
        angV = (angV*math.pi)/180.0

    angP = round(angP,roundingDigit)
    angS = round(angS,roundingDigit)
    angV = round(angV,roundingDigit)
    half = round(math.pi/2,roundingDigit)
    r = -1

    if angP<half and angS<half:
        r = Case1(angP,angS,CameraDis)
    elif angP<half and angS==half:
        r = Case2(angP,angS,CameraDis)
    elif angP<half and angS>half:
        r = Case3(angP,angS,CameraDis)
    elif angP==half and angS>half:
        r = Case4(angP,angS,CameraDis)
    elif angP>half and angS>half:
        r = Case5(angP,angS,CameraDis)
    
    if r == -1:
        return [invalid, invalid, invalid]
    
    X = round(r * math.cos(angP),roundingDigit)
    Y = round(r * math.sin(angP),roundingDigit)
    Z = round(getZ(angV, r, half), roundingDigit)

    print("[r]...")
    print(r)

    return [X,Y,Z]


"""
ag1 = math.acos(11.1/11.9)
ag2 = math.acos(3.1/5.1)
print(getCoordinate(ag1,ag2,ag1,8))

#ag2 = math.pi / 2
#ag2 = math.pi - math.acos(10/10.8)


#print(ag1)
#print(ag2)
ag1 = math.pi - math.acos(1.75/5)
ag2 = math.pi - math.acos(10.75/11.8)
print(getCoordinate(ag1,ag2,ag1,9))

"""