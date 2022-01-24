from gameBoard import GameBoard
from placeShipMenu import PlaceShipMenu

from helpers import clear_console, validate_int_input

class BoardSetupMenu:
  def __init__(self, player):
    self.player = player
    self.game_board: GameBoard = player.game_board
    self.is_done = False
    self.run()

  def run(self):
    ships = self.player.ships
    prompt = self._prompt_builder()

    while not self.is_done:
      clear_console()
      self.game_board.display()
      response = validate_int_input(prompt)

      match response:
        case 1 | 2 | 3 | 4 | 5: 
          PlaceShipMenu(self.player, ships[response - 1])
          prompt = self._prompt_builder()
        case 6: 
          self.player.place_ships_randomly()
          prompt = self._prompt_builder()
        case 7: 
          if len(self.game_board.ships) == len(self.player.ships): self.is_done = True
          else: prompt = 'Please make a valid selection...'
        case _: 
          prompt = 'Please make a valid selection... '

  def _prompt_builder(self):
    ships = self.player.ships
    game_board_ships = self.game_board.ships
    prompt = '\n'
    for i in range(len(ships)):
      prompt += f'{i + 1}) '
      prompt += f'Move {ships[i].name}\n' if ships[i] in game_board_ships.keys() else f'Place {ships[i].name}\n'
    prompt += '6) Place ships randomly\n'
    if len(game_board_ships) == len(ships):
      prompt += '7) Ready for battle!\n'
    return prompt