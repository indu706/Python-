#Checking whether no. is perfect no. or not
def func(n):
  l=[]
  total=0
  print('Divisors of',n,':')
  for i in range(1,n):
    if n%i==0:
      print(i)
      l.append(i)
  for x in l:
    total+=x
  print('Total sum of divisors:',total) 
  if total==n:
    print('Yes,number is a perfect no.')
  else:
    print('No, the number is not perfect') 
n=int(input('Enter a positive no.'))  
func(n)     
