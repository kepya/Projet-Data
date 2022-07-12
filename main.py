from multiprocessing import Manager
from managerApp import ManagerApp

print("******************************************************************************************************************************************")
print("********************************************************Welcome to python program of group 2**********************************************")
print("******************************************************************************************************************************************")

print("A. Menu Group 2")
print("   1.  Set up environment")
print("   2.  Start generation of road")
print("   3.  View statistic result")
print("Choose your option")
option = input()

try:
    option = int(option)
except:
    print("Please enter number between 1 and 3")

if option == 1:
    print("How many cities do you enter ? ")
    numberOfCities = input()

    print(isinstance(numberOfCities, str))

    while isinstance(numberOfCities, str):
        try:
            numberOfCities = int(numberOfCities)
        except:
            print("Please enter a number")
            numberOfCities = input()

    manager = ManagerApp(numberOfCities)
    manager.defineCoordonateOfCities()
elif option == 2:
    print("Please enter number between 1 and 3")
else:
    print("")
