# Python code to generate
# random numbers and random string
import random
import string

# JSON lib
import json

# Path lib
import os


class GenerateCity:

    # number of cities that we want to generate
    numberOfCities = 0

    # Create an empty dictionary of cities with his cordonnate
    citiesWithCoordonate = {}
    citiesWithCoordonate['cities'] = {}

    # length of name of different city
    numberOfLetterOfCity = 6

    def __init__(self, numberOfCities):
        self.numberOfCities = numberOfCities

    def __init__(self, numberOfCities, numberOfLetterOfCity):
        self.numberOfCities = numberOfCities
        self.numberOfLetterOfCity = numberOfLetterOfCity

    def __init__(self):
        self.numberOfCities = 0
        self.numberOfLetterOfCity = 0

    def setNumberOfCities(self, numberOfCities):
        self.numberOfCities = numberOfCities

    def setNumberOfLetterOfCity(self, numberOfLetterOfCity):
        self.numberOfLetterOfCity = numberOfLetterOfCity

    # Generate a random string of length which is pass
    def generateNameOfCity(self):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(self.numberOfLetterOfCity))

    def fillCitiesAndCoordonate(self):
        start = 0
        end = self.numberOfCities*4

        for i in range(self.numberOfCities):
            self.citiesWithCoordonate['cities'][str(i+1)] = {
                str('city'): self.generateNameOfCity(),
                str('coordinated'): (random.randint(start, end), random.randint(start, end))
            }

    def saveCitiesAndCoordonateToJsonFile(self, nameOfFile):
        fileName = str('dataset/cities/' + nameOfFile + '.json')

        with open(fileName, 'w') as outfile:
            json.dump(self.citiesWithCoordonate, outfile)
