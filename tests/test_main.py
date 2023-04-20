"""
Test the main module.
Author: Wolf Paulus (wolf@paulus.com)
"""
from unittest import TestCase
from random import randint


class Test(TestCase):

    def test_dice_sim(self):
        assert type(randint(1, 6)) is int
        assert randint(1, 8) != 10
