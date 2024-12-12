# i)

#A python snippet

age = int(input("Please enter your age: "))

if age >= 18:
    print("You are eligible")

else:
    print("You are not eligible")


# ii)

def grade_students(mark):
    if mark >=90:
        return 'A'
    elif mark >=80:
        return 'B'
    elif mark >=70:
        return 'C'
    elif mark >=60:
        return 'D'
    else:
        return 'F'
    
# iii)
 
mark = 85
grade = grade_students(mark)
print(f"The grade for {mark} is: {grade}")

# iv)

#handle input mark that is not valid (not a number)

def grade_students(mark):
    try:
        mark = float(mark)
        if mark < 0 or mark > 100:
            return 'Invalid Input'
        if mark >=90:
            return 'A'
        elif mark >=80:
            return 'B'
        elif mark >=70:
            return 'C'
        elif mark >=60:
            return 'D'
        else:
            return 'F'
    except ValueError:
        return 'InvalidInput'
    
#Test the function with a valid mark and invalid input

valid_mark = 85
grade = grade_students(valid_mark)
print(f"The grade for valid mark {valid_mark} is: {grade} ")

invalid_input = 'abc'
grade = grade_students(invalid_input)
print(f"The grade for invalid_input 'abc' is : {grade} ")


# v)

#Enhancing the grade_students function to also provide a message along with grade

def grade_students(mark):
    try:
        mark = float(mark)
        if mark < 0 or mark > 100:
            return 'Invalid Input'
        if mark >=90:
            return 'A', 'Excellent'
        elif mark >=80:
            return 'B', 'Excellent'
        elif mark >=70:
            return 'C', 'Good'
        elif mark >=60:
            return 'D', 'Satisfactory'
        else:
            return 'F', 'Needs Improvement'
    except ValueError:
        return 'InvalidInput'
    
# vi)

#Testing the function with a mark of 78
    
mark = 78
grade, message = grade_students(mark)
print(f"The grade for {mark} is: {grade} : message = {message}")
