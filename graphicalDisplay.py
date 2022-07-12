from distutils.log import error
import os.path
from tkinter.ttk import Separator
import PySimpleGUI as sg
from numpy import size
from generateCity import GenerateCity
from managerApp import ManagerApp

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
        "Bell MT", 15)), sg.InputText(font=("Bell MT", 15), key='nberCity')],
    [sg.Text("How many letter the city name can take? ", font=(
        "Bell MT", 15)), sg.InputText(font=("Bell MT", 15), key='nberLetterCity')],
    [sg.Text("What are the different objet that you want to deliver ? ", font=("Bell MT", 15)),
     sg.Multiline(font=("Bell MT", 15))],
    [sg.Text("How many truck you want to used  to do this ? ", font=(
        "Bell MT", 15)), sg.InputText(font=("Bell MT", 15), key='numberOfTruck')],
    [sg.Text("how many objet the truck can take to deliver ? ",
             font=("Bell MT", 15)), sg.InputText(font=("Bell MT", 15), key='numberOfObjetDeliverByTruck')],
    [sg.Text("What quantity of each objet the truck can transport ? ", font=("Bell MT", 15)),
     sg.InputText(font=("Bell MT", 15), key='numberOfEachObjetDeliverByTruck')],
    [sg.Text("Generate file of cities with her coordonate", font=("Bell MT", 15)),
     sg.Button('Generate', font=("Bell MT", 15))],
    # [sg.Text("\n\n",)],
    [sg.Text("\n",)],

    [sg.Button('Validate', font=("Bell MT", 15))],
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

# Create an event loop
while True:
    event, values = window.read()
    manager = ManagerApp()
    generateCity = GenerateCity()

    # End program if user closes window or
    # presses the OK button
    if event == sg.WIN_CLOSED:
        break
    elif event == "choose":
        print('You entered ', values[0])
        try:
            option = int(values[0])

            if option == 1:
                window['errorChooseMenu'].Update(
                    "")
                window['rightLay'].Update(visible=True)
        except:
            window['errorChooseMenu'].Update(
                "Please enter number between 1 and 3")

    elif event == "Validate":
        if values["nberCity"] and values["numberOfEachObjetDeliverByTruck"] and values["nberLetterCity"] and values["numberOfObjetDeliverByTruck"] and values["numberOfTruck"]:
            try:
                manager.setNumberOfCities(int(values["nberCity"]))
                manager.setNumberOfEachObjetDeliverByTruck(
                    int(values["numberOfEachObjetDeliverByTruck"]))
                manager.setNumberOfLetterOfCity(int(values["nberLetterCity"]))
                manager.setNumberOfObjetDeliverByTruck(
                    int(values["numberOfObjetDeliverByTruck"]))
                manager.setNumberOfTruck(int(values["numberOfTruck"]))

                if hasGenerate == False:
                    generateCity.setNumberOfCities(int(values["nberCity"]))
                    generateCity.setNumberOfLetterOfCity(
                        int(values["nberLetterCity"]))
                    generateCity.generateNameOfCity()
                    generateCity.fillCitiesAndCoordonate()
                    filename = sg.PopupGetText(
                        "Enter name of file that we use to store cities with her cordonnate", font=("Bell MT", 15))
                    generateCity.saveCitiesAndCoordonateToJsonFile(filename)
                    sg.PopupAnimated('Cities generate',
                                     ' Cities generate succefully !!', font=("Bell MT", 15))
                    hasGenerate = True

                window['rightLay'].Update(visible=False)

            except:
                sg.PopupError(
                    'Error', 'please verify type of input', font=("Bell MT", 15))
        else:
            sg.PopupError(
                'Error', 'please fill input', font=("Bell MT", 15))
    elif event == "Close":
        window['rightLay'].Update(visible=False)

    elif event == "Generate":
        if values["nberCity"] and values["nberLetterCity"]:
            try:
                generateCity.setNumberOfCities(int(values["nberCity"]))
                generateCity.setNumberOfLetterOfCity(
                    int(values["nberLetterCity"]))
                generateCity.generateNameOfCity()
                generateCity.fillCitiesAndCoordonate()
                filename = sg.PopupGetText(
                    "Enter name of file that we use to store cities with her cordonnate", font=("Bell MT", 15))
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
