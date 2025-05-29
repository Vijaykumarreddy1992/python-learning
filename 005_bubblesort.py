#bubblesort program in python
a=[34,40,20,18,12]
for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        if a[i]>a[j]:
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
            print(i)