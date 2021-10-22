import matplotlib.pyplot as plt
import numpy as np
import os
 


with open('results/mapList.txt', 'r') as f:
    mapList = f.readlines() 
mapList = [line.rstrip('\n') for line in mapList]
mapList = list(map(float, mapList))



# MAP plotting
def mapPlot(list):
    plt.clf() 
    plt.title("MAP")####
    plt.plot(list)
    plt.xlabel("per 3 epoch")#####
    plt.ylabel("MAP")#####
    plt.grid(True)#####
    
    plt.savefig('results/이미지 map') ### 


def main():
    mapPlot(mapList)


if __name__ == "__main__":
    main()