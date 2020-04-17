class Student():

    @property # The getter
    def first_name(self):
        try:
            return self.__first_name # Note there are 2 underscores here
        except AttributeError:
            return 0

    @first_name.setter # The setter
    def first_name(self, new_first_name):
        if type(new_first_name) is str:
            self.__first_name = new_first_name
        else:
            raise TypeError('Please provide a string value for the first name')

    @property # The getter
    def last_name(self):
        try:
            return self.__last_name # Note there are 2 underscores here
        except AttributeError:
            return 0

    @last_name.setter # The setter
    def last_name(self, new_last_name):
        if type(new_last_name) is str:
            self.__last_name = new_last_name
        else:
            raise TypeError('Please provide a string value for the last name')

    @property # The getter
    def age(self):
        try:
            return self.__age # Note there are 2 underscores here
        except AttributeError:
            return 0

    @age.setter # The setter
    def age(self, new_age):
        if type(new_age) is int:
            self.__age = new_age
        else:
            raise TypeError('Please provide a integer value for the age')

    @property # The getter
    def cohort(self):
        try:
            return self.__cohort # Note there are 2 underscores here
        except AttributeError:
            return 0

    @cohort.setter # The setter
    def cohort(self, new_cohort):
        if type(new_cohort) is int:
            self.__cohort = new_cohort
        else:
            raise TypeError('Please provide a integer value for the cohort')
    
    @property
    def full_name(self):
        try:
            return f"{self.__first_name} {self.__last_name}"# Note there are 2 underscores here
        except AttributeError:
            return 0
    
    def __str__(self):
        return f"{self.full_name}"

mike = Student()
mike.first_name = "Mike"
mike.last_name = "Ellis"
mike.age = 35
mike.cohort_number = 39

print(mike)