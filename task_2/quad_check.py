import random
from typing import Callable, Tuple

import scipy.integrate as spi

try:
    from task_2.task_2 import (
        average_estimates,
        square_function,
        analytic_square_integral,
    )
except ImportError:
    import sys
    from pathlib import Path

    sys.path.append(str(Path(__file__).resolve().parent))
    from task_2 import (
        average_estimates,
        square_function,
        analytic_square_integral,
    )


def quad_integral(func: Callable[[float], float], bounds: Tuple[float, float]) -> Tuple[float, float]:
    a, b = bounds
    result, error = spi.quad(func, a, b)
    return result, error


def run_demo() -> None:
    a, b = 0.0, 2.0
    samples = 50_000
    experiments = 5
    rng = random.Random(0)

    mc_value = average_estimates(square_function, a, b, samples, experiments, rng)
    analytic_value = analytic_square_integral(a, b)
    quad_value, quad_error = quad_integral(square_function, (a, b))

    print("Function: f(x) = x^2")
    print(f"Bounds: [{a}, {b}]")
    print("Monte Carlo estimate:", mc_value)
    print("Analytic value:", analytic_value)
    print("SciPy quad value:", quad_value)
    print("SciPy reported abs error:", quad_error)
    print("Error MC vs analytic:", abs(mc_value - analytic_value))
    print("Error MC vs quad:", abs(mc_value - quad_value))
    print("Error quad vs analytic:", abs(quad_value - analytic_value))
    print("Comparison summary:")
    print("  MC is within {:.6f} of analytic".format(abs(mc_value - analytic_value)))
    print("  MC is within {:.6f} of quad".format(abs(mc_value - quad_value)))
    print("  Quad matches analytic within {:.6e}".format(abs(quad_value - analytic_value)))


if __name__ == "__main__":
    run_demo()
