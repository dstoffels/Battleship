from boardSetupMenu import BoardSetupMenu
from player import Player
import coords

class Human(Player):

  def select_target(self):
    self.opponent.game_board.display(False)
    self.game_board.display()
    return coords.get_from_user()

  def _setup_game_board(self):
    BoardSetupMenu(self)
    
  def _set_name(self):
    prompt = f'Enter a name for player {self.player_num}: '
    while self.name == '':
      name = input(prompt)
      if str.lower(name) == str.lower(self.opponent.name): prompt = 'Player names cannot be the same! Enter a different name: '
      else: self.name = name