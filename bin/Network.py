import math
from Neuron import Neuron
from random import random

class Network():

    def __init__(self, nline, numlayers=1, training = False):
        self.trainactual = 0
        self.linedata = []
    
        self.hlayers = []
        self.ilayer = []
        self.olayer = []

        self.layers = []

        if numlayers < 1:
            self.numlayers = 1
        else:
            self.numlayers = numlayers
        self.training = training
        self.nneurons = nline.split()

    def setup(self, line):
        self.linedata = line.split(",")
        if self.training:
            self.trainactual = int(self.linedata[64])
        self.setupLayers()

    def setupLayers(self):
        '''Setup for input layer'''
        for ii in range(0, 64):
            self.ilayer.append(Neuron(int(self.nneurons[0]), int(self.linedata[ii])))
        self.layers.append(self.ilayer)

        '''Setup for n hidden layers'''
        for i in range(0,self.numlayers):
            hl = []
            
            for nnons in range(0, int(self.nneurons[i])):
                if i+1 < len(self.nneurons):
                    ncount = self.nneurons[nnons+1]
                else:
                    ncount = 10
                hl.append(Neuron(ncount,0))
            
            self.layers.append(hl)
                
        '''Setup for output layer'''
        for j in range(0,10):
            self.olayer.append(Neuron(0,0))

        self.layers.append(self.olayer)


    
    def run(self, train = True):
        return

    def feedforward(self):
        for i in range(0, len(self.layers)):
            if i+1 < (len(self.layers)):
                for nni in range(0,len(self.layers[i+1])):
                    for pneuron in self.layers[i]:
                        print pneuron
                        self.layers[i+1][nni].value += pneuron.weights[nni] * pneuron.value
                    print
                    self.layers[i+1][nni] = self.sigmoid(self.layers[i+1][nni].value)



    def backprop(self):
        for layer in reversed(range(len(self.layers))):
            error = (self.trainactual - self.olayer.value) * dsigmoid(self.olayer.value)

        return

    def sigmoid(self, z):
        return ( 1.0 / (1.0 + math.exp(-z)))

    def dsigmoid(self, sigz):
        return sigz * (1.0 - sigz)
