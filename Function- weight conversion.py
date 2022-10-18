def kgtotonne():
  '''
  This function helps the user to convert any quantity in kg to tonnes.
  '''
  x=float(input('Enter the unit in kg:'))
  y=x*0.001
  print('Units in tonnes:',y)

def tonnetokg():
  '''
  This function helps the user to convert any quantity in tonnes to kg.
  '''
  x=float(input('Enter the unit in tonnes:'))
  y=x/0.001
  print('Units in kg:',y)

def kgtopound():
  '''
  This function helps the user to convert any quantity in kg to pound.
  '''  
  x=float(input('Enter the unit in kg:'))
  y=x*2.20462
  print('Units in pounds:',y)

def poundtokg():
  '''
  This function helps the user to convert any quantity in pound to kg.
  '''
  x=float(input('Enter the unit in pounds:'))  
  y=x/2.20462
  print('Unit in kg:',y)

kgtotonne()
tonnetokg()
kgtopound()
poundtokg()
