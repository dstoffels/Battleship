
from battle import Hot_Seat_Battle, Solo_Battle
from helpers import clear_console, validate_int_input
from constant import MAIN_MENU_PROMPT

class Battleship:
  def __init__(self) -> None:
      self.game = None
      self.run()

  def run(self):
    self._reset()

    prompt = MAIN_MENU_PROMPT
    while True:
      userInput = validate_int_input(prompt)
      match userInput:
        case 1: self.game = Solo_Battle()
        case 2: self.game = Hot_Seat_Battle()
        case 3: self.exit_program()
      if self.game: self.game.run()

  def exit_program(self):
    clear_console()
    exit()

  def _reset(self):
    self.game = None
    clear_console()
