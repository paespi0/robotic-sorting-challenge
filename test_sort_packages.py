import unittest
from sort_packages import sort

class TestSortFunction(unittest.TestCase):
    def test_standard(self):
        # Package that is neither bulky nor heavy
        self.assertEqual(sort(50, 50, 50, 10), "STANDARD")
    
    def test_bulky_by_dimension(self):
        # Package is bulky because one dimension >= 150cm
        self.assertEqual(sort(150, 50, 50, 10), "SPECIAL")
    
    def test_bulky_by_volume(self):
        # Package is bulky because volume >= 1,000,000 cm³
        self.assertEqual(sort(100, 100, 100, 10), "SPECIAL")

    def test_heavy_only(self):
        # Package is heavy but not bulky
        self.assertEqual(sort(50, 50, 50, 25), "SPECIAL")

    def test_both_heavy_and_bulky_dimension(self):
        # Package is both heavy and bulky (dimension >= 150cm)
        self.assertEqual(sort(200, 50, 50, 25), "REJECTED")
    
    def test_both_heavy_and_bulky_volume(self):
        # Package is both heavy and bulky (volume >= 1,000,000 cm³)
        self.assertEqual(sort(100, 100, 100, 25), "REJECTED")

    def test_edge_case_exactly_heavy(self):
        # Package is exactly 20kg (edge case)
        self.assertEqual(sort(50, 50, 50, 20), "SPECIAL")
    
    def test_edge_case_exactly_bulky_volume(self):
        # Package volume is exactly 1,000,000 cm³
        self.assertEqual(sort(100, 100, 100, 5), "SPECIAL")
    
    def test_edge_case_exactly_bulky_dimension(self):
        # Package dimension is exactly 150cm
        self.assertEqual(sort(150, 50, 50, 5), "SPECIAL")
    
    def test_edge_case_just_under_limits(self):
        # Package just under all limits
        self.assertEqual(sort(99, 99, 99, 19.9), "STANDARD")

if __name__ == "__main__":
    unittest.main()
