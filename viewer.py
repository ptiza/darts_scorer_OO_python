from throw import Throw
import os
import pdb


class Viewer(object):

  def print_scoreboard(self, game):
    os.system("clear")
    print "\t     %s Sets %s" %(game.player1.sets_won, game.player2.sets_won)
    print "\t     %s Legs %s" %(game.player1.legs_won, game.player2.legs_won)
    print "\t\t%s" %(game.start_score)
    print "\t%s\t |\t%s" %(game.player1.name, game.player2.name)
    print "-----------------------------------"

    for i in range(len(game.player1.scores)):
      #pdb.set_trace()
      if (len(game.player2.scores)) <= i:
        print "\t%s\t |" %(game.player1.scores[i])
      else:
        #pdb.set_trace()
        print "\t%s\t |\t %s" %(game.player1.scores[i], game.player2.scores[i])
    print ""

  def get_score(self, player):
    #print player.name + " score: "
    score = int(raw_input("%s's score: " %(player.name)))
    return score

  def get_player_name(self,player_number):
    #print "Player %s:" %(player_number)
    player = raw_input("Player %s: " %(player_number))
    return player

  def get_start_score(self):
    #print 'Start score: '
    start_score = int(raw_input("Start score: "))
    return start_score

  def get_number_of_sets(self):
    number_of_sets = 0
    while ((number_of_sets %2) == 0):
      number_of_sets = int(raw_input("How many sets ?(must be an odd number) "))
    return number_of_sets   

  def get_number_of_legs_per_set(self):
    number_of_legs_per_set = 0
    while ((number_of_legs_per_set %2) == 0):
       number_of_legs_per_set = int(raw_input("How many legs per set (must be an odd number)? "))
    return number_of_legs_per_set   

  def check_if_on_a_finish(self, player):
    if player.is_on_a_finish():
      print  "%s, you require %s" %(player.name,player.current_score)

  def check_if_bust(self, player, player_throw):
    if (player.is_bust(player_throw)):
      print "BUST!"
      #sleep 1

  def winner(self, player):
    print "Game shot, and the leg, to %s!" %(player.name)

  def check_for_winning_throw(self, player, player_throw):
    if (player.is_winning_throw(player_throw)):
      self.winner(player)

  def get_throw_score(self, player):
    score = self.get_score(player)
    player_throw = Throw(score)
    return player_throw

  def get_throw(self, player):
    player_throw = self.get_throw_score(player)
    while not(player_throw.is_valid()):
      player_throw = self.get_throw_score(player)
    return player_throw
