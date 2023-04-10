import math


def test():
    k1,m,k2,p2,n2=map(int,input().split())
    goodL=[]
    for L in range(1,100000):
        if (p2==(k2-1)//(L*m)+1 and n2==(k2-(p2-1)*L*m-1)//L+1):
            goodL.append(L)
    goodN=set()
    goodP=set()
    for l1 in goodL:
        p1=(k1-1)//(l1*m)+1;
        goodP.add(p1)
        goodN.add((k1-(p1-1)*l1*m-1)//l1+1)
    res=""
    if len(goodP)==1:
        p1=goodP.pop()
    elif len(goodP)>1:
        p1="0"
    else:
        p1="-1"
    if len(goodN)==1:
        n1=goodN.pop()
    elif len(goodN)>1:
        n1="0"
    else:
        n1="-1"
    res=f"{p1} {n1}"
    print(res)

    # minL = math.floor(k2 / ((p2 - 1) * m + n2))
    # if (((p2-1)*m+n2-1)==0):
    #     print ("ХЗ")
    # else:
    #     maxL=math.floor(k2/((p2-1)*m+n2-1))
    #
    #     if (maxL-minL)==1:
    #         L=maxL
    #         p1=1+(k1-1)//(L*m)
    #         n1=(k1-(p1-1)*L*m)//L+1
    #         print (p1,n1)
