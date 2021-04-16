#insertion sort
size = int(input('enter the size of the list:'))
a = []
for i in range(size):
    val=int(input('enter number:'))
    a.append(val)
for i in range(1,size):
    t=a[i]
    j=i-1
    while j>=0 and t>a[j]:
        a[j+1]=a[j]
        j=j-1
    a[j+1]=t
print('the sorted list is:', a)
