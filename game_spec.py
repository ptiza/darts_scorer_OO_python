import unittest
from player import Player
from game import Game

class TestGame(unittest.TestCase):
  
  def setUp(self):
    self.player1 = Player("Jack", 501)
    self.player2 = Player("Victor", 501)

    self.players = [self.player1, self.player2]
    self.game = Game(501,self.players,3,5)

  def test_game_start_score_is_set(self):
    self.assertEqual(501, self.game.start_score)

  def test_game_thrower_player_1(self):
    self.assertEqual(self.player1, self.game.thrower)

  def test_switch_thrower_to_player2(self):
    self.game.switch_thrower()
    self.assertEqual(self.player2, self.game.thrower)

  def test_game_won_false(self):
    self.assertFalse(self.game.won())

  def test_game_won_true(self):
    self.game.player1.current_score = 0
    self.assertTrue(self.game.won())


if __name__ == '__main__':
  unittest.main()