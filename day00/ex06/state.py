import sys

def states_city(capital):
    states = {
        "Oregon" : "OR",
        "Alabama" : "AL",
        "New Jersey": "NJ",
        "Colorado" : "CO"
        }
    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
        }

    for key, value in capital_cities.items():
        if value == capital:
            for chave, valor in states.items():
                if key == valor:
                    print(chave)
                    return True
    return False


def main():
    if len(sys.argv) == 2:
        capital = sys.argv[1]
    else:
        return " "
    value_check = states_city(capital)

    if not value_check:
        print("Unknown capital")

if __name__ == '__main__':
    main()