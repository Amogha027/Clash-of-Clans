import unittest

## importing the required classes
import king
import village

level = 1
V = village.createVillage(level)


class TestMove(unittest.TestCase):

    def setUp(self):
        self.king = king.getHero(0)

    def test_attack_target(self):
        
        # check attack of dead king
        self.king.alive = False
        for i in V.wizard_towers:
            tower = V.wizard_tower_objs[i]
            self.king.attack_target(tower, self.king.attack)
            self.assertEqual(tower.health, tower.max_health, "incorrect")
        self.king.alive = True

        # check normal king attack
        for i in V.cannons:
            cannon = V.cannon_objs[i]
            health = cannon.health - self.king.attack
            self.king.attack_target(cannon, self.king.attack)
            self.assertEqual(cannon.health, health, "incorrect decrement")

        # check if the target is destroyed
        for i in V.huts:
            hut = V.hut_objs[i]
            hut.health = self.king.attack / 2
            self.king.attack_target(hut, self.king.attack)
            self.assertEqual(hut.destroyed, True, "incorrect destroy")
            self.assertEqual(hut.health, 0, "incorrect destroy")

        # check for all attributes of the king
        self.assertEqual(self.king.speed, 1, "incorrect")
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

f = open("output_bonus.txt", "w")
if result.wasSuccessful():
    f.write("True")
else:
    f.write("False")
f.close()
