from __future__ import print_function
from throw import Throw
from collections import deque
import os
import pdb


class Viewer(object):

  def print_scoreboard(self, match, game):
    os.system("clear")
    print(self.border_msg("{:<3}").format(game.start_score))
    print("")
    print("Sets", end='')
    print(''.join(['\t{:^8}']*len(game.players)).format(*[player.sets_won for player in game.players]), end='')
    print('\n',end='')  
    print("Legs", end='')
    print(''.join(['\t{:^8}']*len(game.players)).format(*[player.legs_won for player in game.players]), end='')
    print('\n',end='') 
    print('-'*len(game.players)*19)
    print(''.join(["\t{:^7}\t |"]*len(game.players)).format(*[player.name for player in game.players]), end='')
    print('\n',end='') 
    print('-'*len(game.players)*19)
    check = []
    rotation = deque(range(len(game.players)))
    rotation.rotate(match.leg_thrower.idx*(len(game.players)-1))

    for player in game.players:
        check.append(len(player.scores)) 
    for i in range(min(check)):   
      print(''.join(["\t{:^7}\t |"]*len(game.players)).format(*[player.scores[i] for player in game.players]), end='')
      print('\n',end='')
    tmp_score = ['   ']*len(game.players)
    for player in list(rotation):
      if check[player] == max(check) and max(check) > 0:
        tmp_score[player] = game.players[player].scores[max(check)-1]
    if max(check) != min(check):    
      print(''.join(["\t{:^7}\t |"]*len(game.players)).format(*tmp_score), end='')
      print('\n',end='')

      

  def get_score(self, player):
    #print player.name + " score: "
    try:
      score = int(raw_input("%s's score: " %(player.name)))
      return score
    except ValueError:
      print("Please enter valid score!")

  def get_player_number(self):
    #print 'Start score: '
    playernumber = int(raw_input("No. of Players: "))
    return playernumber

  def get_player_name(self,player_number):
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
      print ("{:s}, you require {:d}".format(player.name,player.current_score))

  def check_if_bust(self, player, player_throw):
    if (player.is_bust(player_throw)):
      print("BUST!")
      #sleep 1

  def winner(self, player):
    print("Game shot, and the leg, to {:s}!".format(player.name))

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

  def border_msg(self, msg):

      count = len(msg) + 10 # dash will need +2 too

      dash = "-"*count 

      return "+{dash}+\n|\t{msg}\t|\n+{dash}+".format(dash=dash,msg=msg)