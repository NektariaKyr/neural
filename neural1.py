import math
import matplotlib.pyplot as plt
import numpy as np
import random

weight_1=np.random.rand(4,3)
weight_2=np.random.rand(5,4)
weight_3=np.random.rand(4,3)
weight_4=np.random.rand(3,5)
weight=[weight_1,weight_2,weight_3,weight_4]
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
    out=[]
    for i in range (0,len(weights)):
        y=neuron(input,weights[i])
        out.append(y)
    return(out)

def network (input,weights_all):
    input=input
    #getting into each  layer one at a time
    for i in weights_all:
        layer_i=layer(input,i)
        print(layer_i)
        input=layer_i
 
y=network(input,weight)

