"""
Tests unitaires pour la classe SimpleMath.
"""

import unittest
from simple_math import SimpleMath

class TestSimpleMath(unittest.TestCase):
    """
    Tests unitaires pour les opérations d'addition et de soustraction.
    """
    def test_addition(self):
        """
        Test de la méthode addition.
        """
        self.assertEqual(SimpleMath.addition(2, 3), 5)
    
    def test_soustraction(self):
        """
        Test de la méthode soustraction.
        """
        self.assertEqual(SimpleMath.soustraction(5, 3), 2)

if __name__ == '__main__':
    unittest.main()

