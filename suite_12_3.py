# ЗАДАНИЕ ПО ТЕМЕ "Систематизация и пропуск тестов"

import unittest
import test_12_3
import test_12_3_1

runST = unittest.TestSuite()
runST.addTest(unittest.TestLoader().loadTestsFromTestCase(test_12_3.RunnerTest))
runST.addTest(unittest.TestLoader().loadTestsFromTestCase(test_12_3_1.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(runST)


