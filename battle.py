from player import Player
from human import Human
from ai import AI

class Battle:
  def __init__(self):
    self.player1: Player = None
    self.player2: Player = None
    
  def run(self):
    self.setup_players()
    while not self.has_winner():
      self.player1.take_turn()
      self.player2.take_turn()
    self.declare_winner()

  def setup_players(self):
    self.player1.setup(self.player2)
    self.player2.setup(self.player1)

  def has_winner(self):
    return self.player1.is_defeated() or self.player2.is_defeated()

  def declare_winner(self):
    print('we have a winner...') #FIXME: needs winner logic for each player

class Hot_Seat_Battle(Battle):
  def __init__(self) :
    super().__init__()
    self.player1 = Human(1)
    self.player2 = Human(2)

class Solo_Battle(Battle):
  def __init__(self):
    super().__init__()
    self.player1 = Human(1)
    self.player2 = AI(2)

class Computer_Battle(Battle):
  def __init__(self):
    super().__init__()
    self.player1 = AI(1)
    self.player2 = AI(2)