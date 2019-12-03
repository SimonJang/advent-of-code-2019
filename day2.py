def execute_operation(operation: int, a: int, b: int) -> int:
    if operation is 1:
        return a + b

    if operation is 2:
        return a * b

    if operation is 99:
        return None

    raise Exception


def day1():
    with open('./data/day2.txt') as file:
        for line in file:
            instructions = line.split(',')
            instructions = [int(instruction) for instruction in instructions]
            instructions[1] = 12
            instructions[2] = 2

            abort = False
            index = 0

            while not abort:
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


day1()
