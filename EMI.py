#Calculating EMI
p=int(input('Enter the principle amount'))
roi=float(input('Enter the rate of interest'))
n=int(input('Enter the no. of years'))
emi=(p*roi*(1+roi)**n)/((1+roi)**n-1)
print('Your EMI is',emi)
