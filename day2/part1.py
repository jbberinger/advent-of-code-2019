import csv


def process_opcodes(intcode):
    processed_intcode = [*intcode]
    index = 0
    length = len(processed_intcode)
    while index < length:
        opcode = processed_intcode[index]
        if opcode == 99:
            break
        val_1 = processed_intcode[processed_intcode[index + 1]]
        val_2 = processed_intcode[processed_intcode[index + 2]]
        location = processed_intcode[index + 3]
        if opcode == 1:
            processed_intcode[location] = val_1 + val_2
        elif opcode == 2:
            processed_intcode[location] = val_1 * val_2
        index += 4
    return processed_intcode


def main():
    intcode = []
    with open('data.txt', 'r') as data:
        reader = csv.reader(data)
        intcode = list(reader)[0]
        intcode = [int(x) for x in intcode]
    intcode[1] = 12
    intcode[2] = 2
    restored_program = process_opcodes(intcode)
    return restored_program[0]


if __name__ == "__main__":
    print(f'The solution is {main()}.')
