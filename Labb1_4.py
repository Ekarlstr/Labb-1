print("Enter a number and find if there are two combinations of 2 numbers cubed that add up to your number!")
def kubsumma(n):
    a=0
    b=0
    count=0
    list = []
    while True:
        if n== a**3 + b**3 and a>=b:
            list.append((a,b))
            count=count+1
        a=a+1
        if a**3 > n:
            a=b
            b=b+1
        if count==2:
            print("Kubsumma: ",list)
            break
        if count==1 and b**3 > n+2 :
            print("No, but ", list, "is one!")
            break
        if count < 1 and b**3 > n +2 :
            print("lacks solutions!")
            break
while True:
    n=int(input("Your number: "))
    kubsumma(n)
