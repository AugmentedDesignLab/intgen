import math
import argparse
import re


def main():
    parser = argparse.ArgumentParser(description='Process intersection generation parameters')
    parser.add_argument("-in", "--incoming_roads", help="input number of incoming roads", type=int, default=3)
    parser.add_argument("-spx", "--spawn_pointx", help="intersection spawn point x coordinate", type=int, default=0)
    parser.add_argument("-spy", "--spawn_pointy", help="intersection spawn point y coordinate", type=int, default=0)
    parser.add_argument("-l", "--length", help="standard incoming road length", type=int, default=10)
    parser.add_argument("-o", "--output_file", help="output file name", default="output.txt")
    parser.add_argument("-multi", "--multilaned", nargs = '+', help="multilaned (4-6 lanes) roads (1,2,...) specification - example : road2laned4, road4laned6, etc.")
    args = parser.parse_args()
    print(generateroadpoints(args.output_file, args.incoming_roads, [args.spawn_pointx, args.spawn_pointy], args.length, args.multilaned))

def generateroadpoints(filename, n, centre, l, multilaned):
    file = open(filename, "w+")
    theta_unit = 360 / n
    i=0;
    laneParam = []
    roadNumber = []
    laneArgument = []
    while (i<len(multilaned)):
        roadNumber.append(int(multilaned[i][(multilaned[i].find('road')) + 4])) #Extracting road roadnumber
        laneParam.append(multilaned[i].find('laned'))
        laneArgument.append(multilaned[i][laneParam[i]:laneParam[i]+6]) #Extracting the 'lanedX' parameter
        i+=1
    i=0;
    for j in range(n):
        x, y = co_ordinate(l, j * theta_unit)
        if (j==(roadNumber[i]-1)):
            road = "(" + str(centre[0]) +", " + str(centre[1]) + ")" + "," + "(" + str(x) +", " + str(y) + ")" +",[],"+laneArgument[i]
            i+=1
        else:
            road = "(" + str(centre[0]) +", " + str(centre[1]) + ")" + "," + "(" + str(x) +", " + str(y) + ")" +",[]"
        file.write(road + "\n")
    # road1 = "(" + str(centre[0]) +", " + str(centre[1]) + ")" + "," + "(" + str(centre[0] - len) +", " + str(centre[1]) + ")" +",[]"
    # road2 = "(" + str(centre[0]) +", " + str(centre[1]) + ")" + "," + "(" + str(centre[0]) +", " + str(centre[1] + len) + ")" +",[]"
    # road3 = "(" + str(centre[0]) +", " + str(centre[1]) + ")" + "," + "(" + str(centre[0] + len) +", " + str(centre[1]) + ")" +",[]"
    return 0

def co_ordinate(len, angle):
    theta = math.radians(angle)
    x = len * math.cos(theta)
    y = len * math.sin(theta)
    #if x < 0.001:
    #    x = 0
    #if y < 0.001:
    #    y = 0
    return x, y


def line(p1, p2):
    A = (p1[1] - p2[1])
    B = (p2[0] - p1[0])
    C = (p1[0]*p2[1] - p2[0]*p1[1])
    return A, B, -C

def intersection(L1, L2):
    D  = L1[0] * L2[1] - L1[1] * L2[0]
    Dx = L1[2] * L2[1] - L1[1] * L2[2]
    Dy = L1[0] * L2[2] - L1[2] * L2[0]
    if D != 0:
        x = Dx / D
        y = Dy / D
        return x,y
    else:
        return False



# L1 = line([5,5], [0, 0])
# L2 = line([0,5], [5, 0])
# print(L1)
# print(L2)
# points = intersection(L1, L2)
# print(points)

if __name__=='__main__':
    main()
