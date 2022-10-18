#Rotating the elements of list
l=[]
n=int(input('Enter the no. of elements'))
i=1
while i<=n :
  a=input('Enter the element')
  l.append(a)
  i+=1
print(l)
n=len(l)
b=l.pop()
listnew=list(b) 
print(listnew+l)
