c=0
p=0
l=input("Enter a line:")
n=len(l)
print("No. of characters=",n)
s=l.split()
w=len(s)
print("No. of words=",w)
for j in l:
  if j.isalnum():
      p+=1
print('No. of Alphanumeric characters=',p)      
print('% of Alphanumeric characters=',(p/n)*100) 
