def getPrimes(num):
    for element in range(num):
        if num%element == 0:
            print "False"


print getPrimes(10)