class Duration:
    """["Class containing durations in the form of a number of minutes and seconds]
    """

    def __init__(self, min=0, sec=0):
        self.min = min
        self.sec = sec

    def __str__(self):
        return f"{self.min:02}:{self.sec:02}"

    def __add__(self, x):
        # if x < 60:
        #     self.sec += x
        # else:
        #     min = x // 60
        #     sec = x / 60 - min
        #     sec = str(sec)
        #     sec = int(sec[sec.index('.') + 1:4])
        #     self.min += min
        #     self.sec += sec
        new_duration = Duration()
        new_duration.sec = self.sec
        new_duration.min = self.min

        new_duration.sec += x

        if new_duration.sec >= 60:
            new_duration.min += new_duration.sec // 60
            new_duration.sec %= 60

        return new_duration

    def __radd__(self, x):
        return self + x

    def __iadd__(self, x):
        """[d += x incrementation of time]"""
        self.sec += x
        if self.sec >= 60:
            self.min += self.sec // 60
            self.sec %= 60

        return self


d1 = Duration(12, 8)
print("display time __str__:")
print(d1)
print("test d object + time (__add_):")
d2 = d1 + 54
print(d2)
print("test right __radd__:")
d3 = 4 + d2
print(d3)

print("test incrementation __iadd__:")

d1 += 54
print(d1)
