###numbers.py
def main():
    with open("numbers.txt", "r") as file:        
        numbers = file.read().split(",")
        for number in numbers:
            print(number)
        file.close()

main()