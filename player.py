from gameBoard import GameBoard
from ship import load_ships

class Player:
  def __init__(self):
    self.name = ''
    self.board = GameBoard()
    self.ships = load_ships()

  def setup(self, player_num, player1_name):
    self.set_name(player_num, player1_name)
    self.place_ships()

  def set_name(self, player_num, player1_name):
    prompt = f'Enter a name for player {player_num}: '
    self.name = player1_name
    while self.name == player1_name:
      name = input(prompt)
      if name == '': continue
      elif str.lower(name) == str.lower(player1_name): prompt = 'Player names cannot be the same! Enter a different name: '
      else: self.name = name
      
    
  
  def place_ships(self):
    pass