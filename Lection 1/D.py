#   (ax+b)**0,5=c
#   ax+b=c**2
#   x=(c**2-b)/a
#   c>=0!
#   ax+b>=0!
import math



a,b,c=int(input()),int(input()),int(input())
if c<0:
    print("NO SOLUTION")
elif a==0:
    if c**2==b:
        print ("MANY SOLUTIONS")
    else:
        print("NO SOLUTION")
else:
    x=(c**2-b)/a
    if x.is_integer():
        print(int(x))
    else:
        print ("NO SOLUTION")
