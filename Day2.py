name=input("enter your name:")
age= int(input("enter your age:"))
is_student= input("are you a student? (yes/no)")

is_student = is_student.lower() == "yes"

print("name:",name)
print("age:",age)
print("student", is_student)

if age >= 18 and is_student:
    print("eligible")
else:
    print("not eligible")