from helpers import validate_int_input


MAIN_MENU = '''
1) Single Player Game
2) Two Player Game
3) Quit

Choose an option: '''

def run_main_menu():
  prompt = MAIN_MENU
  while True:
    userInput = validate_int_input(prompt)

    match userInput:
      case 1: pass
      case 2: pass
      case 3: exit()
      case _: prompt = 'Choose an option between 1-3: '

