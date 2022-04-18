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
    main_window = sg.Window('Phone Book', layout)
    while True:
        event, values = main_window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == '-ADD-':
            create_add_edit_windows('Add Contact')
        if event == '-EDIT-':
            create_add_edit_windows('Edit Contact')
        if event == '-DELETE-':
            print(event)
    main_window.close()


def create_add_edit_windows(title):
    layout = [
        [sg.Text('Name:'), sg.Input()],
        [sg.Text('Surname:'), sg.Input()],
        [sg.Text('Number:'), sg.Input()],
        [sg.Button('Save', key='-SAVE-')],
    ]
    window = sg.Window(title, layout)
    while True:
        event_sub, values_sub = window.read()
        if event_sub == sg.WIN_CLOSED:
            break
    window.close()


if __name__ == '__main__':
    create_main_window()
