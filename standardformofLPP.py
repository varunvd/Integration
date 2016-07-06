"""
 The objective function and all other  constraints
 must be specified in all degree of variable unitl
 the highest one if it has no particular  variable
 then 0 must be specified as it's coefficient.
 Example z-3x1-4x2-0x3
	 1x1-1x2-0x3<=45
	 1x1+33x2+4x3<=6
"""
obj=raw_input("Enter the objective function\n")
n=int(raw_input("Enter the number of constraints\n"))
#The below process is carried out to create a virtual table like representation
list=[]
for i in range(0,n):
	list.append(raw_input())
d = { x:y for x,y in zip(range(0,n), list) }
m=int(obj[-1])
for i in range(1,m+1):
	obj=obj.replace('x'+str(i) , '')
b=''
for i in range(0, len(d)):
	b='s'+str(i)
	(b1,b2)=d[i].split("<=")
	m=int(b1[-1])
	for j in range(1,m+1):
		b1=b1.replace("x"+str(j), '')
	if b1[0] != '-':
		b1="+"+b1
	if b2[0] != '-':
		b2="+"+b2
	b=b+b1+b2
	d[i]=b
	b=''
obj=obj+(n+1)*"+0"
obj=obj.replace('z', 'z0')
b=''
for i in range(0, len(d)):
	b=(i)*'0'+'1'+(n-1-i)*'0'
	k=''
	for j in range(0, len(b)):
		k=k+'+'+b[j]
	c=''
	count=-1
	while(d[i][count]!='+' and d[i][count]!='-'):
		c=d[i][count]+c
		count=count-1
	c=d[i][count]+c
	count=-(count)
	d[i]=d[i].__getslice__(0,len(d[i])-count)
	d[i]=d[i]+k+c
c=''
v=[] #Contains the objective function
for i in range(0, len(obj)):
	if obj[i]=='+' or obj[i]=='-':
		v.append(c)
		c=obj[i]
	else:
		c=c+obj[i]
v.append(c)
for j in range(0,len(d)):
	c=''
	x=[]
	for i in range(0, len(d[j])):
		if d[j][i]=='+' or d[j][i]=='-':
			x.append(c)
			c=d[j][i]
		else:
			c=c+d[j][i]
	x.append(c)
	d[j]=x
print v
print d
