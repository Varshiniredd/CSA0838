l1=[1,2,3,4,5,6,7,8]
even_sq,odd_sq=[],[]
for i in l1:
    (even_sq if 1%2==0 else odd_sq).append(i*i)
print(even_sq,odd_sq)
