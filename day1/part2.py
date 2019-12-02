import math


def fuel_required(mass):
    fuel = math.floor(mass / 3) - 2
    total_fuel = 0
    while fuel >= 0:
        total_fuel += fuel
        fuel = math.floor(fuel / 3) - 2
    return total_fuel


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
