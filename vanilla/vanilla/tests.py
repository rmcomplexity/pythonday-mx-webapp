"""
.. module:: vanilla.tests
   synopsis: Vanilla tests
"""
from django.test import TestCase


class VanillaTest(TestCase):
    """Vanilla Test"""

    def test_random_var(self):
        """Test for the sake of testing."""
        value = False
        self.assertFalse(value)
