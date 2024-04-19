###state.py
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

def get_state(city):
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
    
    state = get_state_of_city(capital_cities, city)
    if state == None:
        return "Unknown capital city"
    else:
        return get_state_name(states, state)        

if (len(sys.argv) != 2):    
    sys.exit(1)

print(get_state(sys.argv[1]))
