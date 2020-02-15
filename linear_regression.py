#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 10:52:27 2020

@author: arshad
"""

import numpy as np
import matplotlib.pyplot as plt
def hypothes_line(x,y,b):
    plt.scatter(x, y, color="red", marker="o", s=30)
    y_predected=b[0] + b[1]*x
    plt.plot(x, y_predected, color="g")

    plt.show()

def coffient(x,y):
    n=np.size(x)
    m_x=np.mean(x)
    m_y=np.mean(y)

    ss_xy=np.sum(x*y) - n*m_x*m_y
    ss_xx=np.sum(x*x) - n*m_x*m_x
    b_1=ss_xy/ss_xx
    b_0=m_y - b_1*m_x
    return (b_0,b_1)
def main():
    x=np.array([0,1,2,3,4,5,6,7,8,9])
    y=np.array([1,3,2,5,7,8,8,9,10,12])
    b=coffient(x,y)
    print("B0={0} and B1={1} are coeffients".format(b[0],b[1]))
    hypothes_line(x,y,b)

if __name__ == "__main__":
    main()