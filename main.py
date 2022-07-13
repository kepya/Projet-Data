import os.path
import time
from tkinter.ttk import Separator
import PySimpleGUI as sg
from numpy import size
from generateCity import GenerateCity
from managerApp import ManagerApp
from statStudy import StatStudy

errorChooseMenu = ""
hasGenerate = False

leftLay = [
    [sg.Text("*********************************", font=("Bell MT", 20))],
    [sg.Text("Welcome to python program of group 2",
             font=("Bell MT", 20), text_color='Blue')],
    [sg.Text("*********************************", font=("Bell MT", 20))],
    [sg.Text("\n",  font=("Bell MT", 11))],
    [sg.Text("A. Menu of Group 2", font=("Bell MT", 15))],
    [sg.Text("\t1.  Set up environment", font=("Bell MT", 15))],
    [sg.Text("\t2.  Start generation of road", font=("Bell MT", 15))],
    [sg.Text("\t3.  View statistic result", font=("Bell MT", 15))],
    [sg.Text("Choose your option", font=("Bell MT", 15))],
    [sg.InputText(font=("Bell MT", 15)), sg.Button(
        'choose', font=("Bell MT", 15))],
    [sg.Text(errorChooseMenu, key='errorChooseMenu',
             font=("Bell MT", 15), text_color='red')],
]

rigthLay = [
    [sg.Text("How many cities do you want to travele ? ", font=(
        "Bell MT", 15)), sg.InputText(font=("Bell MT", 15), key='numberOfCities')],
    [sg.Text("How many letter the city name can take? ", font=(
        "Bell MT", 15)), sg.InputText(font=("Bell MT", 15), key='numberOfLetterOfCity')],
    [sg.Text("How many truck you want to used  to do this ? ", font=(
        "Bell MT", 15)), sg.InputText(font=("Bell MT", 15), key='numberOfTruck')],

    # [sg.Text("how many objet the truck can take to deliver ? ",
    #          font=("Bell MT", 15)), sg.InputText(font=("Bell MT", 15), key='numberOfObjetDeliverByTruck')],
    # [sg.Text("What are the different objet that you want to deliver ? ", font=("Bell MT", 15)),
    #  sg.Multiline(font=("Bell MT", 15))],
    # [sg.Text("What quantity of each objet the truck can transport ? ", font=("Bell MT", 15)),
    #  sg.InputText(font=("Bell MT", 15), key='numberOfEachObjetDeliverByTruck')],

    [sg.Text("How many iteration you want to do ? ", font=("Bell MT", 15)),
     sg.InputText(font=("Bell MT", 15), key='numberOfIteration')],
    [sg.Text("Generate file of cities with her coordonate", font=("Bell MT", 15)),
     sg.Button('Generate', font=("Bell MT", 15)), sg.Button('Use existed File', font=("Bell MT", 15))],
    # [sg.Text("\n\n",)],
    [sg.Text("\n",)],

    [sg.Button('Validate', font=("Bell MT", 15)),
     sg.Button('Reload data', font=("Bell MT", 15))],
    [sg.HSeparator()],
    [sg.Button('Close', font=("Bell MT", 15))]
]

layouts = [
    [sg.Column(leftLay, key='leftLay'),
     sg.VSeperator(),
     sg.Column(rigthLay, key='rightLay', visible=False, size=(700, 400))]
]

# Create the window
window = sg.Window("Big Data Project : Group 2", layouts)
manager = ManagerApp()
generateCity = GenerateCity()

# Début du comptage du temps d'exécution
startAppTime = time.time()
startTime = 0


def main():
    manager = ManagerApp()
    generateCity = GenerateCity()
    print("Start main")


# Create an event loop
while True:
    event, values = window.read()
    # manager = ManagerApp()
    # generateCity = GenerateCity()
    # showGraph = ShowGraph()
    cityFileName = "./dataset/cities/test.json"

    # End program if user closes window or
    # presses the OK button
    if event == sg.WIN_CLOSED:
        break
    elif event == "choose":
        try:
            option = int(values[0])
            print('You entered ', values[0])

            if option == 1:
                window['errorChooseMenu'].Update(
                    "")
                window['rightLay'].Update(visible=True)
                startTime = 0

            elif option == 2:
                startTime = time.time()
                # showGraph.display()
                # result = manager.divideDeliveryBetweenTruck()
                manager.divideDeliveryBetweenTruck()
                window['errorChooseMenu'].Update(
                    "")
        except (OSError, IOError) as e:
            print("Error: " + str(e) + '!')
            window['errorChooseMenu'].Update(
                "Please enter number between 1 and 3")

    elif event == "Validate":
        if values["numberOfCities"] and values["numberOfLetterOfCity"] and values["numberOfTruck"] and values["numberOfIteration"]:
            try:
                manager.setNumberOfCities(int(values["numberOfCities"]))
                manager.setNumberOfLetterOfCity(
                    int(values["numberOfLetterOfCity"]))
                manager.setNumberOfTruck(int(values["numberOfTruck"]))
                manager.setNumberOfIteration(int(values["numberOfIteration"]))

                # manager.setNumberOfObjetDeliverByTruck(
                #     int(values["numberOfObjetDeliverByTruck"]))
                # manager.setNumberOfEachObjetDeliverByTruck(
                #     int(values["numberOfEachObjetDeliverByTruck"]))

                if hasGenerate == False:
                    generateCity.setNumberOfCities(
                        int(values["numberOfCities"]))
                    generateCity.setNumberOfLetterOfCity(
                        int(values["numberOfLetterOfCity"]))
                    generateCity.generateNameOfCity()
                    generateCity.fillCitiesAndCoordonate()
                    filename = sg.PopupGetText(
                        "Enter name of file that we use to store cities with her cordonnate", font=("Bell MT", 15))
                    generateCity.saveCitiesAndCoordonateToJsonFile(filename)
                    manager.setCityFileName(
                        "./dataset/cities/" + filename + ".json")
                    cityFileName = "./dataset/cities/" + filename + ".json"
                    sg.PopupOK('Cities generate',
                               ' Cities generate succefully !!', font=("Bell MT", 15))
                    hasGenerate = True

                manager.saveData()

                if result:
                    sg.PopupOK('Config Save',
                               ' Config save succefully !!', font=("Bell MT", 15))
                else:
                    sg.PopupError(
                        'Error', 'save fail', font=("Bell MT", 15))

                window['rightLay'].Update(visible=False)

            except:
                sg.PopupError(
                    'Error', 'please verify type of input', font=("Bell MT", 15))
        else:
            sg.PopupError(
                'Error', 'please fill input', font=("Bell MT", 15))
    elif event == "Reload data":
        result = manager.loadData()
        window['numberOfIteration'].Update(
            manager.getNumberOfIteration())
        window['numberOfTruck'].Update(
            manager.getNumberOfTruck())
        window['numberOfLetterOfCity'].Update(
            manager.getNumberOfLetterOfCity())
        cityFileName = manager.getCityFileName()
        window['numberOfCities'].Update(
            manager.getNumberOfCities())

        if result:
            sg.PopupOK('Config Reload',
                       ' Config reload succefully !!', font=("Bell MT", 15))
        else:
            sg.PopupError(
                'Error', 'reload fail', font=("Bell MT", 15))

        # window['numberOfObjetDeliverByTruck'].Update(
        #     manager.getNumberOfObjetDeliverByTruck())
        # window['numberOfEachObjetDeliverByTruck'].Update(
        #     manager.getNumberOfEachObjetDeliverByTruck())

    elif event == "Close":
        window['rightLay'].Update(visible=False)

    elif event == "Use existed File":
        filename = sg.PopupGetText(
            "Enter name of file that we want to use to reload data", font=("Bell MT", 15))
        manager.setCityFileName("./dataset/cities/" + filename + ".json")
        cityFileName = "./dataset/cities/" + filename + ".json"

    elif event == "Generate":
        if values["numberOfCities"] and values["numberOfLetterOfCity"]:
            try:
                generateCity.setNumberOfCities(int(values["numberOfCities"]))
                generateCity.setNumberOfLetterOfCity(
                    int(values["numberOfLetterOfCity"]))
                generateCity.generateNameOfCity()
                generateCity.fillCitiesAndCoordonate()
                filename = sg.PopupGetText(
                    "Enter name of file that we use to store cities with her cordonnate", font=("Bell MT", 15))
                manager.setCityFileName(
                    "./dataset/cities/" + filename + ".json")
                cityFileName = "./dataset/cities/" + filename + ".json"

                generateCity.saveCitiesAndCoordonateToJsonFile(filename)
                sg.PopupOK('Cities generate',
                           ' Cities generate succefully !!', font=("Bell MT", 15))
                hasGenerate = True
            except:
                sg.PopupError(
                    'Error', 'please enter a number for number of cities and number of letter of city', font=("Bell MT", 15))

        else:
            sg.PopupError(
                'Error', 'please fill input for number of cities and number of letter of city', font=("Bell MT", 15))

window.close()
