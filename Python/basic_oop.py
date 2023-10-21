# Introduction Class and Object Python
class MyClass:
    print("Hello OOP Python")

# Class and Method
class ModelingPattern():
    def __init__(self) -> None:
        pass
    def testing_model():
        print("Test by User")


# Python Encapsulation
class MyComputer:
    def __init__(self):
        self._maxPrice = 100 # define value 
    
    def sale_department(self, price):
        self._maxPrice = price
        print("By Costumer: ", self._maxPrice)
    def report_department(self):
        print("Totale Product: {}".format(self._maxPrice))
        
# Polymorphism Python OOP
class MathematicModel:
    def __init__(self) -> None:
        pass
    
    def reading_model(slef):
        print("Key Version Model")

class CallBackPattern(MathematicModel):
    def reading_model(self):
        print("Department of Engineer")

class LinearProgramming(MathematicModel):
    def reading_model(self):
        print("Departmnet of ITE")


# Create Object and Call class
myObject = MyClass()
productDepartment = MyComputer()

class_method = ModelingPattern()
class_method.testing_model()

productDepartment.report_department()
productDepartment.sale_department(800.67)

eduPattern = MathematicModel()
callBack = CallBackPattern()
linearModel = LinearProgramming()

linearModel.reading_model()
callBack.reading_model()
eduPattern.reading_model()
