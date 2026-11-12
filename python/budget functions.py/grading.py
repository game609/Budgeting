name= input("Enter your name:")
grade = input("Enter your class:")
A = int(input("Enter your maths marks:"))
B = int(input("Enter your physics marks:"))
C = int(input("Enter your chemistry marks:"))
D = int(input("Enter your bioloogy marks:"))
E = int(input("Enter your geography marks:"))
F = int(input("Enter your computer science marks:"))
G = int(input("Enter your Kiswahili marks:"))
H = int(input("Eter your English marks:"))
I = int(input("Enter your Historia marks:"))
J = int(input("Enter your Business marks:"))
sum = A+B+C+D+E+F+G+H+I+J
avg = sum/6
print(f"Total:{sum}")
print(f"Average:{avg}")
if avg>=80:
    print("Grade: A")
elif avg>=70:
    print("Grade: B")
elif avg>=60:   
    print("Grade: c")
elif avg>=50:
    print("Grade: D")
else:
    print("Grade:F")            