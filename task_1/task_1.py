import pulp


def build_model() -> pulp.LpProblem:
    model = pulp.LpProblem("Maximize_Drinks", pulp.LpMaximize)
    lemonade = pulp.LpVariable("lemonade", lowBound=0, cat="Integer")
    juice = pulp.LpVariable("juice", lowBound=0, cat="Integer")

    model += lemonade + juice, "Total_Output"
    model += 2 * lemonade + juice <= 100, "Water"
    model += lemonade <= 50, "Sugar"
    model += lemonade <= 30, "Lemon_Juice"
    model += 2 * juice <= 40, "Fruit_Puree"
    return model


def solve_model(model: pulp.LpProblem) -> dict[str, float]:
    status_code = model.solve(pulp.PULP_CBC_CMD(msg=False))
    variables = model.variablesDict()
    return {
        "status": pulp.LpStatus[status_code],
        "lemonade": variables["lemonade"].varValue,
        "juice": variables["juice"].varValue,
        "objective": pulp.value(model.objective),
    }


def run_demo() -> None:
    model = build_model()
    result = solve_model(model)
    lemonade = int(result["lemonade"])
    juice = int(result["juice"])
    total = int(result["objective"])

    initial_stock = {"water": 100, "sugar": 50, "lemon_juice": 30, "fruit_puree": 40}
    used = {
        "water": 2 * lemonade + 1 * juice,
        "sugar": 1 * lemonade,
        "lemon_juice": 1 * lemonade,
        "fruit_puree": 2 * juice,
    }
    remaining = {k: initial_stock[k] - used[k] for k in initial_stock}

    print("Status:", result["status"])
    print("Initial stock:", initial_stock)
    print("Optimal production:")
    print("  Lemonade:", lemonade)
    print("  Fruit juice:", juice)
    print("Total drinks:", total)
    print("Resource usage:")
    for res, amount in used.items():
        print(f"  {res}: {amount} used")
    print("Remaining stock:")
    for res, amount in remaining.items():
        print(f"  {res}: {amount} left")


if __name__ == "__main__":
    run_demo()
