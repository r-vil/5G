# -*- coding: utf-8 -*-

import os
import numpy
import math

scene = ["a_example", "b_mumbai", "c_metropolis", "d_polynesia", "e_sanfrancisco", "f_tokyo"]
for sth in range(len(scene)):
    with open("scenarios/data_scenarios_"+scene[sth] + ".in") as file: 

        # leggo width ed height 
        line = file.readline().split() 
        
        width = int(line[0])
        height = int(line[1])

        # leggo N, M, R
        line = file.readline().split() 
        
        n = int(line[0])
        m = int(line[1])
        r = int(line[2])
        
        # leggo i buildings
        b = [] 
        for i in range(0, n) : 
            
            line = file.readline().split()
            b.append([int(j) for j in line])

        # leggo le antenne
        a = []
        for i in range(0, m) : 
            
            line = file.readline().split()
            a.append(line)
        
        
    # algoritmo




    result = []

    for i in range(int(n/2) if (n/2 > m) else 0,(int(n/2) if (n/2 > m) else 0) + m) :

        id_antenna = i - (int(n/2) if (n/2 > m) else 0)
        x = b[i][0]
        y = b[i][1]


        
        result.append([id_antenna, x, y])
        
    tot_antenna = m
        

    # output
    with open("./output1/"+ scene[sth] + ".out", "w+") as output :
        
        output.write(str(tot_antenna)+"\n")

        for item in result :
            output.write(str(item[0])+" "+str(item[1])+" "+str(item[2])+"\n")

