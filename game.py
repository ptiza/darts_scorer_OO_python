class Game(object):

  def __init__(self,score, players, sets, legs_per_set):
    self.start_score = score
    self.player1 = players[0]
    self.player2 = players[1]
    self.thrower = self.player1
    self.sets = sets
    self.legs_per_set = legs_per_set

  def switch_thrower(self):
    if (self.thrower == self.player1):
      self.thrower = self.player2
    else:
      self.thrower = self.player1

  def won(self):
    return (self.player1.current_score == 0 or self.player2.current_score == 0)

  def winner(self):
    if (self.player1.current_score == 0):
      return self.player1
    elif (self.player2.current_score == 0):
      return self.player2