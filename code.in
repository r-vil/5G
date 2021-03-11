# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 18:23:29 2021

@author: GiulioCignoMembo
"""

import os

with open("./scenarios/data_scenarios_f_tokyo.in") as file: 

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
        b.append(line)

    # leggo le antenne
    a = []
    for i in range(0, m) : 
        
        line = file.readline().split()
        a.append(line)
    
    
# algoritmo
result = []
for i in range(0,m) :
    id_antenna = i
    x = b[i][0]
    y = b[i][1]
    
    result.append([id_antenna, x, y])
    
tot_antenna = m
    
print(result)

# output
with open("./example_f.in", "w+") as output :
    
    output.write(str(tot_antenna)+"\n")

    for item in result :
        output.write(str(item[0])+" "+str(item[1])+" "+str(item[2])+"\n")

