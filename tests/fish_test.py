import unittest
from src.fish import Fish

class TestFish(unittest.TestCase):
    def setUp(self):
        self.nemo = Fish("Nemo", "small", "Clown Fish")

    def test_fish_has_name(self):
        self.assertEqual("Nemo", self.nemo.name)