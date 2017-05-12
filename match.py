from viewer import Viewer
from player import Player
from game import Game

class Match(object):

  def __init__(self, player_1_name, player_2_name, sets, legs_per_set, start_score):
    self.viewer = Viewer()
    player1 = Player(player_1_name, start_score)
    player2 = Player(player_2_name, start_score)
    self.start_score = start_score
    self.players = [ player1, player2 ]
    self.sets = sets
    self.legs_per_set = legs_per_set
    self.game = Game(start_score, self.players, sets, legs_per_set)
    self.set_thrower = player1
    self.leg_thrower = player1   

  def turn(self, player):
    self.viewer.check_if_on_a_finish(player)
    player_throw = self.viewer.get_throw(player)
    self.viewer.check_if_bust(player, player_throw)
    self.viewer.check_for_winning_throw(player, player_throw)
    player.throw_darts(player_throw)

  def legs_needed_to_win_set(self):
    return (self.legs_per_set / 2) + 1

  def sets_needed_to_win(self):
    return (self.sets / 2) + 1

  def set_won(self):
    if ((self.game.player1.legs_won == self.legs_needed_to_win_set()) or 
          (self.game.player2.legs_won == self.legs_needed_to_win_set())):   
      self.game.winner().sets_won += 1
      return True
    else:
      return False 

  def match_won(self):
    return ((self.game.player1.sets_won == self.sets_needed_to_win()) or (self.game.player2.sets_won == self.sets_needed_to_win()))

  def play_match(self):
    while not(self.match_won()):
      self.play_leg()
      print
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
    self.game.player1.legs_won = 0
    self.game.player2.legs_won = 0
    self.new_game()
    self.game.thrower = self.switch_thrower(self.set_thrower)
    self.set_thrower = self.game.thrower

  def new_game(self):
    self.game.player1.reset(self.start_score)
    self.game.player2.reset(self.start_score)
    self.game = Game(self.start_score, self.players, self.sets, self.legs_per_set)

  def switch_thrower(self,thrower):
    if (thrower == self.game.player1):
        thrower = self.game.player2
    else:
        thrower = self.game.player1
    return thrower

  def play_leg(self):
    self.viewer.print_scoreboard(self.game)    
    while not(self.game.won()):
      self.turn(self.game.thrower)
      self.viewer.print_scoreboard(self.game)
      self.game.switch_thrower();

  def display_winner(self,game):
    winner = self.game.winner().name
    print "Game shot, and the %s to %s" %(game, winner)
