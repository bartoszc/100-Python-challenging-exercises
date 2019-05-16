class Person:
    gender = None
    """Define a class Person and its two child classes: Male and Female. All classes have a method "getGender" which can 
    print "Male" for Male class and "Female" for Female class."""
    def get_gender(self):
        print(self.gender)


class Male(Person):
    gender = 'Male'


class Female(Person):
    gender = 'Female'


m1 = Male()
m1.get_gender()
fe1 = Female()
fe1.get_gender()