class Person:
    """[Create persons]
    """

    def __init__(self, fname, lname):
        """[The constructor]

        Args:
            fname ([str]): [first name]
            lname ([str]): [last name]
        """
        self.fname = fname
        self.lname = lname
        self.age = 38

    def __repr__(self):
        """["When we enter our object in the interpreter"]

        Returns:
            [str]: [infos about instance]
        """
        return f"Person: firstname({self.fname}), lastname({self.lname}), age({self.age})"

    def __str__(self):
        return f"{self.fname} {self.lname} a {self.age} ans"


p1 = Person("Jason", "Micado")
print(p1)

p1_display = repr(p1)
print(p1_display)
