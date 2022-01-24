from player import Player
from human import Human
from ai import AI

class Battle:
  def __init__(self):
    self.player1: Player = None
    self.player2: Player = None
    
  def run(self):
    self.setup_players()

  def setup_players(self):
    self.player1.setup()
    self.player2.setup()

class Hot_Seat_Battle(Battle):
  def __init__(self) :
    self.player1 = Human()
    self.player2 = Human()

class Solo_Battle(Battle):
  def __init__(self):
      self.player1 = Human()
      self.player2 = AI()
