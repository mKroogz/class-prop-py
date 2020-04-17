class Patient():

    def __init__(self, ssn, dob, acct_num, first_name, last_name, address):
        self.__ssn = ssn
        self.__dob = dob
        self.__acct_num = acct_num
        self.__first_name = first_name
        self.__last_name = last_name
        self.__address = address

    @property # The getter
    def ssn(self):
        try:
            return self.__ssn # Note there are 2 underscores here
        except AttributeError:
            return 0

    @property # The getter
    def dob(self):
        try:
            return self.__dob # Note there are 2 underscores here
        except AttributeError:
            return 0
            
    @property # The getter
    def acct_num(self):
        try:
            return self.__acct_num # Note there are 2 underscores here
        except AttributeError:
            return 0

    @property # The getter
    def address(self):
        try:
            return self.__address # Note there are 2 underscores here
        except AttributeError:
            return 0

    @address.setter # The setter
    def address(self, new_address):
        if type(new_address) is str:
            self.__address = new_address
        else:
            raise TypeError('Please provide a string value for the address')
    
    @property
    def full_name(self):
        try:
            return f"{self.__first_name} {self.__last_name}"# Note there are 2 underscores here
        except AttributeError:
            return 0


cashew = Patient(
    "097-23-1003", "08/13/92", "7001294103",
    "Daniela", "Agnoletti", "500 Infinity Way"
)

# This should not change the state of the object
# cashew.ssn = "838-31-2256"

# Neither should this
# cashew.dob = "01-30-90"

# But printing either of them should work
print(cashew.ssn)   # "097-23-1003"

# These two statements should output nothing
# print(cashew.first_name)
# print(cashew.last_name)

# But this should output the full name
print(cashew.full_name)   # "Daniela Agnoletti"