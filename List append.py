def func(l):
 
 print(l)
 n=len(l)
 if n%2==0:
  hlf=n//2
 else:
  hlf=(n-1)//2
 a=l[0:hlf]
 print(l+a) 
l=[]
i=1
n1=int(input('Enter the no. of elements you want to enter'))
while i<=n1:
  add=int(input('Enter the element'))
  l.append(add) 
  i+=1
func(l)
