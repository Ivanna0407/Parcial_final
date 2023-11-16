import random 
n=random.randint(1,10)
p=3
estado=True
for i in range(3):
  cnt=i+1
  print("Tienes",p,"Intentos para poder adivinar un número del 1 al 10")
  r=int(input("Dime un número "))
  if r ==n:
    print("Adivinaste lo lograste en",cnt,"intentos")
    break
  else:
    print("No adivinaste")
    p=p-1
    estado=False
    
if estado==False:
  print("No lograste adivinar en 3 intentos el número era el",n)
