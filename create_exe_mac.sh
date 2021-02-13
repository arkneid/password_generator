#!/bin/bash

python3.7 /Users/jpfc/opt/pyinstaller-4.2/pyinstaller.py --noconfirm --onefile --windowed --name PassGenMac --add-data "$HOME/git_personal/python/projetos/password_generator/res:res/" "$HOME/git_personal/python/projetos/password_generator/main.py"
mv dist/* exe
rm -rf  __pycache__ build dist *.spec
