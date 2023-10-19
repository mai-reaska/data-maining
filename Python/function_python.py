# Simple function using Pass keyworld
def hello_worl():
    pass

# Function don't have Parameter
def fun_noParam():
    print("Hello Function No Paramter")

# Function Have Paramter Number
def fun_haveParam(a, b):
    c = a + b
    print(c)

# Function Have Paramter Number
def fun_strParam(f_name, l_name):
    my_name = f_name + l_name
    print("My name is ", my_name)

# Function Pass param by *arge
def fun_argeParam(*name):
    print("Pass by ", name)

# Fuction Pass by **kwargs
def fun_kwargsParam(**data):
    print(data)

# Function Use Variabel 
def fun_variabel(x, y):
    return x + y

# Lambda Function
lamda_fun = lambda: print("Lambda Fuction")

# Lambda have Paramater
fun_lamParam = lambda a, b : a + b

# Lambda return
def fun_lamda(*param):
    return lambda x : x + param

# Call function have param pass value
fun_haveParam(10, 20)
fun_strParam('mai','reaksa')
fun_argeParam('reaksa','lika','sokhim','daly')
fun_kwargsParam(f_name="reaksa", l_name="mai", age=21, email="reaksamai@rupp.edu.kh")

# Call fun by Varibel
call_fun = fun_variabel(1, 3)
print(call_fun)

# Call LambdaFuction
lamda_fun()
print(fun_lamParam(12, 34))
pass_agrdLamda = fun_lamda(1)