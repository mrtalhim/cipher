import PySimpleGUI as sg
import numpy as np
import helper_function as hf
from numpy.linalg.linalg import LinAlgError
from shift_cipher import shift_cipher
from substitution_cipher import substitution_cipher
from affine_cipher import affine_cipher
from hill_cipher import hill_cipher
from playfair_cipher import playfair_cipher
from standart_vigenere_cipher import standart_vigenere_cipher
from extended_vigenere_cipher import extended_vigenere_cipher

def key_hill_input(keysize):
    keysize = int(keysize)
    matrix_num = []
    matrix_char = []
    matrix_input = [[sg.InputText(size=(3, 1),
                                  key='KEYINPUT({},{})'.format(x, y))
                     for x in range(keysize)]
                    for y in range(keysize)]
    
    layout = [[sg.Text('Alphabet key (a-z)')],
              [matrix_input],
              [sg.Button('Save', key='SAVE'), sg.CloseButton('Close')],
              [sg.Text(key='MESSAGE')]
              ]
    
    window = sg.Window('Key Input',
                       layout,
                       element_justification='center')
    
    while True:
        event, values = window.read()
        print(event, values)
        
        if event == 'Close' or event == sg.WIN_CLOSED:
            break
        
        if event == 'SAVE':
            alphabet = hf.alphabet_init()
            for i in range(keysize):
                row_num = []
                row_char = []
                for j in range(keysize):
                    input = values['KEYINPUT({},{})'.format(i, j)]
                    row_char.append(input.upper())
                    input = hf.alphabet_index(input.lower(), alphabet)
                    row_num.append(input)
                matrix_char.append(row_char)
                matrix_num.append(row_num)
            
            matrix_num = np.array(matrix_num)
            try:
                np.linalg.inv(matrix_num)
                window.close()
                return matrix_char
            except LinAlgError:
                window['MESSAGE'].update('Key is not inversible')
                matrix_num = []
                matrix_char = []
                continue
            
def home():
    sg.theme('DarkAmber')   # Add a touch of color
    # All the stuff inside your window.
    
    text_cipher_dict = {'Shift': shift_cipher,
                        'Substitution': substitution_cipher,
                        'Affine': affine_cipher,
                        'Vigenere':standart_vigenere_cipher,
                        'Hill': hill_cipher,
                        'Playfair': playfair_cipher
                        }
    
    binaryfile_cipher_dict = {'Vigenere': extended_vigenere_cipher}
    
    num_key_list = ['Shift', 'Affine', 'Hill']
    
    file_input_layout = [[sg.Text('Input File'), sg.InputText(key='INPUTFILEPATH'), sg.FileBrowse(file_types=(('TXT file', '*.txt'),
                                                                                                                                     ('BIN file', '*.bin')))]]
    file_output_layout = [[sg.Text('Output File'), sg.InputText(key='OUTPUTFILEPATH'), sg.FileSaveAs(file_types=(('TXT file', '*.txt'),
                                                                                                                                     ('BIN file', '*.bin')))]]
    cipher_output_layout = [[sg.Text('Ciphertext Output'),
                             sg.Radio('No Space', group_id='CIPHEROUTPUT', default=True, key='CIPHERNOSPACE'),
                             sg.Radio('5-Character Group', group_id='CIPHEROUTPUT', key='CIPHERINGROUP'),
                             ]]
    
    key_single_input = [[sg.Text('Key'),
                         sg.InputText(key='CIPHERKEY'),
                         ],
                         [sg.Text('Number key (0-9)', key='SINGLEINPUTMESSAGE', justification='center', expand_x=True)]
                        ]
    key_affine_input = [[sg.Text('Key'),
                         sg.InputText(key='CIPHERKEY_A'),
                         sg.InputText(key='CIPHERKEY_B')
                         ],
                         [sg.Text('Number key (0-9)', key='AFFINEINPUTMESSAGE', justification='center', expand_x=True)]
                        ]
    key_hill_size_input = [[sg.Text('Key Size'),
                            sg.InputText(key='KEYSIZE'),
                            sg.Button('Input Key', key='GETHILLKEY')
                            ]]
    
    text_input_selection = [[sg.InputCombo(list(text_cipher_dict.keys()), 
                                       enable_events=True,
                                       key='CIPHERTEXTTYPE', 
                                       default_value='Shift')]]
    
    binaryfile_input_selection = [[sg.InputCombo(list(binaryfile_cipher_dict.keys()), 
                                       enable_events=True,
                                       key='CIPHERBINARYFILETYPE', 
                                       default_value='Vigenere')]]

    options_column = [  [sg.Text('Input Type'),
                         sg.Radio('Text', group_id='INPUTTYPE', default=True,enable_events=True, key='TEXTINPUT'),
                         sg.Radio('Binary File', group_id='INPUTTYPE',enable_events=True, key='BINARYFILEINPUT')],
                        [sg.Text('Cipher'),
                         hf.collapse(text_input_selection, 'CIPHERTEXTROW', True),
                         hf.collapse(binaryfile_input_selection, 'CIPHERBINARYFILEROW', False),
                         ],
                        [hf.collapse(key_single_input, 'KEYSINGLEINPUT', True)],
                        [hf.collapse(key_affine_input, 'KEYAFFINEINPUT', False)],
                        [hf.collapse(key_hill_size_input, 'KEYHILLINPUT', False)],
                        [sg.Text('Mode'),
                        sg.Radio('Encryption',
                                 group_id='OPTYPE',default=True, 
                                 enable_events=True, key='ENCRYPT'),
                        sg.Radio('Decryption',
                                 group_id='OPTYPE', enable_events=True, 
                                 key='DECRYPT'),
                        ],
                        [hf.collapse(cipher_output_layout, 'CIPHEROUTPUTTYPE', True)],
                        [sg.Checkbox('Input from file', enable_events=True, key='INPUTFILE'),
                         sg.Checkbox('Save output as file', enable_events=True, key='OUTPUTFILEOPTION', default=False)
                         ],
                        [hf.collapse(file_input_layout, 'INPUTFILESECTION', False)],
                        [hf.collapse(file_output_layout, 'OUTPUTFILESECTION', False)],
                    ]

    plaintext_column = [ [sg.Frame('Plaintext',
                                [[sg.Multiline(key='PLAINTEXT')]],
                                size=(None, 30)
                                )
                        ] ]
                    
    ciphertext_column = [ [sg.Frame('Ciphertext',
                                    [[sg.Multiline(key='CIPHERTEXT')]],
                                    size=(None, 30)
                                    )
                        ] ]

    layout = [  
                [
                sg.Frame('Options', options_column,
                        expand_x=True,
                        element_justification='center'),
                ],
                [sg.Column(plaintext_column,
                        expand_y=True),
                sg.Column(ciphertext_column,
                        expand_y=True),
                ],
                [sg.Button('Start'),
                 sg.CloseButton('Close')
                ],
                [sg.Text(key='MESSAGE')]
            ]

    # Create the Window
    window = sg.Window('Shift Cipher',
                       layout,
                       auto_size_text=True,
                       element_justification='center'
                       )
    
    input_file_section_is_visible = False
    output_file_section_is_visible = False
    cipher_output_section_is_visible = True
    key_input_selection = {'KEYSINGLEINPUT': ['Shift', 'Substitution', 'Vigenere', 'Playfair'],
                           'KEYAFFINEINPUT': 'Affine',
                           'KEYHILLINPUT': 'Hill'
                           }

    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        print(event, values)
        window['MESSAGE'].update('')
        if event == sg.WIN_CLOSED or event == 'Close': # if user closes window or clicks cancel
            break
        
        # enable text file input row
        if event == 'INPUTFILE':
            input_file_section_is_visible = not input_file_section_is_visible
            window['INPUTFILESECTION'].update(visible=input_file_section_is_visible)
        
        # enable file output row
        if event == 'OUTPUTFILEOPTION':
            output_file_section_is_visible = not output_file_section_is_visible
            window['OUTPUTFILESECTION'].update(visible=output_file_section_is_visible)
        
        # enable split type row
        if event == 'ENCRYPT' or event == 'DECRYPT':
            cipher_output_section_is_visible = values['ENCRYPT']
            window['CIPHEROUTPUTTYPE'].update(visible=cipher_output_section_is_visible)
            
        # change key input from cipher selection
        if event == 'CIPHERTEXTTYPE' or event == 'CIPHERBINARYFILETYPE':
            object_key = 'CIPHERTEXTTYPE' if values['TEXTINPUT'] else 'CIPHERBINARYFILETYPE'
            for x in key_input_selection.keys():
                if values[object_key] in key_input_selection[x]:
                    window[x].update(visible=True)
                else:
                    window[x].update(visible=False)
            
            if values[object_key] in num_key_list:
                window['SINGLEINPUTMESSAGE'].update('Number key (0-9)')
            else:
                window['SINGLEINPUTMESSAGE'].update('Alphabet key (a-z)')
                    
        # open hill key input
        if event == 'GETHILLKEY':
            key = key_hill_input(values['KEYSIZE'])
            window['MESSAGE'].update(key)
                    
        # change cipher selection based on input type
        if event == 'TEXTINPUT' or event == 'BINARYFILEINPUT':
            window['CIPHERTEXTROW'].update(visible=values['TEXTINPUT'])
            window['CIPHERBINARYFILEROW'].update(visible=values['BINARYFILEINPUT'])
            window['INPUTFILE'].update(values['BINARYFILEINPUT'], disabled=values['BINARYFILEINPUT'])
            input_file_section_is_visible = not input_file_section_is_visible
            window['INPUTFILESECTION'].update(visible=input_file_section_is_visible)
        
        if event == 'Start':
            input = ''
            output = ''
            is_split = values['CIPHERINGROUP']
            if values['TEXTINPUT']:
                if values['CIPHERTEXTTYPE'] == 'Affine':
                    a_key = int(values['CIPHERKEY_A'])
                    b_key = int(values['CIPHERKEY_B'])
                    key = (a_key, b_key)
                elif values['CIPHERTEXTTYPE'] == 'Hill':
                    key=key
                else:
                    key = int(values['CIPHERKEY']) if values['CIPHERTEXTTYPE'] in num_key_list else values['CIPHERKEY']
            elif values['BINARYFILEINPUT']:
                key = values['CIPHERKEY']
            
            if values['INPUTFILE']:
                open_file_mode = 'r' if values['TEXTINPUT'] else 'rb'
                with open(values['INPUTFILEPATH'], open_file_mode) as f:
                    input = f.read()
                window['PLAINTEXT' if values['ENCRYPT'] else 'CIPHERTEXT'].update(input)
            else:
                input = values['PLAINTEXT' if values['ENCRYPT'] else 'CIPHERTEXT']
            
            dict_function = text_cipher_dict if values['TEXTINPUT'] else binaryfile_cipher_dict
            cipher_type = 'CIPHERTEXTTYPE' if values['TEXTINPUT'] else 'CIPHERBINARYFILETYPE'
            mode = 'encrypt' if values['ENCRYPT'] else 'decrypt'
            
            output = dict_function[values[cipher_type]](key=key, input=input, mode=mode, cipher_split=is_split)
            window['CIPHERTEXT' if values['ENCRYPT'] else 'PLAINTEXT'].update(output)
                
            if values['OUTPUTFILEOPTION']:
                open_file_mode = 'w' if values['TEXTINPUT'] else 'wb'
                with open(values['OUTPUTFILEPATH'], open_file_mode) as f:
                    f.write(output.encode() if values['BINARYFILEINPUT'] else output)
                    window['MESSAGE'].update('File saved ({})'.format(values['OUTPUTFILEPATH']))
            else:
                window['MESSAGE'].update('Operation {} {} complete'.format(values[cipher_type], mode))
                
                
if __name__ == "__main__":
    home()