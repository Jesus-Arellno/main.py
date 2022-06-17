#loguin
def loguin():
  usuarios = ['admin','usuario1','usuario2','usuario3']
  contraseñas = ['pas1','pas2','pas3','pas4']
  acceso = False
  while True :
    usuario = input("ingrese su usuario: ")
    pasword = input("ingrese su contraseña: ")
    if usuario in usuarios and pasword in contraseñas:
      print(usuario)
      if usuarios.index(usuario) == contraseñas.index(pasword):
        acceso = True
        break
      else:
        print("ingrese contrasena valida")
    else:
      print("usuario no balido")

  if acceso:
    print("analisis de dartos")
    