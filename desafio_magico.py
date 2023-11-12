gryffindor_score=0
slytherin_score=0
n=int(input("Ingresa el número de eventos en el partido de Quidditch"))
for i in range (n):
  e=input("Ingresa el evento goal/snitch/foul ")
  c=input("¿Qué equipo (Gryffindor/Slytherin) ")
  if c=="Gryffindor" or c=="gryffindor":
    if e=="Goal" or e=="goal":
      gryffindor_score+=10
    elif e=="Snitch" or e=="snitch":
      gryffindor_score+=150
    elif e=="Foul" or e=="foul":
      gryffindor_score=gryffindor_score-30
  elif c=="Slytherin" or c=="slytherin":
    if e=="Goal" or e=="goal":
      slytherin_score+=10
    elif e=="Snitch" or e=="snitch":
      slytherin_score+=150
    elif e=="Foul" or e=="foul":
      slytherin_score=slytherin_score-30

print("Gryffindor",gryffindor_score,"puntos")
print("Slytherin",slytherin_score,"puntos")
if gryffindor_score>slytherin_score:
  print("Gana Gryffindor")
elif slytherin_score>gryffindor_score:
  print("Gana Slytherin")
elif gryffindor_score==slytherin_score:
  print("Empate")
