class InheritanceClass(Exception):
    """Define a custom exception class which takes a string message as attribute."""
    def __init__(self, msg):
        self.msg = msg


error = InheritanceClass('Something Wrong')
