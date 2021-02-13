#!/usr/bin/env python3
# coding=utf-8

#########################
# Author: João Chaminé  #
#########################

# imports
from res.gen_pass import gen_pass
from res.build_layout import build
import PySimpleGUI as sg

# Build Window
layout = build(sg)
window = sg.Window("Password Generator", layout, size=(300, 100))

while True:
    event, values = window.read()

    if event == "Generate password":
        password = gen_pass()
        window.FindElement('_output_').Update(password)

    if event == sg.WIN_CLOSED:
        break

window.close()
