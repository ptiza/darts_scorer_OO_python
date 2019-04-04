from viewer import Viewer
from player import Player
from game import Game

class Match(object):

  def __init__(self, playernames, sets, legs_per_set, start_score):
    self.viewer = Viewer()
    self.players = list(range(len(playernames)))
    for i in list(range(len(playernames))):
      self.players[i] = Player(i, playernames[i], start_score)
    self.start_score = start_score
    self.sets = sets
    self.legs_per_set = legs_per_set
    self.game = Game(start_score, self.players, sets, legs_per_set)
    self.set_thrower = self.players[0]
    self.leg_thrower = self.players[0] 

  def turn(self, player):
    self.viewer.check_if_on_a_finish(player)
    player_throw = self.viewer.get_throw(player)
    self.viewer.check_if_bust(player, player_throw)
    self.viewer.check_for_winning_throw(player, player_throw)
    player.throw_darts(player_throw)

  def legs_needed_to_win_set(self):
    return int((self.legs_per_set / 2) + 1)

  def sets_needed_to_win(self):
    return int((self.sets / 2) + 1)

  def set_won(self):
    for player in self.players:
      if (player.legs_won == self.legs_needed_to_win_set()):   
        self.game.winner().sets_won += 1
        return True 
    return False 

  def match_won(self):
    for player in self.players:
      if player.sets_won == self.sets_needed_to_win():
        return True
    return False

  def play_match(self):
    while not(self.match_won()):
      self.play_leg()
      self.leg_won()

  def leg_won(self):
    self.game.winner().legs_won += 1
    if (self.set_won()):
      if (self.match_won()):
        self.display_winner("match")
        return
      else:
        self.display_winner("set")
        self.new_set()
    else:
      self.display_winner("leg")
      self.new_leg()

  def new_leg(self):
    self.new_game()
    self.game.thrower = self.switch_thrower(self.leg_thrower)
    self.leg_thrower = self.game.thrower

  def new_set(self):
    for num in list(range(len(self.game.players))):   
      self.game.players[num].legs_won = 0
    self.new_game()
    self.game.thrower = self.switch_thrower(self.set_thrower)
    self.set_thrower = self.game.thrower

  def new_game(self):
    for num in list(range(len(self.game.players))):
      self.game.players[num].reset(self.start_score)
    self.game = Game(self.start_score, self.players, self.sets, self.legs_per_set)

  def switch_thrower(self,thrower):
    if (thrower == self.game.players[len(self.game.players)-1]):
        thrower = self.game.players[0]
    else:
        thrower = self.game.players[self.game.players.index(thrower)+1]
    return thrower

  def play_leg(self):
    self.viewer.print_scoreboard(self,self.game)    
    while not(self.game.won()):
      self.turn(self.game.thrower)
      self.viewer.print_scoreboard(self,self.game)
      self.game.switch_thrower();

  def display_winner(self,game):
    winner = self.game.winner().name
    print("Game shot, and the {:s} to {:s}".format(game, winner))
