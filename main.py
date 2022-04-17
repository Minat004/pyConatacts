import PySimpleGUI as sg

data_values = [[]]

layout = [
    [sg.Input(), sg.Button('Browse', key='-BROWSE-')],
    [sg.Input(), sg.Combo(['Name', 'Surname', 'Number'], default_value='Name'), sg.Button('Search', key='-SEARCH-')],
    [sg.Table(values=data_values)],
    [sg.Button('Add')],
    [sg.Button('Edit')],
    [sg.Button('Delete')],
]

sg.Window('Phone Book', layout).read()
