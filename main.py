import PySimpleGUI as sg
import make_list as li

sg.theme('DarkTanBlue')

layout = [[sg.Text('Enter an event:')],
          [sg.Input(key='-IN-', do_not_clear=False)],
          [sg.Button('Add'), sg.Button('Exit')], 
          [sg.Text(size=(15,1), key='-OUTPUT-')]]

window = sg.Window('Pattern 2B', layout)

while True:  # Event Loop
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Add':
        # Update the "output" text element to be the value of "input" element
        occurence = "".join(values['-IN-'])
        day_list = li.make_list(occurence)
        window['-OUTPUT-'].update(day_list)

window.close()