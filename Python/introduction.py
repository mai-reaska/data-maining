# Basic print in Python
print('Hello')

# Varaible in Pthon 
varlInt = 12
valString = "Hello World"
valFloat = 34.11
print(valString)
print(varlInt)
print(valFloat)

# Conditional in Python
i = 10
if i==10:
    print(i)

if i>=0:
    print(i)
else:
    print('No Print')

if i!=1 & i<10:
    s = i =+ 2
    print(s)
elif i == 0 | i == 1:
    pass
else:
    print('Thank!') 

#cuasting string in python
a = 12
st = "Good Morning Sunday!"
string_val = '1'
con_val = int(string_val)
f = float(a)
cal = con_val + 1000
print(cal)
print(type(con_val))

# Assignt two 
a,b = (12, 13)
st1, st2 = ("Hello_1", "Hello_2")
print(a,b)
print(st1, st2)

# String Varaible
string_num1 = "Hello"
string_num2 = "Wolrd"
string_number1 = '1'
string_number2 = '2'

cas_str1 = int(string_number1)
cas_str2 = int(string_number2)

# string adding with integer can not!
# -> ading_str_int = string_num1 + cas_str1 # Don't work 

casting_string = string_number1 + string_number2 # This adding by string  
add_string_number = cas_str1 + cas_str2 # adding by casting to integer
adding_str = string_num1 + ' '+ string_num2

print(adding_str)
print(casting_string, type(string_number1), type(string_number2))
print(add_string_number, type(cas_str1), type(cas_str2))

#Array in python 
# >> List
list_number = [1, 2, 3, 4, 5, 'OK'] # list number
list_string = ['1', '2', '3', '4', '5'] # list of string 

cas = int(list_string[1]) # casting list of string to integer base index
print(type(cas))
print(list_number) # Print all 
print(list_number[1]) # Print base index of array

# null list using assign value too
null_list = []
null_list.append("Hello")
print(null_list)

# Slicing of a List
print(list_number) # print all index
print(list_number[1:4]) # print start index 1 to index 4
print(list_number[1:]) # print indext start form 1 too

# counting list
print(list_number.count(5))

# Loop in Python 
# >> For loop

