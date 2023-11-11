temp_w=0
cnt=0
cnt_1=0
n=int(input("¿Cuántas lecturas tienes?"))
for i in range(n):
  cnt=i
  temp=int(input("Dame la lectura"))
  if(temp<10 or temp>40):
    temp_w+=1
    cnt_1+=1
porcentaje=cnt_1/n*100
print("El sensor tuvo",cnt_1,"fallos")
print("El porcentaje de error es del",porcentaje,"%")
