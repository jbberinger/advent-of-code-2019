import csv


def process_opcodes(intcode):
    processed_intcode = [*intcode]
    index = 0
    length = len(processed_intcode)

    while index < length:
        opcode = processed_intcode[index]
        val_1 = processed_intcode[processed_intcode[index + 1]]
        val_2 = processed_intcode[processed_intcode[index + 2]]
        location = processed_intcode[index + 3]
        if opcode == 99:
            break
        if opcode == 1:
            processed_intcode[location] = val_1 + val_2
        elif opcode == 2:
            processed_intcode[location] = val_1 * val_2
        index += 4

    return processed_intcode


def main():
    intcode = []
    expected_solution = 19690720

    with open('data.txt', 'r') as data:
        reader = csv.reader(data)
        intcode = [int(x) for x in list(reader)[0]]

    for noun in range(0, 100):
        for verb in range(0, 100):
            new_intcode = [*intcode]
            new_intcode[1] = noun
            new_intcode[2] = verb
            restored_program = process_opcodes(new_intcode)
            if restored_program[0] == expected_solution:
                return 100 * noun + verb

    return None


if __name__ == "__main__":
    print(f'The solution is {main()}.')
