def test ():
    a,b,c=int(input()),int(input()),int(input())
    a,b,c=min(a,b,c),a+b+c-min(a,b,c)-max(a,b,c),max(a,b,c)
    if (a+b>c and a+c>b and b+c>a):
        print ("YES")
    else:
        print("NO")
