class Player(object):

  def __init__(self, name, score):
    self.name = name
    self.current_score = score
    self.scores = [] 
    self.legs_won = 0
    self.sets_won = 0 

  def reset(self,score):
    self.current_score = score
    self.scores = [] 
  
  def throw_darts(self, player_throw):
    if (player_throw.is_valid() and not(self.is_bust(player_throw))):
      self.current_score -= player_throw.score
      self.scores.append(self.current_score)

  def is_bust(self, player_throw):
    temp = self.current_score - player_throw.score
    return (temp < 0 or temp == 1)
  
  def is_winning_throw(self,player_throw):
    return (self.is_on_a_finish() and player_throw.is_valid() and player_throw.score == self.current_score)

  def is_on_a_finish(self):
    big_finishes = [170, 167, 164, 161, 160]
    if self.current_score in big_finishes:
      return True
    elif self.current_score < 159:
      return True
    else:
      return False