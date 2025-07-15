import unittest
from sort_packages import sort

class TestSortFunction(unittest.TestCase):
    def test_standard(self):
        self.assertEqual(sort(100, 100, 100, 19), "STANDARD")
    
    def test_bulky_only(self):
        self.assertEqual(sort(150, 50, 50, 10), "SPECIAL")

    def test_heavy_only(self):
        self.assertEqual(sort(100, 100, 100, 20), "SPECIAL")

    def test_both(self):
        self.assertEqual(sort(200, 200, 30, 25), "REJECTED")

    def test_neither(self):
        self.assertEqual(sort(50, 50, 50, 5), "STANDARD")

if __name__ == "__main__":
    unittest.main()
