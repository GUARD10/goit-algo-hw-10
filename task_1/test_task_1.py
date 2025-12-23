import unittest

from task_1.task_1 import build_model, solve_model


class ProductionOptimizationTest(unittest.TestCase):
    def test_solution_optimal(self) -> None:
        model = build_model()
        result = solve_model(model)
        self.assertEqual(result["status"], "Optimal")
        self.assertEqual(int(result["lemonade"]), 30)
        self.assertEqual(int(result["juice"]), 20)
        self.assertEqual(int(result["objective"]), 50)

    def test_constraints_satisfied(self) -> None:
        model = build_model()
        result = solve_model(model)
        lemonade = result["lemonade"]
        juice = result["juice"]
        self.assertLessEqual(2 * lemonade + juice, 100)
        self.assertLessEqual(lemonade, 50)
        self.assertLessEqual(lemonade, 30)
        self.assertLessEqual(2 * juice, 40)


if __name__ == "__main__":
    unittest.main()
