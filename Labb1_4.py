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
        if a > n**(1/3):
            a=b
            b=b+1
        if b**3 > n and count==2:
            print("Kubsumma: ",list)
            break
        if count < 2 and b**3 > n +2 :
            print("lacks solutions!")
            break
while True:
    n=int(input("write a number: "))
    kubsumma(n)
