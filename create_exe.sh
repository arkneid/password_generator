#!/bin/bash

pyinstaller --noconfirm --onefile --windowed --name PassGen --add-data "/mnt/c/users/joao.chamine/git_personal/python/projetos/password_generator/res:res/" "/mnt/c/users/joao.chamine/git_personal/python/projetos/password_generator/main.py"
mv dist/* exe
rm -rf  __pycache__ build dist *.spec
