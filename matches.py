
def matches(str1,str2):
a=(input("str1 ="))
b=(input("str2 ="))
c=min(len(a),len(b))
d=0
for i in range(c):
    if (a[i]==b[i]):
        d+=1
print(d)
