#PySimple examples (v 3.9)
#Tony Crewe
#Oct 2018 MacOs

import simpleui as sg

#sg.ChangeLookAndFeel('BlueMono')
sg.SetOptions (background_color = 'LightBlue',
            element_background_color = 'LightBlue',
            text_element_background_color = 'LightBlue',
               font = ('Calibri', 14, 'bold'),
               text_color = 'Black',
               input_text_color ='Black',
               button_color = ('Black', 'White'))

#use column feature with height listbox takes up
column1 = [
    [sg.Text('Add or Delete Items\nfrom a Listbox')],
     [sg.InputText( size = (15,1), key = 'add'), sg.ReadButton('Add', size = (5,1))],
    [sg.ReadButton('Delete selected entry', size = (18,1))]]

#initial listbox entries
List = ['Austalia', 'Canada', 'Greece']         

#add initial List  to listbox
layout = [
    [sg.Listbox(values=[l for l in List], size = (20,8), key ='_listbox_'),
     sg.Column(column1)]]

window = sg.Window('Listbox').Layout(layout)

while True:
    button, value = window.Read()
    if button is not None:
        #value[listbox] returns a list
        #using value[listbox][0] gives the string
        if button == 'Delete selected entry':
            #ensure something is selected
            if value['_listbox_'] == []:               
                sg.Popup('Error','You must select a Country')
            else:
                #find and remove this
                List.remove(value['_listbox_'][0])  
        if button == 'Add':
            #add string in add box to list
            List.append(value['add'])          
        List.sort()                         
        #update listbox
        window.FindElement('_listbox_').Update(List)
    else:
        break  
