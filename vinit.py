size = int(input('enter size of the list:'))
a = []
for i in range(size):
    val = int(input('enter number:'))
    a.append(val)
for i in range(size):
    for j in range(size-i-1):
        if a[j]> a[j+1]:
            t=a[j]
            a[j]=a[j+1]
            a[j+1]= t
print('the sorted list is:', a)