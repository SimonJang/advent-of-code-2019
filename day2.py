def execute_operation(operation: int, a: int, b: int) -> int:
    if operation is 1:
        return a + b

    if operation is 2:
        return a * b

    if operation is 99:
        return None

    print(f"Exception operation: {operation}")
    raise Exception


def day1():
    with open('./data/day2.txt') as file:
        for line in file:
            instructions = line.split(',')
            instructions = [int(instruction) for instruction in instructions]
            instructions[1] = 12
            instructions[2] = 2

            index = 0

            while True:
                operation = instructions[index]
                value_a = instructions[instructions[index + 1]]
                value_b = instructions[instructions[index + 2]]
                store_location = instructions[index + 3]

                if operation is 99:
                    print(f"First number is: {instructions[0]}")
                    break

                result = execute_operation(operation, value_a, value_b)
                instructions[store_location] = result
                index = index + 4


# day1()


def day2():
    with open('./data/day2.txt') as file:
        for line in file:
            instructions = line.split(',')
            instructions = [int(instruction) for instruction in instructions]
            parameters = [tuple([x, y]) for x in range(0, 100) for y in range(0, 100)]

            checksum = 19690720

            for a, b in parameters:
                calculated_instructions = instructions.copy()
                index = 0

                calculated_instructions[1] = a
                calculated_instructions[2] = b

                while True:
                    operation = calculated_instructions[index]
                    value_a = calculated_instructions[calculated_instructions[index + 1]]
                    value_b = calculated_instructions[calculated_instructions[index + 2]]
                    store_location = calculated_instructions[index + 3]

                    result = execute_operation(operation, value_a, value_b)

                    if result is None:
                        if calculated_instructions[0] == checksum:
                            print(f"{calculated_instructions[0]} | {checksum}")
                            print(f"Checksum match: {100 * a + b}")

                        break

                    calculated_instructions[store_location] = result
                    index = index + 4


day2()
