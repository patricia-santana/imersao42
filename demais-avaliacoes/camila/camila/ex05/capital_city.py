import sys

def get_capital(state):
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
    
    if state not in states:
        return "Unknown state"
    else:
        return capital_cities[states[state]]


if (len(sys.argv) != 2):    
    sys.exit(1)

print(get_capital(sys.argv[1]))