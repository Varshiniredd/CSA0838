#program for grade and average marks
S1=english=int(input("enter the marks"))
S2=maths=int(input("enter the marks"))
S3=social=int(input("enter the marks"))
S4=chemisty=int(input("enter the marks"))
S5=physics=int(input("enter the marks"))
t=S1+S2+S3+S4+S5
print("total=",t)
if(t>=500):
    print("S grade")
    if(t>=450 and t<500):
        print("A grade")
        if(t>=400 and t<450):
            print("B grade")
            if(t>=350 and t<400):
                print("C grade")
                if(t>=350 and t<400):
                     print("D grade")
                     if(t<300):
                         print("fail")
average=t/5
print("average=",average)

                         
                     

