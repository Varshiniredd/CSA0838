def charr(s,r):
    sp=""
    for i in (s):
        if(i==r):
           continue
        else :
           sp=sp+i
    print(  "OUTPUT : ",sp)
str=str(input("sentence: "))
r=input(" character to be removed :")
charr(str,r)
