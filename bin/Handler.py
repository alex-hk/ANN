from Network import Network

filename = "../docs/optdigits_train.txt"
f = open(filename, "r")
line = f.readline()

numNeurons = raw_input("Neurons in hidden layer: ")

n = Network(numNeurons, 1, True)
n.setup(line)
print n
print
print len(n.ilayer)
print
print len(n.ilayer[0].weights)
print
print n.ilayer[0].weights
print

n.feedforward()

for ol in n.olayer:
    print ol.value
