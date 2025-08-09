# test_geofencingservice.py
"""
Tests for GeofencingService module.
"""

import unittest
from geofencingservice import GeofencingService

class TestGeofencingService(unittest.TestCase):
    """Test cases for GeofencingService class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = GeofencingService()
        self.assertIsInstance(instance, GeofencingService)
        
    def test_run_method(self):
        """Test the run method."""
        instance = GeofencingService()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
