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
    return sg.Window('Phone Book', layout, finalize=True)


def create_add_edit_windows(title):
    layout = [
        [sg.Text('Name:'), sg.Input()],
        [sg.Text('Surname:'), sg.Input()],
        [sg.Text('Number:'), sg.Input()],
        [sg.Button('Save', key='-SAVE-')],
    ]
    return sg.Window(title, layout, finalize=True)


def main():
    main_window = create_main_window()
    add_edit_window = None
    while True:
        window, event, values = sg.read_all_windows()
        if event == sg.WIN_CLOSED and window == main_window:
            break

        if event == '-ADD-' and not window == add_edit_window:
            add_edit_window = create_add_edit_windows('Add Contact')
        elif event == '-EDIT-' and not window == add_edit_window:
            add_edit_window = create_add_edit_windows('Edit Contact')
        elif event == '-DELETE-':
            print(event)

        if event == sg.WIN_CLOSED and window == add_edit_window:
            add_edit_window.close()
            add_edit_window = None
    main_window.close()
    if add_edit_window is not None:
        add_edit_window.close()


if __name__ == '__main__':
    main()