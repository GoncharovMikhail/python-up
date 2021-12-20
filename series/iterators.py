import numpy as np


def multiply_coss(x_initial, iterations):
    product = 1.0
    for i in range(1, iterations+1):
        x_initial = x_initial/2
        product *= np.cos(x_initial)
    return product


def calcualte_up_x(x, iterations, iteartiion_M):
    up_x = 1/2
    for i in range(1, iterations+1):
        up_x += multiply_coss(i*np.pi/4, iteartiion_M)*np.cos(np.pi*i*x)
    return up_x