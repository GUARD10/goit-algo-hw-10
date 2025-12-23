import random
from typing import Callable, Iterable


def estimate_integral(
    func: Callable[[float], float],
    a: float,
    b: float,
    samples: int,
    rng: random.Random | None = None,
) -> float:
    generator = rng or random
    width = b - a
    values = (func(generator.uniform(a, b)) for _ in range(samples))
    return width * sum(values) / samples


def average_estimates(
    func: Callable[[float], float],
    a: float,
    b: float,
    samples: int,
    experiments: int,
    rng: random.Random | None = None,
) -> float:
    generator = rng or random
    return sum(
        estimate_integral(func, a, b, samples, generator)
        for _ in range(experiments)
    ) / experiments


def square_function(x: float) -> float:
    return x * x


def analytic_square_integral(a: float, b: float) -> float:
    return (b ** 3 - a ** 3) / 3


def run_demo() -> None:
    a, b = 0.0, 2.0
    samples = 50_000
    experiments = 5
    rng = random.Random(0)
    mc_value = average_estimates(square_function, a, b, samples, experiments, rng)
    analytic_value = analytic_square_integral(a, b)
    error = abs(mc_value - analytic_value)
    print("Function: f(x) = x^2")
    print(f"Bounds: [{a}, {b}]")
    print("Samples per experiment:", samples)
    print("Experiments:", experiments)
    print("Monte Carlo estimate:", mc_value)
    print("Analytic value:", analytic_value)
    print("Absolute error:", error)


if __name__ == "__main__":
    run_demo()
