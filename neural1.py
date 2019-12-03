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
output=np.random.rand(1,3)
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
        input=layer_i
 
y=network(input,weight)

def loss(x):
    f=0
    for i in x:
        f=f+i**2
    return f

def grad(x,e,fin):
    gr=[]
    list_high=[]
    list_low=[]
    for i in range(0,len(x)):
        x[i]=x[i]+e
        l_high=fin
        list_high.append(l_high)
        print(x)
        x[i]=x[i]-e
    for i in range(0,len(x)):
        x[i]=x[i]-e
        l_low=fin
        list_low.append(l_low)
        x[i]=x[i]+e
    for i in range(0,len(x)):
        gradient=(list_high[i]-list_low[i])/(2*e)
        gr.append(gradient)
    return gr

print(grad(input,0.01,loss(input)))
