"""
Test the main module.
Author: Wolf Paulus (wolf@paulus.com)
"""
from unittest import TestCase
from random import randint


class Test(TestCase):

    def test_is_odd_str(self):
        assert type(randint(1, 6)) is int
