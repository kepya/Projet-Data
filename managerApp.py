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
    numberOfCities = 0
    numberOfTruck = 0
    numberOfLetterOfCity = 0
    numberOfObjetDeliverByTruck = 0
    numberOfEachObjetDeliverByTruck = 0
    cityFileName = ""

    def __init__(self, numberOfCities, numberOfTruck, numberOfLetterOfCity, numberOfObjetDeliverByTruck, numberOfEachObjetDeliverByTruck):
        self.numberOfCities = numberOfCities
        self.numberOfTruck = numberOfTruck
        self.numberOfLetterOfCity = numberOfLetterOfCity
        self.numberOfObjetDeliverByTruck = numberOfObjetDeliverByTruck
        self.numberOfEachObjetDeliverByTruck = numberOfEachObjetDeliverByTruck
        self.cityFileName = "./dataset/cities/test.json"

    def __init__(self):
        self.numberOfCities = 0
        self.numberOfTruck = 0
        self.numberOfLetterOfCity = 0
        self.numberOfObjetDeliverByTruck = 0
        self.numberOfEachObjetDeliverByTruck = 0
        self.cityFileName = "./dataset/cities/test.json"

    # Adds an instance variable
    def setNumberOfCities(self, numberOfCities):
        self.numberOfCities = numberOfCities

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

    def getCities(self):
        try:
            with open(self.cityFileName, encoding="utf8") as json_file:
                cityWithCoordonate = json.load(json_file)
            return cityWithCoordonate

        except (OSError, IOError) as e:
            print("Error: " + str(e) + '!')

    # return list of tour choose in the sequence of element, I use this to get a random random sampling without replacement.

    def generateTour(self, cities):
        try:
            lengthOfCity = len(cities['cities'])
            return random.sample(range(lengthOfCity), lengthOfCity)

        except (OSError, IOError) as e:
            print("Error: " + str(e) + '!')

    # this function is used to retreive the distance of the lowest tour that the vehicle realized
    def generateGoodTour(self, cities, nbrOfTour=10000):
        best_tour = self.generateTour(cities)
        lowest = self.distance(best_tour, cities)
        for _ in range(nbrOfTour):
            tour = self.generateTour(cities)
            dist = self.distance(tour, cities)
            if dist < lowest:
                lowest = dist
                best_tour = copy.copy(tour)

        print("Lowest tour has distance {}".format(lowest))
        return best_tour

    def array_part_loop(arr, start, end):
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

    def distance_between(tour, cities, i, j):
        city_count = len(cities)
        return sum([math.sqrt(sum([(cities[tour[(k+1) % city_count]][d] - cities[tour[k % city_count]][d])**2 for d in [0, 1]])) for k in [j, j-1, i, i-1]])

    # I used this function to get the distance between actual city ant the next city
    def distance_to_next(tour, cities, index):
        city_count = len(cities)
        return sum([math.sqrt(sum([(cities[tour[(k+1) % city_count]][d] - cities[tour[k % city_count]][d])**2 for d in [0, 1]])) for k in [index]])

    def distance(tour, cities):
        city_count = len(cities)
        return sum([math.sqrt(sum([(cities[tour[(k+1) % city_count]][d] - cities[tour[k % city_count]][d])**2 for d in [0, 1]])) for k in range(city_count)])

    def divideDeliveryBetweenTruck(self):
        cities = self.getcities['cities']()
        lengthOfCity = len(cities['cities'])
        tour = self.generateGoodTour(cities['cities'])

        tour_distance = distance(tour, cities['cities'])
        position_first_city = tour.index(0)
        position_relative_next_stop_city = 0
        initial_tour = copy.copy(tour)

        for truck in range(self.numberOfTruck-1):
            distance_cumulee = 0
            while distance_cumulee < (tour_distance / self.numberOfTruck):
                curr = initial_tour[(
                    position_first_city + position_relative_next_stop_city) % lengthOfCity]
                distance = self.distance_to_next(
                    initial_tour, cities['cities'], position_first_city + position_relative_next_stop_city)
                distance_cumulee += distance
                position_relative_next_stop_city += 1

            tour.insert(
                (position_first_city + position_relative_next_stop_city) % lengthOfCity, 0)

        if self.numberOfTruck > 1:
            # On insère le dernier tour
            zero_positions = [i for i, e in enumerate(tour) if e == 0]
            number_zeros = len(zero_positions)
            plt.clf()

            for zero_pos_i in range(len(zero_positions)):
                tour_start_index = zero_positions[zero_pos_i]
                tour_end_index = zero_positions[(
                    zero_pos_i + 1) % number_zeros]
                truck_tour = self.array_part_loop(
                    tour, tour_start_index, tour_end_index)
                truck_tour_len = len(truck_tour)

                cities['coordinated'][0] = [cities['coordinated'][truck_tour[i % truck_tour_len]][0]
                                            for i in range(truck_tour_len + 1)]
                cities['coordinated'][1] = [cities['coordinated'][truck_tour[i % truck_tour_len]][1]
                                            for i in range(truck_tour_len + 1)]
                plt.plot(cities['coordinated'][0],
                         cities['coordinated'][1], '-')

            plt.pause(0.1)

            while True:
                time.sleep(1)
