# test_nftsmartcontractgenerator.py
"""
Tests for NftSmartContractGenerator module.
"""

import unittest
from nftsmartcontractgenerator import NftSmartContractGenerator

class TestNftSmartContractGenerator(unittest.TestCase):
    """Test cases for NftSmartContractGenerator class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NftSmartContractGenerator()
        self.assertIsInstance(instance, NftSmartContractGenerator)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NftSmartContractGenerator()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
