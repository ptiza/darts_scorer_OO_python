import unittest
from throw import Throw

class TestThrow(unittest.TestCase):
  def test_score_is_set(self):
    t = Throw(180)
    self.assertEqual(180, t.score)

  def test_180_is_valid_throw(self):
    t = Throw(180)
    self.assertTrue(t.is_valid())

  def test_181_is_invalid_throw(self):
    t = Throw(181)
    self.assertFalse(t.is_valid())

  def test_100_is_valid_throw(self):
    t = Throw(100)
    self.assertTrue(t.is_valid())

  def test_0_is_valid_throw(self):
    t = Throw(0)
    self.assertTrue(t.is_valid())

  def test_163_is_invalid_throw(self):
    t = Throw(163)
    self.assertFalse(t.is_valid())

  def test_164_is_valid_throw(self):
    t = Throw(164)
    self.assertTrue(t.is_valid())

  def test_minus_10_is_invalid_throw(self):
    t = Throw(-10)
    self.assertFalse(t.is_valid())

if __name__ == '__main__':
    unittest.main()