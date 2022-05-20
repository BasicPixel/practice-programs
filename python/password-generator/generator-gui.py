import PySimpleGUI as sg

layout = [
    [sg.Text("Password Generator")],
    [sg.Button('Generate a Password')]

]

window = sg.Window("Password Generator", layout)

event, values = window.read()
