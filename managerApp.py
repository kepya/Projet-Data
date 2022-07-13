# Python code to generate
# random numbers and random string
import copy
import math
import random
import string

# JSON lib
import json

# Lib to show graph
import matplotlib.pyplot as plt
import numpy as np
import time


class ManagerApp:
    # numberOfCities = 0
    # numberOfTruck = 0
    # numberOfIteration = 0
    # numberOfLetterOfCity = 0
    # numberOfObjetDeliverByTruck = 0
    # numberOfEachObjetDeliverByTruck = 0
    # cityFileName = ""
    # loadFile = "./dataset/load.json"

    def __init__(self, numberOfCities, numberOfTruck, numberOfLetterOfCity, numberOfObjetDeliverByTruck, numberOfEachObjetDeliverByTruck):
        self.numberOfCities = numberOfCities
        self.numberOfTruck = numberOfTruck
        self.numberOfIteration = 1
        self.numberOfLetterOfCity = numberOfLetterOfCity
        self.numberOfObjetDeliverByTruck = numberOfObjetDeliverByTruck
        self.numberOfEachObjetDeliverByTruck = numberOfEachObjetDeliverByTruck
        self.cityFileName = "./dataset/cities/test.json"
        self.loadFile = "./dataset/load.json"

    def __init__(self):
        self.numberOfCities = 0
        self.numberOfTruck = 0
        self.numberOfLetterOfCity = 0
        self.numberOfObjetDeliverByTruck = 0
        self.numberOfEachObjetDeliverByTruck = 0
        self.numberOfIteration = 1
        self.cityFileName = "./dataset/cities/test.json"
        self.loadFile = "./dataset/load.json"

    def loadData(self):
        try:
            with open(self.loadFile, encoding="utf8") as json_file:
                data = json.load(json_file)

                self.numberOfCities = int(data['numberOfCities'])
                self.numberOfTruck = int(data['numberOfTruck'])
                self.numberOfLetterOfCity = int(data['numberOfLetterOfCity'])
                self.numberOfIteration = int(data['numberOfIteration'])
                self.cityFileName = data['cityFileName']

                # self.numberOfObjetDeliverByTruck = int(
                #     data['numberOfObjetDeliverByTruck'])
                # self.numberOfEachObjetDeliverByTruck = int(
                #     data['numberOfEachObjetDeliverByTruck'])
            return True

        except(OSError, IOError) as e:
            print("Error: " + str(e) + '!')
            return False

    def saveData(self):
        try:
            data = {}
            data['numberOfCities'] = self.numberOfCities
            data['numberOfTruck'] = self.numberOfTruck
            data['numberOfLetterOfCity'] = self.numberOfLetterOfCity
            data['numberOfIteration'] = self.numberOfIteration
            data['cityFileName'] = self.cityFileName

            # data['numberOfObjetDeliverByTruck'] = self.numberOfObjetDeliverByTruck
            # data['numberOfEachObjetDeliverByTruck'] = self.numberOfEachObjetDeliverByTruck

            with open(self.loadFile, 'w') as outfile:
                json.dump(data, outfile)

            return True
        except(OSError, IOError) as e:
            print("Error: " + str(e) + '!')
            return False

    # Adds an instance variable

    def setNumberOfCities(self, numberOfCities):
        self.numberOfCities = numberOfCities

    def setNumberOfIteration(self, numberOfIteration):
        self.numberOfIteration = numberOfIteration

    def setCityFileName(self, cityFileName):
        self.cityFileName = cityFileName

    def setNumberOfTruck(self, numberOfTruck):
        self.numberOfTruck = numberOfTruck

    def setNumberOfLetterOfCity(self, numberOfLetterOfCity):
        self.numberOfLetterOfCity = numberOfLetterOfCity

    def setNumberOfObjetDeliverByTruck(self, numberOfObjetDeliverByTruck):
        self.numberOfObjetDeliverByTruck = numberOfObjetDeliverByTruck

    def setNumberOfEachObjetDeliverByTruck(self, numberOfEachObjetDeliverByTruck):
        self.numberOfEachObjetDeliverByTruck = numberOfEachObjetDeliverByTruck

    def getNumberOfCities(self):
        return self.numberOfCities

    def getCityFileName(self):
        return self.cityFileName

    def getNumberOfTruck(self):
        return self.numberOfTruck

    def getNumberOfLetterOfCity(self):
        return self.numberOfLetterOfCity

    def getNumberOfObjetDeliverByTruck(self):
        return self.numberOfObjetDeliverByTruck

    def getNumberOfEachObjetDeliverByTruck(self):
        return self.numberOfEachObjetDeliverByTruck

    def getNumberOfIteration(self):
        return self.numberOfIteration

    def getCities(self):
        try:
            with open(self.cityFileName, encoding="utf8") as json_file:
                cityWithCoordonate = json.load(json_file)

        except (OSError, IOError) as e:
            print("Error: " + str(e) + '!')

        return cityWithCoordonate

    def getCoordonateOfData(self, cities):
        lengthOfCity = int(len(cities))

        col = []
        for j in range(lengthOfCity):
            col.append(cities[str(j + 1)]["coordinated"])
        # print(col)

        return col

    def distance_between(self, tour, cities, i, j):
        lengthOfCity = int(len(cities))
        cordonnate = self.getCoordonateOfData(cities)
        return sum([math.sqrt(sum([(cordonnate[tour[(k+1) % lengthOfCity]][d] - cordonnate[tour[k % lengthOfCity]][d])**2 for d in [0, 1]])) for k in [j, j-1, i, i-1]])

    # I used this function to get the distance between actual city ant the next city
    def distance_to_next(self, tour, cities, index):
        lengthOfCity = int(len(cities))
        cordonnate = self.getCoordonateOfData(cities)
        return sum([math.sqrt(sum([(cordonnate[tour[(k+1) % lengthOfCity]][d] - cordonnate[tour[k % lengthOfCity]][d])**2 for d in [0, 1]])) for k in [index]])

    def distance(self, tour, cities):
        cordonnate = self.getCoordonateOfData(cities)
        lengthOfCity = int(len(cities))

        return sum([math.sqrt(
            sum([(cordonnate[tour[(k+1) % lengthOfCity]][d] -
                    cordonnate[tour[k % lengthOfCity]][d])**2 for d in [0, 1]])
        ) for k in range(lengthOfCity)])

    # return list of tour choose in the sequence of element, I use this to get a random random sampling without replacement.

    def generateTour(self, cities):
        try:
            lengthOfCity = int(len(cities))
            return random.sample(range(lengthOfCity), lengthOfCity)

        except (OSError, IOError) as e:
            print("Error: " + str(e) + '!')

    # this function is used to retreive the distance of the lowest tour that the vehicle realized
    def generateGoodTour(self, cities, nbrOfTour):
        best_tour = self.generateTour(cities)
        lowest = self.distance(best_tour, cities)
        print('\n')

        for i in range(nbrOfTour):
            tour = self.generateTour(cities)
            dist = self.distance(tour, cities)
            print('tour : ', tour)
            print('distance : ', dist)
            print('\n')
            if dist < lowest:
                lowest = dist
                best_tour = copy.copy(tour)

        print("Lowest tour has distance {}".format(lowest))
        print("Lowest tour is : ", best_tour)
        print('\n')
        return best_tour

    def getArrayByLoop(self, arr, start, end):
        print('laoo')
        arr_len = len(arr)
        ret = []

        if start > end:
            nb_elements = arr_len - start
            nb_elements += end
        else:
            return arr[start:(end + 1) % arr_len]

        for i in range(nb_elements):
            ret.append(arr[(start + i) % arr_len])

        ret.append(arr[(start + nb_elements) % arr_len])
        return ret

    # I used this function to get the distance between two cities at a specific index
    def divideDeliveryBetweenTruck(self):
        cities = self.getCities()

        lengthOfCity = int(len(cities['cities']))
        tour = self.generateGoodTour(
            cities['cities'], self.getNumberOfIteration())

        tour_distance = self.distance(tour, cities['cities'])

        position_first_city = tour.index(0)
        position_relative_next_stop_city = 0
        initial_tour = copy.copy(tour)

        for truck in range(self.getNumberOfTruck()-1):
            distance_cumulee = 0
            while distance_cumulee < (tour_distance / self.getNumberOfTruck()):
                curr = initial_tour[(
                    position_first_city + position_relative_next_stop_city) % lengthOfCity]
                distance = self.distance_to_next(
                    initial_tour, cities['cities'], position_first_city + position_relative_next_stop_city)
                distance_cumulee += distance
                position_relative_next_stop_city += 1

            tour.insert(
                (position_first_city + position_relative_next_stop_city) % lengthOfCity, 0)

        if self.getNumberOfTruck() > 1:
            # On insère le dernier tour
            zero_positions = [i for i, e in enumerate(tour) if e == 0]
            number_zeros = int(len(zero_positions))
            plt.clf()

            for zero_pos_i in range(number_zeros):
                tour_start_index = zero_positions[zero_pos_i]
                tour_end_index = zero_positions[(
                    zero_pos_i + 1) % number_zeros]
                truck_tour = self.getArrayByLoop(
                    tour, tour_start_index, tour_end_index)
                truck_tour_len = int(len(truck_tour))

        print("pyuy oo *** yes")
        cities['coordinated'][0] = [cities['coordinated'][truck_tour[i % truck_tour_len]][0]
                                    for i in range(truck_tour_len + 1)]
        cities['coordinated'][1] = [cities['coordinated'][truck_tour[i % truck_tour_len]][1]
                                    for i in range(truck_tour_len + 1)]
        plt.plot(cities['coordinated'][0],
                 cities['coordinated'][1], '-')

        plt.pause(0.1)

        while True:
            time.sleep(1)
