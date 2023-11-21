from pathlib import Path
import PySimpleGUI as ui

ui.theme("DarkBlue")

def choose_crm_file() -> str:
    select_file = [
        [ui.Text('CRM File'), ui.InputText(key='-file1-'), ui.FileBrowse()],
        [ui.Button("Start")],
    ]
    window = ui.Window('SteveConnections', select_file)
    file_exists = False
    while not file_exists:
        event, values = window.read()
        if event == ui.WINDOW_CLOSED:
            break
        elif event == "Start":
            filename = values['-file1-']
            while True:
                if not Path(filename).is_file():
                    if filename == '':
                        ui.popup_ok('Please select a file!')
                    else:
                        ui.popup_ok("That file doesn't exist!")
                    filename = ui.popup_get_file("", no_window=True)
                    if filename == '':
                        break
                    window['-file1-'].update(filename)
                else:
                    print('File is ready !')
                    file_exists = True
                    break
    window.close()
    return str(values['-file1-'])