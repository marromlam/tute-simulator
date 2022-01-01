# Simulation for 'tute!'
#
#

__all__ = []
__author__ = ["Marcos Romero Lamas"]
__email__ = ["marromlam@gmail.com"]


from tqdm import tqdm
from game import Game


game = Game(4)
number_of_games = int(1e6)
match = 0

print("Running simulation for shouting 'tute!' when playing tute.")
print("The player can claim tute if she/he has the four jacks or four kings.")
print("Let's say swords (S) are trumps.")
print(80*"-")
for i in tqdm(range(number_of_games)):
  game.shuffle(False)
  game.deal(False)
  if ("kS" in game.players[0]) and ("jS" in game.players[0]):
    match += 1

if match > 0:
  print(f"{match}/{number_of_games} = {match/number_of_games:.4f}")
else:
  print("Please increase the number of games, since there are no matches")


# vim: fdm=marker ts=2 sw=2 sts=2 sr noet
