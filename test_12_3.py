# ЗАДАНИЕ ПО ТЕМЕ "Простые Юнит-Тесты"

import unittest
from runner import Runner


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        """
        Тест для проверки функции run класса Runner
        :return:
        """
        run1 = Runner('Alex')
        for i in range(10):
            run1.walk()
        self.assertEqual(run1.distance, 50, f'Для {run1} расстояние должно быть равно 50')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        """
        Тест для проверки функции walk класса Runner
        :return:
        """
        run2 = Runner('Max')

        for i in range(10):
            run2.run()
        self.assertEqual(run2.distance, 100, f'Для {run2} расстояние должно быть равно 100')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        """
        Тест для проверки неравенства результатов функций run и walk
        :return:
        """
        run1 = Runner('Alex')
        run2 = Runner('Max')
        for i in range(10):
            run1.run()
            run2.walk()
        self.assertNotEqual(run1.distance, run2.distance)


if __name__ == '__main__':
    unittest.main()