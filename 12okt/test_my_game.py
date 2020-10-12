from unittest import TestCase
from my_game import Ball

class TestBall(TestCase):
    def test_collision_true(self):
        ball1 = Ball(100, 100, 0, 0, (0, 0, 0), 25)
        ball2 = Ball(120, 135, 0, 0, (0, 0, 0), 10)
        self.assertTrue(ball1.collide(ball2))

    def test_collision_false(self):
        ball1 = Ball(100, 100, 0, 0, (0, 0, 0), 25)
        ball2 = Ball(20, 35, 0, 0, (0, 0, 0), 10)
        self.assertFalse(ball1.collide(ball2))

    def test_collision_outside_screen(self):
        ball1 = Ball(-100, 100, 0, 0, (0, 0, 0), 25)
        ball2 = Ball(-80, 135, 0, 0, (0, 0, 0), 10)
        self.assertTrue(ball1.collide(ball2))
