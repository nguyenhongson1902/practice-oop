class Person: 
    number_of_people = 0 # A class attribute, not different from each instance of the class
    GRAVITY = 9.8


    def __init__(self, name):
        self.name = name
        # Person.number_of_people += 1 # keep track of how many instances initialized
        Person.add_person()


    @classmethod
    def number_of_people_(cls):
        return cls.number_of_people

    @classmethod
    def add_person(cls):
        cls.number_of_people += 1



p1 = Person('Son')
p2 = Person('Tim')
print(Person.number_of_people_())
