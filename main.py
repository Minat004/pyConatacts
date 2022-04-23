import PySimpleGUI as sg
import csv


def make_table():
    data = []
    try:
        with open('contacts.csv', mode='r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                data.append([str(row['name']).title(), str(row['surname']).title(), row['number']])
        return data
    except Exception as ex:
        print(ex)


def save_table(data):
    try:
        with open('contacts.csv', mode='w', encoding='utf-8', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow([i.lower() for i in header])
            csv_writer.writerows(data)
    except Exception as ex:
        print(ex)


data_values = make_table()
header = ['Name', 'Surname', 'Number']


def create_main_window():
    layout = [
        [sg.Input(), sg.Button('Browse', key='-BROWSE-', expand_x=True)],
        [
            sg.Input(),
            sg.Combo(header, default_value='Name'),
            sg.Button('Search', key='-SEARCH-')
        ],
        [sg.Table(values=data_values,
                  key='-TABLE-',
                  headings=header,
                  justification='left',
                  expand_x=True,
                  enable_events=True,
                  # select_mode=sg.TABLE_SELECT_MODE_BROWSE,
                  )],
        [
            sg.Button('Add', key='-ADD-', expand_x=True),
            sg.Button('Edit', key='-EDIT-', expand_x=True),
            sg.Button('Delete', key='-DELETE-', expand_x=True),
        ],
    ]
    return sg.Window('Phone Book', layout, finalize=True)


def create_add_window():
    layout = [
        [sg.Text('Name:'), sg.Push(), sg.Input(key='-ADD_NAME-')],
        [sg.Text('Surname:'), sg.Push(), sg.Input(key='-ADD_SURNAME-')],
        [sg.Text('Number:'), sg.Push(), sg.Input(key='-ADD_NUMBER-')],
        [sg.Button('Save', key='-ADD_SAVE-')],
    ]
    return sg.Window('Add Contact', layout, finalize=True)


def create_edit_window():
    layout = [
        [sg.Text('Name:'), sg.Push(), sg.Input(key='-EDIT_NAME-')],
        [sg.Text('Surname:'), sg.Push(), sg.Input(key='-EDIT_SURNAME-')],
        [sg.Text('Number:'), sg.Push(), sg.Input(key='-EDIT_NUMBER-')],
        [sg.Button('Save', key='-EDIT_SAVE-')],
    ]
    return sg.Window('Edit Contact', layout, finalize=True)


def main():
    main_window = create_main_window()
    add_window = None
    edit_window = None
    data_selected = []
    data_row = None
    while True:
        window, event, values = sg.read_all_windows()

        # main window events
        if event == sg.WIN_CLOSED and window == main_window:
            break
        if event == '-ADD-' and not add_window and not edit_window:
            add_window = create_add_window()

        if event == '-EDIT-' and not edit_window and not add_window and data_selected:
            edit_window = create_edit_window()
            edit_window['-EDIT_NAME-'].update(data_selected[0][0])
            edit_window['-EDIT_SURNAME-'].update(data_selected[0][1])
            edit_window['-EDIT_NUMBER-'].update(data_selected[0][2])

        if event == '-DELETE-' and window == main_window and data_selected:
            del data_values[data_row]
            save_table(data_values)
            main_window['-TABLE-'].update(values=data_values)

        if event == '-TABLE-':
            data_selected = [data_values[row] for row in values[event]]
            for row in values[event]:
                data_row = row

        if event == '-BROWSE-':
            print(event)

        # add window events
        if event == sg.WIN_CLOSED and window == add_window:
            window.close()
            add_window = None

        if event == '-ADD_SAVE-' and window == add_window:
            if len(values['-ADD_NAME-']) and len(values['-ADD_SURNAME-']) and len(values['-ADD_NUMBER-']):
                data_values.append([values['-ADD_NAME-'], values['-ADD_SURNAME-'], values['-ADD_NUMBER-']])
                save_table(data_values)
            main_window['-TABLE-'].update(values=data_values)
            window.close()
            add_window = None

        # edit window events
        if event == sg.WIN_CLOSED and window == edit_window:
            window.close()
            edit_window = None

        if event == '-EDIT_SAVE-' and window == edit_window:
            if len(values['-EDIT_NAME-']) and len(values['-EDIT_SURNAME-']) and len(values['-EDIT_NUMBER-']):
                data_values[data_row] = [values['-EDIT_NAME-'], values['-EDIT_SURNAME-'], values['-EDIT_NUMBER-']]
                save_table(data_values)
            main_window['-TABLE-'].update(values=data_values)
            window.close()
            edit_window = None

    main_window.close()
    if add_window is not None:
        add_window.close()
    elif edit_window is not None:
        edit_window.close()


if __name__ == '__main__':
    main()