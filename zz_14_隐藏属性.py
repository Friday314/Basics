class Dog:

    def set_Age(self, new_age):

        if new_age > 0 and new_age <= 100:
            self.age = new_age
        else:
            self.age = 0

    def get_Age(self):
        return self.age


dog = Dog()

dog.set_Age(-10)

age = dog.get_Age()

print(age)
