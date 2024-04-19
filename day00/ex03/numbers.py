def open_numbers():
    with open("./d00/ex03/numbers.txt", "r") as arquivo:
        numbers = arquivo.read().split(",")
    return numbers


def read_numbers(numbers):
    for number in numbers: 
        print(number)


def main():
    numbers = open_numbers()
    read_numbers(numbers)


if __name__ == '__main__':
    main()