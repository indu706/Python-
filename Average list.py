#Finding average of list of no.s
def func(l):
  total=0
  n=len(l)
  if n==0:
    print('The list is empty!')
  for i in l:
    a=int(i)
    total+=a 
  print('Total=',total) 
  print('Average=',total/n) 

l=[]
i=1
ne=int(input('Enter the No. of elements '))
while i<=ne:
  add=input('Enter the element:')
  if add.isalpha():
    print('Wrong input!')
  else:
    l.append(add)
    i+=1
func(l)  
