class Math:


    @staticmethod # not changing, staying the same
    def add5(x):
        return x + 5

    @staticmethod # not changing, staying the same
    def add10(x):
        return x + 10

    @staticmethod
    def pr():
        print('Run')


# m = Math() # That's not necessary

print(Math.add5(5))
print(Math.add5(10))
Math.pr()