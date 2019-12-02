import math


def calculate_fuel(weight: int) -> int:
    return math.floor(weight / 3) - 2


def calculate_total_weight(weight: int, total: int) -> int:
    new_weight = calculate_fuel(weight)

    if new_weight > 0:
        new_total = total + new_weight

        return calculate_total_weight(new_weight, new_total)

    return total


def day1():
    total_fuel_requirement = 0

    with open('./data/day1.txt') as data:
        for line in data:
            module_value = int(line)
            fuel_requirement = calculate_fuel(module_value)
            total_fuel_requirement += fuel_requirement

    print(f"Total fuel requirement: {total_fuel_requirement}")


day1()


def day2():
    total_fuel_required = 0

    with open('./data/day1.txt') as data:
        for line in data:
            module_value = int(line)
            module_fuel_requirement = calculate_fuel(module_value)
            fuel_requirement = calculate_total_weight(module_fuel_requirement, 0)

            total_fuel_required += module_fuel_requirement + fuel_requirement

    print(f"Total fuel requirement (with fuel weight included): {total_fuel_required}")


day2()
