# test_webpackconfig.py
"""
Tests for WebpackConfig module.
"""

import unittest
from webpackconfig import WebpackConfig

class TestWebpackConfig(unittest.TestCase):
    """Test cases for WebpackConfig class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = WebpackConfig()
        self.assertIsInstance(instance, WebpackConfig)
        
    def test_run_method(self):
        """Test the run method."""
        instance = WebpackConfig()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
