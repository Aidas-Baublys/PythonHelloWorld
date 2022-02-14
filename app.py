class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print("Blah, blah")


person = Person("Lopchikas")
person.talk()
print(person.name)
