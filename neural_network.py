#!/usr/bin/env python

""" Neural network implemented with guidiance by the 
book "Make your own neural network" from Tariq Rashid."""

#import numpy as np
#import matplotlib.pyplot as plt

__author__ = "Manuel Aigner"
__copyright__ = ""
__credits__ = [""]
__license__ = ""
__version__ = "1.0.0"
__maintainer__ = "Manuel Aigner"
__email__ = "manuelaigner@gmx.de"
__status__ = "Development"


class NeuralNetwork:

    def __init__(self):
        self.activation_func = lambda x: x + 1

    def train(self):

        print(self.activation_func(2))


if __name__ == '__main__':
    network = NeuralNetwork()
    network.train()
