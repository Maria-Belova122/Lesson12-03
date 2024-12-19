# ЗАДАНИЕ ПО ТЕМЕ "Простые Юнит-Тесты"

import unittest
import runner_and_tournament as rt


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = []  # Список словарей с результатами соревнований

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def setUp(self):
        self.runner1 = rt.Runner('Усэйн', 10)
        self.runner2 = rt.Runner('Андрей', 9)
        self.runner3 = rt.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for tour_result in cls.all_results:
            print(tour_result)

    def test_start1(self):
        tournament = rt.Tournament(90, self.runner1, self.runner3)
        list_runner = list(vars(tournament).values())[1]
        runner_min_speed = min(list_runner, key=lambda x: x.speed)
        tour_result = tournament.start()
        last_place = max(tour_result.keys())
        self.assertTrue(tour_result[last_place] == runner_min_speed.name)
        self.all_results.append(tour_result)

    def test_start2(self):
        tournament = rt.Tournament(90, self.runner2, self.runner3)
        list_runner = list(vars(tournament).values())[1]
        runner_min_speed = min(list_runner, key=lambda x: x.speed)
        tour_result = tournament.start()
        last_place = max(tour_result.keys())
        self.assertTrue(tour_result[last_place] == runner_min_speed.name)
        self.all_results.append(tour_result)

    def test_start3(self):
        tournament = rt.Tournament(90, self.runner1, self.runner2, self.runner3)
        list_runner = list(vars(tournament).values())[1]
        runner_min_speed = min(list_runner, key=lambda x: x.speed)
        tour_result = tournament.start()
        last_place = max(tour_result.keys())
        self.assertTrue(tour_result[last_place] == runner_min_speed.name)
        self.all_results.append(tour_result)


if __name__ == '__main__':
    unittest.main()
