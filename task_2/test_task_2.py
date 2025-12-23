import random
import unittest

from task_2.task_2 import (
    analytic_square_integral,
    average_estimates,
    estimate_integral,
    square_function,
)


class MonteCarloIntegralTest(unittest.TestCase):
    def test_estimate_is_close_to_analytic(self) -> None:
        rng = random.Random(0)
        mc_value = average_estimates(square_function, 0.0, 2.0, 10000, 5, rng)
        analytic_value = analytic_square_integral(0.0, 2.0)
        self.assertLess(abs(mc_value - analytic_value), 0.05)

    def test_deterministic_with_seed(self) -> None:
        rng = random.Random(123)
        first = estimate_integral(square_function, 0.0, 2.0, 5000, rng)
        rng.seed(123)
        second = estimate_integral(square_function, 0.0, 2.0, 5000, rng)
        self.assertAlmostEqual(first, second, places=12)


if __name__ == "__main__":
    unittest.main()
