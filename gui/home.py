import PySimpleGUI as sg

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.

options_column = [  [sg.Text('Input Type'),
                     sg.Radio('Text', group_id='FILETYPE', default=True),
                     sg.Radio('Text File', group_id='FILETYPE'),
                     sg.Radio('Binary File', group_id='FILETYPE')
                    ],
                    [sg.Text('Filepath'), sg.InputText(), sg.Button('Browse')],
                    [sg.Text('Cipher Type'),
                     sg.InputCombo(['Shift', 'Substitution', 'Affine', 'Hill', 'Playfair', 'Vigenere'], default_value='Shift')
                    ],
                    [sg.Text('Key      '),sg.InputText()],
                    [sg.Text('Ciphertext Output')],
                    [sg.Radio('No Space', group_id='CIPHEROUTPUT', default=True),
                     sg.Radio('5-Character Group', group_id='CIPHEROUTPUT'),
                    ],
                    [sg.Checkbox('Save output as file', default=False)],
                    [sg.Button('Encrypt'),
                     sg.Button('Decrypt'),
                     sg.Button('Cancel')
                    ]
                ]

plaintext_column = [ [sg.Frame('Plaintext',
                               [[sg.Multiline(key='-INPUT-')]]
                               )
                      ] ]
                
ciphertext_column = [ [sg.Frame('Ciphertext',
                                [[sg.Multiline(key='-OUTPUT-')]]
                                )
                       ] ]

layout = [  [sg.Column([[sg.Frame('Options', options_column)]]),
             sg.Column(plaintext_column,
                       expand_y=True),
             sg.Column(ciphertext_column,
                       expand_y=True)
             ] ]

# Create the Window
window = sg.Window('Cipher', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    window['-OUTPUT-'].update('Hello ' + values['-INPUT-'] + "! Thanks for trying PySimpleGUI")


window.close()