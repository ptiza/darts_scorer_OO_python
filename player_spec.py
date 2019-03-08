import unittest
from player import Player
from throw import Throw

class TestPlayer(unittest.TestCase):

  def test_player_name_is_set(self):
    player = Player(0, 'Phil', 100)
    self.assertEqual('Phil', player.name)

  def test_player_score_is_set(self):
    player = Player(0, 'Phil', 100)
    self.assertEqual(100, player.current_score)

  def test_player_sets_won_is_zero(self):
    player = Player(0, 'Phil', 100)
    self.assertEqual(0, player.sets_won)

  def test_player_legs_won_is_zero(self):
    player = Player(0, 'Phil', 100)
    self.assertEqual(0, player.legs_won)

  def test_player_throw_updates_score(self):
    player = Player(0, 'Phil', 501)
    player_throw = Throw(180)
    player.throw_darts(player_throw)
    self.assertEqual(321, player.current_score)

  def test_player_is_bust_when_throw_greater_than_current_score(self):
    player = Player(0, 'Phil', 100)
    player_throw = Throw(120)
    self.assertTrue(player.is_bust(player_throw))

  def test_player_is_bust_when_throw_is_one_less_than_current_score(self):
    player = Player(0, 'Phil', 100)
    player_throw = Throw(99)
    self.assertTrue(player.is_bust(player_throw))

  def test_player_score_does_not_change_when_busted(self):
    player = Player(0, 'Phil', 100)
    player_throw = Throw(120)
    player.throw_darts(player_throw)
    self.assertEqual(100, player.current_score)

  def test_player_throws_winning_score(self):
    player = Player(0, 'Phil', 100)
    player_throw = Throw(100)
    self.assertTrue(player.is_winning_throw(player_throw))

  def test_player_throws_winning_score_results_in_zero_score(self):
    player = Player(0, 'Phil', 100)
    player_throw = Throw(100)
    self.assertTrue(player.is_winning_throw(player_throw))
    player.throw_darts(player_throw)
    self.assertEqual(0,player.current_score)

  def test_player_does_not_throw_winning_score(self):
    player = Player(0, 'Phil', 100)
    player_throw = Throw(80)
    self.assertFalse(player.is_winning_throw(player_throw))
    player.throw_darts(player_throw)
    self.assertEqual(20,player.current_score)

  def test_100_is_a_finish(self):
    player = Player(0, 'Phil', 100)
    self.assertTrue(player.is_on_a_finish())

  def test_180_is_not_a_finish(self):
    player = Player(0, 'Phil', 180)
    self.assertFalse(player.is_on_a_finish())

  def test_170_is_a_finish(self):
    player = Player(0, 'Phil', 170)
    self.assertTrue(player.is_on_a_finish())

  def test_167_is_a_finish(self):
    player = Player(0, 'Phil', 167)
    self.assertTrue(player.is_on_a_finish())

  def test_164_is_a_finish(self):
    player = Player(0, 'Phil', 164)
    self.assertTrue(player.is_on_a_finish())

  def test_161_is_a_finish(self):
    player = Player(0, 'Phil', 161)
    self.assertTrue(player.is_on_a_finish())

  def test_160_is_a_finish(self):
    player = Player(0, 'Phil', 160)
    self.assertTrue(player.is_on_a_finish())

  def test_159_is_not_a_finish(self):
    player = Player(0, 'Phil', 159)
    self.assertFalse(player.is_on_a_finish())

  def test_162_is_not_a_finish(self):
    player = Player(0, 'Phil', 162)
    self.assertFalse(player.is_on_a_finish())

  def test_171_is_not_a_finish(self):
    player = Player(0, 'Phil', 171)
    self.assertFalse(player.is_on_a_finish())

if __name__ == '__main__':
    unittest.main()