import math


def day1():
    total_fuel_requirement = 0

    with open('./data/day1.txt') as data:
        for line in data:
            module_value = int(line)
            fuel_requirement = math.floor(module_value / 3) - 2
            total_fuel_requirement += fuel_requirement

    print(f"Total fuel requirement: {total_fuel_requirement}")


day1()
