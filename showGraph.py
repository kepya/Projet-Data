# Python code to generate
# random numbers and random string
import random
import string

# JSON lib
import json

# Path lib
import os

# Lib to show graph
import matplotlib.pyplot as plt
import numpy as np


class ShowGraph:
    fileOfCity = ""
    storageOfGraph = "dataset/graph"
    graphName = ""

    def __init__(self, fileOfCity):
        self.fileOfCity = fileOfCity

    def __init__(self, fileOfCity, storageOfGraph):
        self.fileOfCity = fileOfCity
        self.storageOfGraph = storageOfGraph

    def __init__(self, fileOfCity, storageOfGraph, graphName):
        self.fileOfCity = fileOfCity
        self.storageOfGraph = storageOfGraph
        self.graphName = graphName

    def __init__(self):
        self.fileOfCity = "./dataset/cities/test.json"
        self.storageOfGraph = "./dataset/graphs"
        self.graphName = "graph"

    def display(self):
        try:
            with open(self.fileOfCity, encoding="utf8") as json_file:
                cityWithCoordonate = json.load(json_file)

                GraphX = []
                GraphY = []

                for cityIndex in cityWithCoordonate['cities']:
                    city = cityWithCoordonate['cities'][cityIndex]

                    plt.scatter(city['coordinated'][0],
                                city['coordinated'][1], marker='o')
                    plt.annotate(
                        cityIndex, (city['coordinated'][0], city['coordinated'][1]))

                    GraphX.append(city['coordinated'][0])
                    GraphY.append(city['coordinated'][1])

                    if(int(cityIndex) == int(len(cityWithCoordonate['cities']))):
                        GraphX.append(
                            cityWithCoordonate['cities']['1']['coordinated'][0])
                        GraphY.append(
                            cityWithCoordonate['cities']['1']['coordinated'][1])

            plt.title('Representation of the tour with Matplotlib')
            plt.xlabel('x')
            plt.ylabel('y')

            if not os.path.exists(self.storageOfGraph):
                os.makedirs(self.storageOfGraph)

            plt.plot(GraphX, GraphY)
            graphFileName = str(self.storageOfGraph +
                                "/" + self.graphName + '.png')
            plt.savefig(graphFileName)
            plt.show()

        except (OSError, IOError) as e:
            print("Error: " + str(e) + '!')
