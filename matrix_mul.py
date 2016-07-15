# 2X2 matrix multiplication

a=[]
print("Enter 4 numbers for Matrix A")
for i in range(4):
    a.append(int(input("Enter value ")))
print ("%d %d\n%d %d"%(a[0],a[1],a[2],a[3]))

b=[]
print("Enter 4 numbers for Matrix B")
for i in range(4):
    b.append(int(input("Enter value " )))
print ("%d %d\n%d %d"%(b[0],b[1],b[2],b[3]))


c=[]
c.append(a[0]*b[0]+a[1]*b[2])
c.append(a[0]*b[1]+a[1]*b[3])
c.append(a[2]*b[0]+a[3]*b[2])
c.append(a[2]*b[0]+a[3]*b[3])
print("The resltant Matrix C is")
print ("%d %d\n%d %d"%(c[0],c[1],c[2],c[3]))
