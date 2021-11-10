class Person:

    def __init__(self, **kwargs):
        self.person_info = {k: v for k, v in kwargs.items()}

    def display_info(self):
        for k, v in self.person_info.items():
            print(f"{k} -> {v}")

    def __del__(self):
        print(f"object was deleted")

    def __repr__(self):
        return str(self.person_info)

    def __str__(self):
        res = ""
        for k, v in self.person_info.items():
            res += str(k) + ": " + str(v) + ",\n"
        return res

    def __getitem__(self, index):
        return self.person_info[index]

    def __setitem__(self, index, value):
        self.person_info[index] = value

    def __contains__(self, item):
        if item in self.person_info:
            return True
        return False

    def __len__(self):
        return len(self.person_info)


info = {
    "fname": "Jason",
    "lname": "Micado",
    "age": 54,
    "planet": "Mars",
}


p1 = Person(**info)
# p1.display_info()
# print(p1.person_info["fname"])
# p1.person_info["planet"] = "Jupyter"

# print(dir(p1))
# print(p1.__dict__)

# print(repr(p1))

print(p1["planet"])
p1["planet"] = "Earth"
print(p1["planet"])
print("planet" in p1)

p1["city"] = "Marseille"
print(p1)
print(p1["city"].__len__())
