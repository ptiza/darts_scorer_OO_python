class Game(object):

  def __init__(self,score, players, sets, legs_per_set):
    self.start_score = score
    self.players = players
    self.thrower = self.players[0]
    self.sets = sets
    self.legs_per_set = legs_per_set
    self.turn = 0

  def switch_thrower(self):
    if (self.thrower == self.players[len(self.players)-1]):
      self.thrower = self.players[0]
      self.turn += 1
    else:
      self.thrower = self.players[self.players.index(self.thrower)+1]

  def won(self):
    for player in self.players:
      if player.current_score == 0:
        return True
    return False

  def winner(self):
    for player in self.players:
      if (player.current_score == 0):
        return player