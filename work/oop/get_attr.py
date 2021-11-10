class Protect:
    """[Class having a particular method of accessing its attributes]

    Returns:
        [type]: [description]
    """
    all_instance = []

    def __init__(self, school, age):
        self.school = school
        self.age = age
        self.city = "Casablanca"
        Protect.all_instance.extend([self.school, self.age, self.city])

    def __getattr__(self, name):
        if name not in Protect.all_instance:
            print(f"{name} doesn't exist! you will redirect to school")
            name = self.school
        return name

    def __setattr__(self, name, value):
        """[Method called when object is made. name attr = val attr. 
        We take care of registering the object]"""
        object.__setattr__(self, name, value)
        # self.register()

    def __delattr__(self, name):
        """[We cannot delete an attribute, we throw the exception AttributeError]"""

        raise AttributeError("You cannot remove any attribute from this class")


pro = Protect("EUC", 18)


pro.__delattr__(pro.age)
