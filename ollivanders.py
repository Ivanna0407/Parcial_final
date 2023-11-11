sauco=0
espino=0
sauce=0
acebo=0
clientes_t=0
clientes_com=0
estado=True
while estado==True:
  c=input("¿Entra un cliente? si/no")
  if c=="si":
    clientes_t+=1
    compra=input("¿Compró algo? si/no")
    if compra=="si":
      clientes_com+=1
      varita=int(input("¿Qué varita compró? 1. Varita de Saúco, 2. Varita de Espino, 3. Varita de Sauce y 4. Varita de Acebo."))
      if(varita==1):
        sauco+=1
      elif(varita==2):
        espino+=1
      elif(varita==3):
        sauce+=1
      elif(varita==4):
        acebo+=1
    else:
      estado=True
  elif c=="no":
    estado=False

print("Clientes que entraron:",clientes_t)
print("Clientes que compraron",clientes_com)
print("Clientes que no compraron",clientes_t-clientes_com)
print("Varitas de sauco vendidas",sauco)
print("Varitas de espino vendidas",espino)
print("Varitas de sauce vendidas",sauce)
print("Varitas de acebo vendidas",acebo)
