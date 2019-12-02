import math


def fuel_required(mass):
    return math.floor(mass / 3) - 2


def main():
    total_fuel_requirements = 0
    with open('data.txt') as data:
        module_mass = data.readline()
        while module_mass:
            total_fuel_requirements += fuel_required(int(module_mass))
            module_mass = data.readline()
    return total_fuel_requirements


if __name__ == "__main__":
    print(f'The sum of the fuel requirements is {main()}.')
