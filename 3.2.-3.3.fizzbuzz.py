file = open ('/Users/apple/Documents/fizzbuzz.txt' , 'r')
a = file.readline()
f1 = a[0]
b1 = a[2]
c1 = a[4]+a[5]
f=int(f1)
b=int(b1)
c=int(c1)
file2 = open('/Users/apple/Desktop/fizzbuzz2.txt', 'w')
for x in range(1, c+1):
    if x % f == 0 and x % b == 0:
        file2.write("FB")
    elif x % f == 0:
        file2.write("F")
    elif x % b == 0:
        file2.write("B")
    else:
        file2.write(str (x))
file.close()
file2.close()
