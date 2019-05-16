class Exc:
    """Define a class, which have a class parameter and have a same instance parameter."""
    name = 'Person'

    def __init__(self, name=None):
        self.name = name


e1 = Exc()
print(e1.name)
e2 = Exc('Bart')
print(e2.name)
