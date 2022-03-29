import math 
print("Welcome to my fraction reducer!")
print("*******************************")

while 1 == 1:
  a = int(input("Enter the numerator: "))
  b = int(input("Enter the denominator: "))

  if b == 0: #checking for 0 in the denominator
    print("The fraction is undefined")

  elif a == 0: #checking for 0 in the numerator
    print("Here is your reduced fraction:")
    print(str(a)+"/"+str(b),"=","0")

  else: 
    #finding the GCD using Euclid's formula
    MAX = min(a,b)
    MIN = max(a,b)
    remainder = MAX % MIN

    while remainder > 0:   
      MAX = MIN
      MIN = remainder
      remainder = MAX % MIN

    gcd = MIN

    #dividing the numerator and denominator by the GCD to find the reduced fraction
    aReduced = int(a/gcd)
    bReduced = int(b/gcd)

    #removing the denominator of the fraction if the denominator is equal to 1
    if bReduced == 1:
      print("Here is your reduced fraction:")
      print(str(a)+"/"+str(b),"=",aReduced)
    
    #checking for fractions that are already in reduced form
    elif gcd == 1:
      print("The fraction", str(a)+"/"+str(b) ,"is already in reduced form")

    #if nothing applies, the fraction reduces normally
    else: 
      print("Here is your reduced fraction:")
      print (str(a)+"/"+str(b),"=",str(aReduced) + "/" + str(bReduced)) 