class ManagerApp:
    numberOfCities = 0
    numberOfTruck = 0
    numberOfLetterOfCity = 0
    numberOfObjetDeliverByTruck = 0
    numberOfEachObjetDeliverByTruck = 0

    def __init__(self, numberOfCities, numberOfTruck, numberOfLetterOfCity, numberOfObjetDeliverByTruck, numberOfEachObjetDeliverByTruck):
        self.numberOfCities = numberOfCities
        self.numberOfTruck = numberOfTruck
        self.numberOfLetterOfCity = numberOfLetterOfCity
        self.numberOfObjetDeliverByTruck = numberOfObjetDeliverByTruck
        self.numberOfEachObjetDeliverByTruck = numberOfEachObjetDeliverByTruck

    def __init__(self):
        self.numberOfCities = 0
        self.numberOfTruck = 0
        self.numberOfLetterOfCity = 0
        self.numberOfObjetDeliverByTruck = 0
        self.numberOfEachObjetDeliverByTruck = 0

    # Adds an instance variable
    def setNumberOfCities(self, numberOfCities):
        self.numberOfCities = numberOfCities

    def setNumberOfTruck(self, numberOfTruck):
        self.numberOfTruck = numberOfTruck

    def setNumberOfLetterOfCity(self, numberOfLetterOfCity):
        self.numberOfLetterOfCity = numberOfLetterOfCity

    def setNumberOfObjetDeliverByTruck(self, numberOfObjetDeliverByTruck):
        self.numberOfObjetDeliverByTruck = numberOfObjetDeliverByTruck

    def setNumberOfEachObjetDeliverByTruck(self, numberOfEachObjetDeliverByTruck):
        self.numberOfEachObjetDeliverByTruck = numberOfEachObjetDeliverByTruck
