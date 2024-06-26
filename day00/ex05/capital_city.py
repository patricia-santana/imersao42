import sys

def capital_city():
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
    
    if len(sys.argv) == 2:
        state = sys.argv[1]
    else:
        return " "

    if state in states: 
        print(capital_cities[states[state]])
    else:
        print("Unknown state")

if __name__ == '__main__':
    capital_city()