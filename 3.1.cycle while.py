a = [1, 2, 3, 4, 5]
s = 0
counter = 0
lenth=a[len(a)-1]
while  counter < a[lenth-1]:
     s+=a[counter]
     counter+=1
print (s)