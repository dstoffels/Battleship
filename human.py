from player import Player

class Human(Player):
  def __init__(self):
      super().__init__()

  def set_name(self, player_num, player1_name):
    prompt = f'Enter a name for player {player_num}: '
    self.name = player1_name
    while self.name == player1_name:
      name = input(prompt)
      if name == '': continue
      elif str.lower(name) == str.lower(player1_name): prompt = 'Player names cannot be the same! Enter a different name: '
      else: self.name = name