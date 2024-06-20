#PySimple examples (v 3.9)
#Tony Crewe
#Oct 2018 MacOs

import simplegui as sg

sg.SetOptions(background_color = 'LightGreen',
            element_background_color = 'LightGreen',
            text_element_background_color = 'LightGreen',
              font= ('Calibri', 12, 'bold'))       

layout = [
    [sg.Text('Spinner and Combo box demo', font = ('Calibri', 14, 'bold'))],
    [sg.Spin([sz for sz in range (-9,10)], size = (2,1),initial_value = 0),
    sg.Spin([sz for sz in range (-9,10)], size = (2,1), initial_value = 0),
    sg.Text('Pick operation ->', size = (15,1)),
    sg.InputCombo(['Add','Subtract','Multiply','Divide'], size = (8,6))],
    [sg.Text('Result:   ')],[sg.InputText(size = (5,1), key = '_result_'),
     sg.ReadButton('Calculate', button_color = ('Black', 'White'))]]

window = sg.Window('Enter & Display Data', grab_anywhere= False).Layout(layout)

while True:
    button, value = window.Read()

    if button is not None:
        #convert returned values to integers
        val = [int(value[0]), int(value[1])]
        if value[2] == 'Add':
            result = val[0] + val[1]
        elif value[2] == 'Multiply':
            result = val[0] * val[1]
        elif value[2] == 'Subtract':
            result = val[0] - val[1]
        elif value[2] == 'Divide':
            if val[1] ==0:
                sg.Popup('Second value can\'t be zero')
                result = 'NA'
            else:
                result = round( val[0] / val[1], 3)
        window.FindElement('_result_').Update(result)              
    else:
        break  
