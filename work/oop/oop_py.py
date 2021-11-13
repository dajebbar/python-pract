import datetime

class Student:
    def __init__(self, name, age, courses):
        self.__name = name
        self.__age = age
        self.__courses = courses

    # getters of Student class
    def get_age(self):
        return self.__age

    def get_name(self):
        return self.__name

    def get_courses(self):
        return self.__courses

    # setters of Student class
    def set_age(self, new_age):
        self.__age = new_age

    def set_name(self, new_name):
        print("name of student can't be changed")

    def set_courses(self, new_course, index=None):

        if isinstance(index, int) and index < len(self.__courses):
            self.__courses[index] = new_course

        if new_course not in self.__courses:
            self.__courses.append(new_course)
    
    # __str__ method
    def __str__(self):
        return f"{self.get_name()} - {self.get_age()} - {self.get_courses()}"
    
    # derived constructor
    @classmethod
    def student_results(cls, name, birthday, **results):
        age = datetime.datetime.now().year - birthday
        return cls(name, age, results)


std_1 = Student("Alpha", 21, ["cs50", "philo"])
# print(std_1.get_courses())
# std_1.set_courses("Maths")
# std_1.set_courses("DL", 3)
# print(std_1.get_courses())
std_2 = Student.student_results("Beta", 1998, cs50=17, agro=15.5)
print(std_2)
