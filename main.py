import PySimpleGUI as sg
import make_list as li

sg.theme('DarkTanBlue')


layout = [[sg.Text('Enter or edit an event:')],
          [sg.Input(key='-IN-', do_not_clear=False)],
          [sg.Button('Add'), sg.Button('Exit')], 
          [sg.Listbox([], size=(15,13), key ='-LIST-')],
          [sg.Button('Delete'), sg.Button('Edit')]]

window = sg.Window('Day Planner', layout)

while True:  # Event Loop
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Add':
        # Update the "output" text element to be the value of "input" element
        occurence = "".join(values['-IN-'])
        day_list = li.make_list(occurence)
        window['-LIST-'].update(day_list)
    if event == 'Delete':
      if values['-LIST-']:
        day_list = li.deleted(values['-LIST-'][0], day_list)
        window['-LIST-'].update(day_list)
    if event == 'Edit':
      if values['-LIST-']:
        day_list = li.edit(values['-LIST-'][0],values['-IN-'], day_list)
        window['-LIST-'].update(day_list)
    


window.close()