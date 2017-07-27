import random

class Neuron(object):
    
    def __init__(self, numConnections, value):
        bias = 0
        self.weights = []
        self.numConnections = numConnections;
        self.value = value
        self.randWeights()

    def getWeight(self, index):
        if 0 <= index < len(self.weights):
            return self.weights[index]

    def randWeights(self):
        for i in range(0, self.numConnections):
            self.weights.append(random.uniform(0,1))




