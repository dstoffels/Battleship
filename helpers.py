import os

def clear_console():
    os.system('cls')

def validate_int_input(prompt):
    while True:
        try:
            response = int(input(prompt))
            return response
        except:
            prompt = 'Please enter a number: '

def index_len(list):
    return len(list) - 1