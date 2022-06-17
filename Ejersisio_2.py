numero = 1000000
print(numero)

numero = 1_000_000
print(numero)

#tipos de variable
variable1 = 12
variable2 = 13.0
variablec =  variable1 + variable2
#imprecion de tipo de variable
print(type(variablec))

variablec = "carlos"
print (type(variablec))

print(variablec * 5)

numero = 1000000
print(numero)

numero = 1_000_000
print(numero)

texto_numero = str(numero)
print(texto_numero)

nombre = "carlos"
apellido = "perez"
print(nombre,apellido)
#elentos con mayuscula y minusculas
print(nombre.lower(),apellido.upper())


# variable con el nombre
name ="antonio"
print(name)
# imprimir entrada de texto
letra = input("ingresa una letra")
print(name[0],letra,name[2:])



# asicnacion de variable con entradad de texto
palabra = input("Ingrese una palabra a analisar: ")
# identificacio de caracteres en la cadena de texto
cont_vocal = palabra.count("a")
cont_vocal+=palabra.count("e")
cont_vocal+=palabra.count("i")
cont_vocal+=palabra.count("o")
cont_vocal+=palabra.count("u")
#muestra el contenido del contador con espesificacion
print("su palabra tiene: #",cont_vocal,"vocales")
