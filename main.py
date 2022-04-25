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


def save_table(data, head):
    try:
        with open('contacts.csv', mode='w', encoding='utf-8', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow([i.lower() for i in head])
            csv_writer.writerows(data)
    except Exception as ex:
        print(ex)


def create_main_window(data, head):
    layout = [
        [sg.Input(key='-IN_BROWSE-'), sg.Button('Browse', key='-BROWSE-', expand_x=True)],
        [
            sg.Input(enable_events=True, key='-IN_SEARCH-'),
            sg.Combo(head, default_value='Name'),
            # sg.Button('Search', key='-SEARCH-')
        ],
        [sg.Table(values=data,
                  key='-TABLE-',
                  headings=head,
                  justification='left',
                  expand_x=True,
                  enable_events=True,
                  select_mode=sg.TABLE_SELECT_MODE_BROWSE,
                  # alternating_row_color='black'
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
    add_window = None
    edit_window = None
    data_values = make_table()
    header = ['Name', 'Surname', 'Number']
    main_window = create_main_window(data_values, header)
    data_selected = []
    search_values = []
    data_row = None
    while True:
        window, event, values = sg.read_all_windows()

        # main window events
        if window == main_window:
            if event == sg.WIN_CLOSED:
                window.close()
                break

            elif event == '-ADD-' and not add_window and not edit_window:
                add_window = create_add_window()

            elif event == '-EDIT-' and not edit_window and not add_window and data_selected:
                edit_window = create_edit_window()
                edit_window['-EDIT_NAME-'].update(data_selected[0][0])
                edit_window['-EDIT_SURNAME-'].update(data_selected[0][1])
                edit_window['-EDIT_NUMBER-'].update(data_selected[0][2])

            elif event == '-TABLE-' and len(values['-TABLE-']):
                if search_values:
                    data_selected = [search_values[row] for row in values[event]]
                else:
                    data_selected = [data_values[row] for row in values[event]]
                for row in values[event]:
                    data_row = row

            elif event == '-DELETE-' and not edit_window and not add_window and data_selected:
                del data_values[data_row]
                save_table(data_values, header)
                main_window['-TABLE-'].update(values=data_values)

            elif event == '-BROWSE-':
                print(event)

            if values['-IN_SEARCH-'] != '' and event != '-TABLE-':
                search = str(values['-IN_SEARCH-']).lower()
                search_values = [search_row for search_row in data_values if search in str(search_row[0]).lower()]
                main_window['-TABLE-'].update(values=search_values)
            elif event != '-TABLE-':
                search_values = []
                main_window['-TABLE-'].update(values=data_values)

        # add window events
        if window == add_window:
            if event == sg.WIN_CLOSED:
                window.close()
                add_window = None

            elif event == '-ADD_SAVE-' and window == add_window:
                if len(values['-ADD_NAME-']) and len(values['-ADD_SURNAME-']) and len(values['-ADD_NUMBER-']):
                    data_values.append([values['-ADD_NAME-'], values['-ADD_SURNAME-'], values['-ADD_NUMBER-']])
                    save_table(data_values, header)
                main_window['-TABLE-'].update(values=data_values)
                window.close()
                add_window = None

        # edit window events
        if window == edit_window:
            if event == sg.WIN_CLOSED:
                window.close()
                edit_window = None

            elif event == '-EDIT_SAVE-' and window == edit_window:
                if len(values['-EDIT_NAME-']) and len(values['-EDIT_SURNAME-']) and len(values['-EDIT_NUMBER-']):
                    data_values[data_row] = [values['-EDIT_NAME-'], values['-EDIT_SURNAME-'], values['-EDIT_NUMBER-']]
                    save_table(data_values, header)
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