import math
import matplotlib.pyplot as plt
import numpy as np
import random

weight = np.array([[0.1 , 0.2 , 0.3],
                 [0.4 , 0.5, 0.6],
                 [0.7, 0.8, 0.9],
                 [0.07, 0.09, 0.04]])


input=[2,9,10]

def sigmoid(x):
    item=x
    a=(1/(1+math.exp(-item)))
    return a

def neuron(inputs,weights):
 weighted_sum=0
 for i in range (0,len(input)):
    weighted_sum=weights[i]*inputs[i]+weighted_sum
 tr_function=sigmoid(weighted_sum)
 return tr_function


def layer(input,weights):
    o=[]
    for i in range (0,len(input)):
        y=neuron(input,weight[i])
        o.append(y)
    return(o)

layer_1_numbers=layer(input,weight)
print(layer_1_numbers)

def network (input,weights):
    d=[]
    #getting into each  layer one at a time
    for i in range (0,10):
        layer_i=layer(input,weights)
        input=layer_i
        #generating the outputs of each layer
        for i in range (0,len(layer_i)):
            y=layer_i[i]
            j=layer(input,weights)
            d.append(y)
    return(d)
 
print(network(input,weight))
