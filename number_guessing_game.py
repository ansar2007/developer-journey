n= 45
tries = 0
while True:
    d = int (input("Guess the number: "))
    tries+= 1
    if d>n:
        print ("Too high!")
    elif d<n:
        print ("Too low!")
    else:
        print ("Correct! You won!")
        break
print ("Guessed in ",tries,"tries")