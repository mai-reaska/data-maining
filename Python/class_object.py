# Create class and Object

class MyClass:
    stu_id = 0

# Python Constructors 
class CalculationNumber():
    total = 0
    def __init__(self, value, suming, adding):
        self.value = value
        self._suming = suming
        self.__adding__ = adding
        CalculationNumber.total = suming + value

    def calculate_model(self):
        print("Thank!")

    def call_back(self):
        print(self.value)

    def adding_value(aelf, *args):
        print(f'Calculation of Value:  {CalculationNumber.total}')

# Call call and Object
myObj = MyClass()
myObj.stu_id = 999.1
print(f'{myObj.stu_id}')

claculator = CalculationNumber(13.12, 2, 3)
claculator.call_back()
claculator.adding_value()