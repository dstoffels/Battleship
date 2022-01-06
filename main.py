from gameBoard import GameBoard
from ship import Ship


gb = GameBoard()

destroyer = Ship('Destroyer', 2)
carrier = Ship('Carrier', 5)

# gb.try_place_ship(carrier, (1,10), False)
gb.try_place_ship(carrier, 'a7', True)
# gb.try_place_ship(destroyer, (1,1), True)
gb.try_place_ship(destroyer, 'i1', True)
