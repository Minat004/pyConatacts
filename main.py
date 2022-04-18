import PySimpleGUI as sg

data_values = [
    ['Alex', 'Bell', 578364303],
    ['Masha', 'Bell', 578364304],
]
header = ['qwerty', 'asdfgh', 'zxcvbn']


def create_main_window():
    layout = [
        [sg.Input(), sg.Button('Browse', key='-BROWSE-', expand_x=True)],
        [
            sg.Input(),
            sg.Combo(['Name', 'Surname', 'Number'], default_value='Name'),
            sg.Button('Search', key='-SEARCH-')
        ],
        [sg.Table(values=data_values, headings=header, justification='left', expand_x=True)],
        [
            sg.Button('Add', key='-ADD-', expand_x=True),
            sg.Button('Edit', key='-EDIT-', expand_x=True),
            sg.Button('Delete', key='-DELETE-', expand_x=True),
         ],
    ]

    return sg.Window('Phone Book', layout)


main_window = create_main_window()

while True:
    event, values = main_window.read()
    if event == sg.WIN_CLOSED:
        break