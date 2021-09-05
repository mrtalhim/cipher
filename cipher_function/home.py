import PySimpleGUI as sg
from gui_shift_cipher import gui_shift_cipher
import affine_cipher, substitution_cipher, standart_vigenere_cipher, extended_vigenere_cipher

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.

# simple key input = shift, substitution, vigenere
# complex key input = playfair, hill, affine
text_cipher_options = {'Shift':gui_shift_cipher,
                       'Substitution':substitution_cipher,
                       'Vigenere':standart_vigenere_cipher,
                       'Affine':affine_cipher
                       }

binaryfile_cipher_options = {'Vigenere':extended_vigenere_cipher}

text_cipher_frame = [sg.Frame('Text',
                             [[sg.Button(i, key=i) for i in list(text_cipher_options.keys())]]
                             )]

binaryfile_cipher_frame = [sg.Frame('Binary File',
                                    [[sg.Button(i, key=i) for i in list(binaryfile_cipher_options.keys())]]
                                    )]

layout = [text_cipher_frame,
          binaryfile_cipher_frame
          ]

# Create the Window
window = sg.Window('Cipher',
                   layout,
                   auto_size_text=True,
                   element_justification='center'
                   )

window2_active = False

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    
    # if event in text_cipher_options:
    #     break
    
    if event == 'Shift':
        window2_active = True
        window.hide()
        text_cipher_options[event]()
        window.un_hide()

window.close()