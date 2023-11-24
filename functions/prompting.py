import time
from os import system, name

def prompting(text):
    for lettre in text: 
        print(lettre, end='', flush=True)
        time.sleep(0.03)

def clear_screen():
    if name == 'nt': 
        _ = system('cls') 
    else: 
        _ = system('clear')