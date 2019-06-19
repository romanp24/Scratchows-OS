from tkinter import messagebox, simpledialog, Tk
import os
print('Welcome to Scratchows Console Engine 1.0')
print('For a list of commands, type "help"')
loop = 'true'
while loop == 'true':
    command = input('> ')
    if command == 'exit' or command == 'Exit':
        loop = 'false'
    elif command == 'help':
        print('''Apps:
calc.exe - opens the calculator
diag.exe - runs Scratchows diagnostics
pref.exe - opens settings

Commands:
shtdwn - shuts down the engine
opn - open a file (coming soon)
''')

    elif command == 'calc.exe':
        os.system('calculator.py')
    else:
        print('That is not a valid command.')
    
        