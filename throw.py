class Throw(object):

  def __init__(self,score):
    self.score = score
  
  def is_valid(self):
    valid_high_scores = [180, 177, 174, 171, 170, 167, 165, 164]
    if self.score in valid_high_scores:
      return True
    elif ((self.score >= 0) and (self.score < 163)):
      return True
    else:
      return False