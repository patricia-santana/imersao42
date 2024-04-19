        ##all_in.py
import sys

def get_state_of_city(capitals, city):
    for state in capitals:
        if city == capitals[state]:
            return state
    return None

def get_state_name(states, state):
    for name in states:
        if state == states[name]:
            return name
    return None

def search(term):
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
    
    if term in states:
        return f"{term} is a state"
    
    capital = get_state_of_city(capital_cities, term)
    if capital  is not None:
        state = get_state_name(states, capital)
        return f"{term} is the capital of {state}"
    
    return f"{term} is neighter a capital or state"

if (len(sys.argv) != 2):    
    sys.exit(1)

terms = sys.argv[1].split(",")


for term in terms:
    print(search(term))
###fim