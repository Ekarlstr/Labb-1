print("Enter a number and find if there is a combination of 2 numbers cubed that add up to your number!")
def kubsumma(n):
    a=0
    b=0
    list = []
    for b in range(0,int(n**(1/3))+1):
        for a in range(0,int(n**(1/3))+1):
            if n== a**3 + b**3 and a>=b:
                list.append((a,b))
    return list
while True:
    n=int(input("Your number: "))
    print(kubsumma(n))
