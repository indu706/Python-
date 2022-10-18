#Generate armstrong no. upto n
n=int(input('Enter the range'))
for i in range(1,n+1):
  n1=i
  sum=0
  while n1>0:
    d=n1%10
    n1=n1//10
    sum=d**3+sum
  if sum==i:
    print(i)
