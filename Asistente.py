txt=input()
cnt=0
cnt=txt.split().count("Alexa")
if cnt>=2:
  print("Tranquilo, solo di mi nombre una vez")
else:
  print("Dime,¿Cómo te puedo ayudar?")
