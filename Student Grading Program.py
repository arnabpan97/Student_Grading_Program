n=float(input("Enter The No Of The Subject : "))

if n<50:
    print("Grade : Fail")
elif n>=50 and n<60:
    print("Grade : D")
elif n>=60 and n<70:
    print("Grade : C")
elif n>=70 and n<80:
    print("Grade : B")
elif n>=80 and n<90:
    print("Grade : A")
elif n>=90 and n<=100:
    print("Grade : A+")
else:
    print("Invalid Marks")