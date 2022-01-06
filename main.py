from player import Player
from ai import AI

from helpers import clear_console, validate_int_input
from constant import MAIN_MENU

def run_solo_game():
  player1 = Player()
  player2 = AI()
  run_game(player1, player2)

def run_hotseat_game():
  player1 = Player()
  player2 = Player()
  run_game(player1, player2)

def run_game(player1: Player, player2: Player):
  player1.setup(1, '')
  player2.setup(2, player1.name)


def run_main_menu():
  prompt = MAIN_MENU
  while True:
    clear_console()
    userInput = validate_int_input(prompt)

    match userInput:
      case 1: run_solo_game()
      case 2: run_hotseat_game()
      case 3: exit_program()
      case _: prompt = 'Choose an option between 1-3: '

def exit_program():
  clear_console()
  exit()

run_main_menu()