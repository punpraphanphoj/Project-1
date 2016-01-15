"""
Created on Thu Jan 14 16:02:20 2016

A3 Data statistics function

"""

import numpy as np
import math


def dataStatistics(data, statistics):
    
    if statistics == "Mean Temperature":
        temperature = data[:,0]
        result = np.mean(temperature)
    
    elif statistics == "Mean Growth rate":
        growthRate = data[:,1]
        result = np.mean(growthRate)
        
    elif statistics == "Std Temperature":
        stdTem = data[:,0]
        result = np.std(stdTem)
        
    elif statistics == "Std Growth rate":
        stdGrowthRate = data[:,1]
        result = np.std(stdGrowthRate)
        
    elif statistics == "Rows":
        row = np.size(data[:,0])
        result = row
        
    elif statistics == "Mean Cold Growth rate":
        tem = data[:,0]
        grow = data[:,1]
        totalsum = 0
        count = 0
        for i in range(np.size(data[:,0])):
            if tem[i] < 20:
                totalsum = totalsum + grow[i]
                count = count + 1
            else:
                print("Selected dataset does not contain temperature samples below 20°C")
        result = totalsum/count
        
    elif statistics == "Mean Hot Growth rate":
        tem = data[:,0]
        grow = data[:,1]
        totalsum = 0
        count = 0
        for i in range(np.size(data[:,0])):
            if tem[i] > 50:
                totalsum = totalsum + grow[i]
                count = count + 1
            else:
                print("Selected dataset does not contain temperature samples above 50°C")
        
        result = totalsum/count
    
    return result


#print(dataStatistics(dataLoad("test.txt"), "Mean Temperature"))
