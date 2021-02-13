# coding=utf-8

#########################
# Author: João Chaminé  #
#########################

def build(sg):
    buttons = [
        [sg.Button("Generate password")]
    ]

    outbox = [
        [sg.Output(key='_output_')]
    ]

    layout = [
        [sg.Column(outbox, justification='center', size=(300, 35))],  # Column 1
        [sg.Column(buttons, justification='center')]  # Column 2
    ]

    return layout
