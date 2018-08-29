import os
import point
import fileinput

def read_input(file_name):
    #fh = open(file_name)
    #lines = fh.readlines()
    lines = []
    for lin in fileinput.input(file_name):
        lines.append(lin)
    #
    np = int(lines[0].strip())
    points = []
    for i in range(np):
        line = lines[i+1]
        x,y,z = list(map(int,line.strip().split()))
        points.append(point.Point3D(i,x,y,z))
    #
    return points



