class American:
    """Define a class named American which has a static method called printNationality."""
    nationality = 'American'

    @staticmethod
    def print_nationality():
        print('Your nationality is', American.nationality)


print(American.nationality)
a1 = American()
a1.print_nationality()
