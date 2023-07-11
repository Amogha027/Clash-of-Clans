import unittest

## importing the required classes
import king
import points as pt
import village

level = 1
V = village.createVillage(level)


class TestMove(unittest.TestCase):

    def setUp(self):
        self.king = king.getHero(0)

    def test_runUp(self):

        # check movement of dead king
        self.king.alive = False
        self.king.position = [17, 35]
        self.king.speed = 1
        final = [17, 35]
        self.king.move("up", V)
        self.assertEqual(self.king.position, final, "incorrect upward movement")
        self.king.alive = True

        # check normal upward movement and pt.HERO_POS
        self.king.position = [17, 35]
        self.king.speed = 5
        final = [12, 35]
        self.king.move("up", V)
        self.assertEqual(self.king.position, final, "incorrect upward movement")
        self.assertEqual(pt.HERO_POS, final, "incorrect")

        # check out of bound case and king.facing
        self.king.position = [1, 35]
        self.king.speed = 4
        final = [0, 35]
        self.king.move("up", V)
        self.assertEqual(self.king.position, final, "incorrect upward movement")
        self.assertEqual(self.king.facing, 'up', "incorrect")

        # check obstacle in the way case 
        self.king.position = [4, 12]
        self.king.speed = 3
        final = [4, 12]
        self.king.move("up", V)
        self.assertEqual(self.king.position, final, "incorrect upward movement")

        # check for all attributes of the king
        self.assertEqual(self.king.speed, 3, "incorrect")
        self.assertEqual(self.king.health, 100, "incorrect")
        self.assertEqual(self.king.max_health, 100, "incorrect")
        self.assertEqual(self.king.attack, 30, "incorrect")
        self.assertEqual(self.king.AoE, 10, "incorrect")
        self.assertEqual(self.king.attack_radius, 3, "incorrect")
        self.assertEqual(self.king.alive, True, "incorrect")

    def test_runDown(self):

        # check movement of dead king
        self.king.alive = False
        self.king.position = [12, 35]
        self.king.speed = 1
        final = [12, 35]
        self.king.move("down", V)
        self.assertEqual(self.king.position, final, "incorrect downward movement")
        self.king.alive = True

        # check normal downward movement and pt.HERO_POS
        self.king.position = [12, 35]
        self.king.speed = 4
        final = [16, 35]
        self.king.move("down", V)
        self.assertEqual(self.king.position, final, "incorrect downward movement")
        self.assertEqual(pt.HERO_POS, final, "incorrect")

        # check out of bound case and king.facing
        self.king.position = [15, 35]
        self.king.speed = 4
        final = [17, 35]
        self.king.move("down", V)
        self.assertEqual(self.king.position, final, "incorrect downward movement")
        self.assertEqual(self.king.facing, 'down', "incorrect")

        # check obstacle in the way case 
        self.king.position = [2, 14]
        self.king.speed = 3
        final = [2, 14]
        self.king.move("down", V)
        self.assertEqual(self.king.position, final, "incorrect downward movement")

        # check for all attributes of the king
        self.assertEqual(self.king.speed, 3, "incorrect")
        self.assertEqual(self.king.health, 100, "incorrect")
        self.assertEqual(self.king.max_health, 100, "incorrect")
        self.assertEqual(self.king.attack, 30, "incorrect")
        self.assertEqual(self.king.AoE, 10, "incorrect")
        self.assertEqual(self.king.attack_radius, 3, "incorrect")
        self.assertEqual(self.king.alive, True, "incorrect")

    def test_runLeft(self):

        # check movement of dead king
        self.king.alive = False
        self.king.position = [17, 35]
        self.king.speed = 1
        final = [17, 35]
        self.king.move("left", V)
        self.assertEqual(self.king.position, final, "incorrect leftward movement")
        self.king.alive = True

        # check normal leftward movement and pt.HERO_POS
        self.king.position = [1, 35]
        self.king.speed = 4
        final = [1, 31]
        self.king.move("left", V)
        self.assertEqual(self.king.position, final, "incorrect leftward movement")
        self.assertEqual(pt.HERO_POS, final, "incorrect")

        # check out of bound case and king.facing
        self.king.position = [1, 2]
        self.king.speed = 4
        final = [1, 0]
        self.king.move("left", V)
        self.assertEqual(self.king.position, final, "incorrect leftward movement")
        self.assertEqual(self.king.facing, 'left', "incorrect")

        # check obstacle in the way case 
        self.king.position = [11, 7]
        self.king.speed = 3
        final = [11, 6]
        self.king.move("left", V)
        self.assertEqual(self.king.position, final, "incorrect leftward movement")

        # check for all attributes of the king
        self.assertEqual(self.king.speed, 3, "incorrect")
        self.assertEqual(self.king.health, 100, "incorrect")
        self.assertEqual(self.king.max_health, 100, "incorrect")
        self.assertEqual(self.king.attack, 30, "incorrect")
        self.assertEqual(self.king.AoE, 10, "incorrect")
        self.assertEqual(self.king.attack_radius, 3, "incorrect")
        self.assertEqual(self.king.alive, True, "incorrect")

    def test_runRight(self):

        # check movement of dead king
        self.king.alive = False
        self.king.position = [1, 30]
        self.king.speed = 1
        final = [1, 30]
        self.king.move("right", V)
        self.assertEqual(self.king.position, final, "incorrect rightward movement")
        self.king.alive = True

        # check normal rightward movement and pt.HERO_POS
        self.king.position = [1, 30]
        self.king.speed = 4
        final = [1, 34]
        self.king.move("right", V)
        self.assertEqual(self.king.position, final, "incorrect rightward movement")
        self.assertEqual(pt.HERO_POS, final, "incorrect")

        # check out of bound case and king.facing
        self.king.position = [1, 32]
        self.king.speed = 4
        final = [1, 35]
        self.king.move("right", V)
        self.assertEqual(self.king.position, final, "incorrect rightward movement")
        self.assertEqual(self.king.facing, 'right', "incorrect")

        # check obstacle in the way case 
        self.king.position = [11, 2]
        self.king.speed = 3
        final = [11, 3]
        self.king.move("right", V)
        self.assertEqual(self.king.position, final, "incorrect rightward movement")

        # check for all attributes of the king
        self.assertEqual(self.king.speed, 3, "incorrect")
        self.assertEqual(self.king.health, 100, "incorrect")
        self.assertEqual(self.king.max_health, 100, "incorrect")
        self.assertEqual(self.king.attack, 30, "incorrect")
        self.assertEqual(self.king.AoE, 10, "incorrect")
        self.assertEqual(self.king.attack_radius, 3, "incorrect")
        self.assertEqual(self.king.alive, True, "incorrect")

# unittest.main()
suite = unittest.TestLoader().loadTestsFromTestCase(TestMove)
runner = unittest.TextTestRunner()
result = runner.run(suite)

f = open("output.txt", "w")
if result.wasSuccessful():
    f.write("True")
else:
    f.write("False")
f.close()
