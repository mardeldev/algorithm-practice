"""
Level of difficulty
Medium

Objectives
improving the student's skills in operating with special methods
Scenario
Create a class representing a time interval;
the class should implement its own method for addition, subtraction on time interval class objects;
the class should implement its own method for multiplication of time interval class objects by an integer-type value;
the __init__ method should be based on keywords to allow accurate and convenient object initialization, but limit it to hours, minutes, and seconds parameters;
the __str__ method should return an HH:MM:SS string, where HH represents hours, MM represents minutes and SS represents the seconds attributes of the time interval object;
check the argument type, and in case of a mismatch, raise a TypeError exception.
"""


class Time:
    def __init__(self, hrs, mins, secs):
        self.hours = hrs
        self.minutes = mins
        self.seconds = secs

    def __add__(self, others):
        match self.check_type(others):
            case 'Time':
                self.hours += others.hours
                self.minutes += others.minutes
                self.seconds += others.seconds
                return self.__str__()
            case 'int': 
                self.seconds += others
                return self.__str__()

    def __sub__(self, others):
        match self.check_type(others):
            case 'Time':
                self.hours -= others.hours
                self.minutes -= others.minutes
                self.seconds -= others.seconds
                return self.__str__()
            case 'int':
                self.seconds -= others
                return self.__str__()

    def __str__(self):
        return '{0:02}:{1:02}:{2:02}'.format(self.hours, self.minutes, self.seconds)

    def check_type(self, others):
        if isinstance(others, Time):
            return 'Time'
        elif isinstance(others, int):
            return 'int'
        else:
            raise TypeError('Mismatch in object type')


t1 = Time(2, 5, 30)
t2 = Time(1, 1, 1)
print(t1 + t2)
print(t1 + 10)
