# Python code to generate
# random numbers and random string
import random
import string

# JSON lib
import json

# Path lib
import os
import time

# Lib to show graph
import matplotlib.pyplot as plt
import numpy as np


class ShowGraph:

    def __init__(self):
        self.storageOfGraph = "./dataset/graphs"
        self.graphName = "graphStat"

    def display(self, abscisse, ordonne, labelX, labelY, title):
        try:
            plt.title(title)
            plt.xlabel(labelX)
            plt.ylabel(labelY)

            if not os.path.exists(self.storageOfGraph):
                os.makedirs(self.storageOfGraph)

            plt.plot(abscisse, ordonne,  'xb-')
            graphFileName = str(self.storageOfGraph +
                                "/" + self.graphName + str(time.monotonic_ns()) + '.png')
            plt.savefig(graphFileName)
            plt.show()

        except (OSError, IOError) as e:
            print("Error: " + str(e) + '!')
