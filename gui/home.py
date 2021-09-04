import PySimpleGUI as sg

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.

options_column = [  [sg.Text('Input Type'),
                     sg.Radio('Text File', group_id='FILETYPE', default=True, enable_events=True, key='filetype2'),
                     sg.Radio('Text', group_id='FILETYPE', enable_events=True, key='filetype1'),
                     sg.Radio('Binary File', group_id='FILETYPE', enable_events=True, key='filetype3')
                    ],
                    [sg.Text('File Input Path', key='filepathText'),
                     sg.InputText( key='filepathInput'),
                     sg.FileBrowse(key='filepathButton')
                     ],
                    [sg.Text('Cipher Type'),
                     sg.InputCombo(['Shift', 'Substitution', 'Affine', 'Hill', 'Playfair', 'Vigenere'], default_value='Shift')
                    ],
                    [sg.Text('Key      '), sg.InputText()],
                    [sg.Text('Operation'),
                     sg.Radio('Encryption', group_id='OPTYPE', default=True, enable_events=True, key='optype1'),
                     sg.Radio('Decryption', group_id='OPTYPE', enable_events=True, key='optype2'),
                    ],
                    [sg.Text('Ciphertext Output', key='CIPHEROUTPUTTYPE'),
                     sg.Radio('No Space', group_id='CIPHEROUTPUT', default=True),
                     sg.Radio('5-Character Group', group_id='CIPHEROUTPUT'),
                    ],
                    [sg.Checkbox('Save output as file', default=False)],
                ]

plaintext_column = [ [sg.Frame('Plaintext',
                               [[sg.Multiline(key='-INPUT-')]],
                               size=(None, 30)
                               )
                      ] ]
                
ciphertext_column = [ [sg.Frame('Ciphertext',
                                [[sg.Multiline(key='-OUTPUT-')]],
                                size=(None, 30)
                                )
                       ] ]

layout = [  [sg.Column(plaintext_column,
                       expand_y=True),
             sg.Column(ciphertext_column,
                       expand_y=True),
             ],
            [
             sg.Frame('Options', options_column,
                      expand_x=True,
                      element_justification='center'),
             ],
            [sg.Button('Start'),
             sg.Button('Cancel')
             ]
          ]

# Create the Window
window = sg.Window('Cipher',
                   layout,
                   auto_size_text=True,
                   element_justification='center'
                   )

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    
    if event == 'Start':
        window['-OUTPUT-'].update('Hello ' + values['-INPUT-'] + "! Thanks for trying PySimpleGUI")
        
    if event == 'filetype1':
        window['filepathText'].hide_row()
    elif event == 'filetype2' or event == 'filetype3':
        window['filepathText'].unhide_row()
    
    if event == 'optype2':
        window['CIPHEROUTPUTTYPE'].hide_row()
    elif event == 'optype1':
        window['CIPHEROUTPUTTYPE'].unhide_row()

window.close()