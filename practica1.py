#ejercicio retador 1
def retador1():
  superficie_estado_sinaloa = 57365
  temp_anual_sinaloa = 25.45
  presipitacion_anual_sinaloa = 790.1
  climas_sinaloa = "cálido, subhúmedo, seco y semiseco"
  poblasion_mujeres = 1532128
  poblasion_hombes = 1494815
  poblasion_mazatlan = poblasion_mujeres * .3316 + poblasion_hombes * .3316
  poblasion_culiacan = poblasion_mujeres * .1657 + poblasion_hombes * .1657

  print("La población total entre hombres y mujeres: ", poblasion_hombes+poblasion_mujeres)
  print("El porcentaje total de la población entre Culiacán y Mazatlán:", poblasion_culiacan+poblasion_culiacan)
  print("La temperatura media anual y los tipos de clima: ", temp_anual_sinaloa,"grados centigrados ", climas_sinaloa)

# ejercicio retador 2
def retador2():
  municipios = []
  habitantes = []
  i = 0
  n_abitantes = 0
  promedio_habitantes = 0
  for i in range(3):
    valorm = input("Ingrese el Municipio: ")
    valorh = int(input("Ingresa el número de habitantes:"))
    municipios.append(valorm)
    habitantes.append(valorh)
  for i in range(3):
    n_abitantes +=  habitantes[i] 
  promedio_habitantes = n_abitantes/3
  print("El total de habitantes es: ",n_abitantes)
  print("El promedio de habitantes es: ",promedio_habitantes)

#ejercicio retador 3
def retador3():
  cap_max = 3254
  cap_min = cap_max*.5
  cemento = 40
  yeso = 30
  pepido_cemento = cemento * int(input("cuantos sacos de semento desea: "))
  pedido_yeso = yeso * int(input("cuantos sacos de yeso desea: "))
  peso_pedido = pepido_cemento + pedido_yeso
  if(peso_pedido > cap_min and peso_pedido < cap_max):
    print("pesos total de su pedido es: ", peso_pedido)
    print("su pedido puede ser enviado")
  else:
    print("pesos total de su pedido es: ", peso_pedido)
    print("su pedido no puede ser enviado")