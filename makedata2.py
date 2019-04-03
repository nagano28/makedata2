# -*- coding: utf-8 -*-
"""
Created on Mon Dec 04 19:20:19 2017

@author: Nagano Masatoshi
"""

import numpy as np
import matplotlib.pyplot as plt
#import random
data3 = []

def makedata():
    x = 0
    data0 = []
    data1 = []
    data2 = []
    data3 = []
    data3.append(0)
    a = 1
    d = 0
    
    #1
    b = np.random.randint(10,12)
    b1 = b
    for i in range(3):
        data0.append(0)
    while b > 0:
        data0.append(a)
        b = b - 1
    for i in range(3):
        data0.append(0)
    
    #0
    c = np.random.randint(10,14)
    c1 = c
    while c > 0:
        data1.append(d)
        c = c - 1
    
    
    #010
    e = np.random.randint(12,14)
    f = 1
    g = e/2
    yama = [0.125,0.25,0.375,0.5,0.625,0.75,0.875,1,0.875,0.75,0.625,0.5,0.375,0.25,0.125]
    for i in range(3):
        data0.append(0)
    while g > f:
        data2.append(d)
        f = f + 1
    for ii in range(len(yama)):
        data2.append(yama[ii])
    f = 1
    while g > f:
        data2.append(d)
        f = f + 1
    for i in range(3):
        data0.append(0)
    
    
    #mix
    #segm_min
    j = 0
    #segm_max
    y = 9
    while j < y:
        h = np.random.randint(1,4)
        if h == 1:
            data3 += data0
            x += b1
        elif h == 2:
            data3 += data1
            x += c1
        else:
            data3 += data2
            x += e
        j = j + 1

    #result
    k = range(len(data3))
    plt.plot(k,data3)
    plt.show()
    #save
    np.savetxt('data.txt',data3)


"""normalize
    means = np.mean( data3, 0 )
    maxvars = np.max( data3-means, 0 )
    new_data = []
    
    for i in range(len(data3)):
        data3[i] = (data3[i]-means)/maxvars
        #print data[0]
        new_data.append(data3[i]) 
    print new_data
    plt.plot(k,new_data)
    plt.show()
    np.savetxt('n015.txt',new_data)
"""

def main():
    makedata()
#    normalize()

if __name__ == '__main__':
    main()