
a = [1,44,2,4,1,2,3,6,13,4]


for i in range(len(a)):
    for j in range(0,len(a)-i-1):
        if a[j] > a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]


print(a)