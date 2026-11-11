n = int (input ("Enter a number: "))
x=1
if n < 0:
    print ("Factorial undefined")
else:
    while n>=1:
        x*= n
        n-=1
    print ("factorial = ",x)
