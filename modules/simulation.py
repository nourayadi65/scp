
def calculate_water_balance(
    initial_water,
    rainfall,
    inflow,
    evaporation,
    outflow
):
    """
    Calculate the water balance of Sebkha Sejoumi.

    All inputs must use the same volume unit.
    """

    values = {
        "initial_water": initial_water,
        "rainfall": rainfall,
        "inflow": inflow,
        "evaporation": evaporation,
        "outflow": outflow
    }

    for name, value in values.items():
        if not isinstance(value, (int, float)):
            raise TypeError(f"{name} must be a number")

        if value < 0:
            raise ValueError(f"{name} cannot be negative")

    water_change = rainfall + inflow - evaporation - outflow

    final_water = initial_water + water_change

    water_deficit = max(0, -final_water)

    return {
        "initial_water": initial_water,
        "water_change": water_change,
        "final_water": max(0, final_water),
        "water_deficit": water_deficit
    }


def run_scenario(
    initial_water,
    rainfall,
    inflow,
    evaporation,
    outflow
):
    """
    Run one water-balance scenario.
    """

    results = calculate_water_balance(
        initial_water=initial_water,
        rainfall=rainfall,
        inflow=inflow,
        evaporation=evaporation,
        outflow=outflow
    )

    return results
