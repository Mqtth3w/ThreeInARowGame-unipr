# MATTEO GIANVENUTI
import unittest
from P2_321490 import _3inarow

class _3inarow_Test(unittest.TestCase):
   
    def test_mossa(self):
        matrix = _3inarow((6,6))
        matrix.play_at(0,0)
        self.assertTrue(matrix.value_at(0,0) == "W")
        matrix.play_at(0,0)
        self.assertTrue(matrix.value_at(0,0) == "B")
        
    def test_backtraking_finished(self):
        matrix = _3inarow((10,10))
        matrix.solve_recursive(0)
        self.assertTrue(matrix.finished() == True)
    
    def test_unsolvable(self):
        matrix = _3inarow((6,6))
        matrix.play_at(2,4)
        matrix.play_at(2,4)
        self.assertTrue(matrix.unsolvable() == True)
        
    def test_suggerimenti(self):
        matrix = _3inarow((6,6))
        matrix.suggerimenti()
        self.assertTrue(matrix.value_at(2,4) == "W")
    

if __name__ == '__main__':
    unittest.main()
    
    
    
    