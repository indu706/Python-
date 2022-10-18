d={60:'Elephants',4:'Eggs',113:'Red',33:'Peacock'}
l=list(d.keys())
n=len(l)
for i in range(n-1):
  for j in range(n-i-1):
    if l[j]>l[j+1]:
      l[j],l[j+1]=l[j+1],l[j]
print('Sorted list of keys--',l)  
