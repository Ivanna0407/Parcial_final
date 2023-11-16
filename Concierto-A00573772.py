estado=True
c_zona=0
desc=0
cnt=0
acc=0
while estado==True:
  r=input("Hay un cliente en la fila ")
  if r=="si" or r=="Si":
    cnt+=1
    nombre=input("Dime el nombre del cleinte")
    dia=input("Dime el día de la semana")
    zona=int(input("A que zona va el cliente, 1/2/3"))
    if zona==1:
      c_zona=2000
    elif zona==2:
      c_zona=1000
    elif zona==3:
      c_zona=700
    cupon_r=input("Tiene un cupón")
    if cupon_r=="Si" or cupon_r=="si":
      cupon=input("¿Qué tipo de cupón? Platino/Oro/Plata")
      if cupon=="platino" or cupon=="Platino":
        desc=500
      elif cupon=="oro" or cupon=="Oro":
        desc=300
      elif cupon=="plata" or cupon=="Plata":
        desc=200
    if dia=="Lunes" or dia=="lunes" or dia=="Martes" or dia=="martes" or dia=="Miercoles" or dia=="miercoles" or dia=="Jueves" or dia=="jueves":
      costo=c_zona-desc
    else:
      costo=c_zona
    acc+=costo
    print("El costo total del boleto de",nombre,"es de",costo)
  elif r=="no" or r=="No":
    print("No hay un cliente")
    estado=False
  else:
    print("No es valido")
print("Se vendieron un total de",cnt,"boletos")
print("Y se vendió un total de",acc,"pesos")
