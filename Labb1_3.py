print("Name a number and find two numbers that cubed add up to your number")
print("The program will find all the solutions")
while True:
    a=int(input("Enter your number: "))
    Count=0
    b=0
    c=0
    while True:
        if a==(b**3 + c**3):
            print("Answer: ", b, "and", c)
            Count=Count+1
        if a==1:
            print("Answer: ","1 and 0")
            break
        b=b+1
        if b==a and b>=c:
            c=c+1
            b=c
        if c==a:
            if Count==0:
                print("No integer fullfills conditions")
            break
