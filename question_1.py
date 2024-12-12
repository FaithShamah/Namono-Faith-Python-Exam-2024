# i)

import math

def circle_area(radius):     #I have used math.pi from import math and radius because the string 'r' can not be called and the sign '^' brings an error.
    area = math.pi * radius ** 2
    return area

radius = 4
result = circle_area(radius)
print(f"The radius of circle with radius {radius} is : {result}")

     
#iii)

value_one = int(input("Enter the first number: "))
value_two = int(input("Enter the second number: "))

sum = (value_one + value_two)
difference = (value_one - value_two)
product = (value_one * value_two)
quotient = (value_one / value_two)

print(f"The sum , difference , product , and quotient of {value_one} and {value_two} are :\n sum = {sum} , difference = {difference} , product = {product} and quotient = {quotient} respectively.")

#v)

student_info = {'name': 'Alice' , 'age' : 20 , 'grade' : 'A'}

student_info['age'] = 26
student_info['city'] = 'Kampala'

print(student_info)
