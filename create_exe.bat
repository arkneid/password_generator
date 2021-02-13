pyinstaller --noconfirm --onedir --windowed --name PassGen --add-data "C:/Users/joao.chamine/git_personal/python/projetos/password_generator/res;res/" "C:/Users/joao.chamine/git_personal/python/projetos/password_generator/main.py"
move dist\PassGen exe
rmdir /S /Q __pycache__ build dist
erase *.spec