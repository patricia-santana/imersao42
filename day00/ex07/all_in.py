import sys

def states_city(lugares):
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
    
    lugares_split = [lugar for lugar in lugares[0].split(",")]
    lugares_strip = [lugar.strip() for lugar in lugares_split]
    lugares_cap = [lugar.title() for lugar in lugares_strip]

    for lugar in lugares_cap:
        value_check = False
        if lugar != '':
            for (key1, value1),(key2, value2) in zip(states.items(), capital_cities.items()):
                if key1 == lugar:
                    print(value2, "is the capital of ", key1)
                    value_check = True
                else:
                    if value2 == lugar:
                        for chave, valor in states.items():
                            if key2 == valor:
                                print(value2, "is the capital of ", key1)
                                value_check = True
            if not value_check:
                print(lugar, "is neither a capital city nor a state")


def main():
    lugares = sys.argv
    del(lugares[0])
    if len(lugares) == 1:
        states_city(lugares)

if __name__ == '__main__':
    main()