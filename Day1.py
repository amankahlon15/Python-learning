



name=input ("enter your name:")
age= int(input("enter your age:"))
city=input("enter your city:")
height= float(input("enter your height in feet:"))
is_student= input("are you a student? (yes/no)")

# convert student to true or false
is_student= is_student.lower() =="yes"

#calculations
height_in_inches= round(height*12)
age_next_year= age+1

#display the information
print("name:", name)
print("age:",age)
print("city:",city)
print("height:", height , "feet")
print("your height in inches is:", height_in_inches)
print("student:", is_student)
print("age next year:", age_next_year)

    
