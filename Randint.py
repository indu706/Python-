#Generate random no.s from the range
import random
l=int(input('Enter the lower limit'))
u=int(input('Enter the upper limit'))
for i in range(1,6):
  print(random.randint(l,u))
