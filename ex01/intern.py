class Intern:
    def __init__(self, name = "My name? I'm nobody, an intern, I have no name."):
        self.name = name
        

    def __str__(self):
        return self.name
    
    def work(self):
        raise Exception("I'm just an intern, I can't do that...")
    
    def make_coffee(self):
        return Coffee()

class Coffee:
    def __str__(self):
        return "This is the worst coffee you ever tasted."


if __name__ == "__main__":
    intern1 = Intern()
    intern2 = Intern("Mark")

    print(str(intern1))
    print(str(intern2))

print(str(intern2.make_coffee()))

try:
    intern1.work()
except Exception as e:
    print(e)

