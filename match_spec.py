import unittest
from match import Match
from player import Player

class TestMatch(unittest.TestCase):
  
  def setUp(self):
    self.player1 = Player(0, "Jack", 501)
    self.player2 = Player(1, "Victor", 501)

    self.players = [self.player1, self.player2]

    self.match = Match([self.player1.name, self.player2.name], 9, 5, 301)

  def test_sets_needed_to_win(self):
    sets_needed = self.match.sets_needed_to_win()
    self.assertEqual(5, sets_needed)

  def test_legs_needed_to_win_set(self):
    legs_needed = self.match.legs_needed_to_win_set()
    self.assertEqual(3, legs_needed)

  def test_set_won(self):
     self.match.game.players[1].legs_won = 3
     self.match.game.players[1].sets_won = 0
     self.match.game.players[1].current_score = 0
     self.match.game.winner() 
     set_won = self.match.set_won()
     self.assertTrue(set_won)

if __name__ == '__main__':
    unittest.main()