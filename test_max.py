
import unittest
from max import mymax
class TestmaxTestCase(unittest.TestCase):
    def test_mymax(self):
        assert mymax([4, 8, 9]) == 9,"Here is the Max List"