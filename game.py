# Game
#
#

__all__ = ['Game']
__author__ = ["Marcos Romero Lamas"]
__email__ = ["marromlam@gmail.com"]

import random
from functools import reduce
from operator import mul


class Game(object):
  """docstring for Game."""

  def __init__(self, number_of_players=4, number_of_cards=40,
               number_of_decks=1, number_of_jokers=0):
    super(Game, self).__init__()
    self.number_of_players = number_of_players
    self.number_of_cards = number_of_cards
    self.number_of_decks = number_of_decks
    self.number_of_jokers = number_of_jokers
    self.players = self.number_of_players * [[]]
    self.cards = []
    self.deck = ['aC', '2C', '3C', '4C', '5C', '6C', '7C', 'sC', 'jC', 'kC']
    self.deck += ['aS', '2S', '3S', '4S', '5S', '6S', '7S', 'sS', 'jS', 'kS']
    self.deck += ['aB', '2B', '3B', '4B', '5B', '6B', '7B', 'sB', 'jB', 'kB']
    self.deck += ['aO', '2O', '3O', '4O', '5O', '6O', '7O', 'sO', 'jO', 'kO']
    self.jokers = []
    self.dealer = None
    self.current_player = None
    self.current_card = None
    self.current_round = None
    if len(self.deck) % self.number_of_players != 0:
        msg = "Cant create the game because the number of players and the "
        msg += "number of cards are incompatible."
        raise AttributeError(msg)

  def shuffle(self, debug=False):
    if debug:
        print("Shuffling the deck...")
        print(self.deck)
    random.shuffle(self.deck)
    if debug:
        print(self.deck)

  def deal(self, debug=False):
    # TODO: this can be optimized a lot
    def _group(lst, shape):
      if len(shape) == 1:
          return lst
      n = reduce(mul, shape[1:])
      return [_group(lst[i*n:(i+1)*n], shape[1:]) for i in range(len(lst)//n)]

    # define the output shape
    shape = [len(self.deck)//self.number_of_players,
             self.number_of_players]
    # group the cards
    _players = _group(self.deck, shape)
    # transpose it
    assert reduce(mul, shape) == len(self.deck)
    self.players = list(map(list, zip(*_players)))
    if debug:
        print(self.players)


# vim: fdm=marker ts=2 sw=2 sts=2 sr noet
