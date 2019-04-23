# There can be three types of methods in classes in Python

# 1 - class method  -- we can use class methods as alternative constructor
# 2 - static method -- are used for methods which don't have direct connection to the class
# 3 - regular method -- they are just normal methods


class Student:

    # initializing the class
    def __init__(self, name, roll, branch):
        self.name = name
        self.roll = roll
        self.branch = branch

    # Function to return the details of the Student
    def get_details(self):
        print("The Details of the Student is :")
        print(f'Name : {self.name}')
        print(f'RollNo : {self.roll}')
        print(f'Branch : {self.branch}')

    # This method is used as an alternative constructor to accept raw string as its input and return a {Student} class object
    @classmethod
    def extract_info(cls, raw_string):
        name, roll, branch = raw_string.split('+')
        return cls(name, roll, branch)

    # This method doesn't contains any diret relation or use of any class variables
    @staticmethod
    def is_of_college(college):
        if college == 'PSIT':
            print(True)
        else:
            print(False)


# This function provides documentation on any object that we need help for
# print(help(map))


# Creating an instance of the Student Class and passing the parameters and using methods of the Student class.

# s1 = Student('shiv kumar katheriya', 1716410223, 'CSE')
# s1.get_details()
# s2 = Student('harsh Chaurasia', 1716410223, 'CSE')
# s2.get_details()
# s3 = Student('Prakhar kumar', 1716410223, 'CSE')
# s3.get_details()
# s1.is_of_college("PSIT")


# Creating an instance of the Student class via {extract_info}-classmethod.

s2 = Student.extract_info("Harsh Chaurasia+1716410101+CSE")
s2.get_details()
# s2.is_of_college("KIT")


# This function can be used to know if an object is an instance of a class or not
# print(isinstance(s1, Student))