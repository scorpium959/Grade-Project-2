import platform
import os
import os.path

path = os.path
if (platform.system() == "Linux"):
  os.system("clear")
else:
  os.system("cls")

def Error_Checker_int (data):
  temp = data
  while (True):
    try:
      temp = int(float(temp))
      break
    except ValueError:
      print("Tipo de dato erróneo.")
    temp = input("intente de nuevo: ")
  return temp

def Question (data):
  temp = Error_Checker_int(input(f"Por favor, ingrese {data}: "))
  return temp

def Calc (puntaje_max, puntaje_obt, exigencia, nota_max, nota_min, nota_apr):
  global punobt
  global punmax
  global exig
  global notamin
  global notamax
  global notaapr
  punobt = puntaje_obt
  punmax = puntaje_max
  exig = exigencia
  notamin = nota_min
  notamax = nota_max
  notaapr = nota_apr

  while (punobt < 0 or punmax <= 0 or exigencia <= 0 or nota_min < 0 or nota_max < 0 or notamin >= notamax or punobt > punmax or notaapr <= 0 or notamax <= notaapr or notaapr < notamin):
    if (punobt < 0):
      print(f"su puntaje obtenido es incorrecto o menor que cero. \nIntente de nuevo.")
      punobt = Question("el puntaje obtenido en esa evaluación")
    if (punmax <= 0):
      print(f"El puntaje máximo ({puntaje_max}) es invalido (cero o menor).\nIntente de nuevo.")
      punmax = Question("el puntaje máximo de su evaluación o prueba")
    if (exig <= 0):
      print(f"Su exigencia es igual o menor que cero, por lo que tiene que intentar de nuevo.")
      exig = Question("el porcentaje de exigencia de su evaluación (sin el símbolo de porcentaje, %)")/100
    if (notamin < 0):
      print(f"Su nota mínima ({notamin}) es menor que cero, porfavor, considere cambiarla.")
      notamin = Question("la nota mínima de su evaluación")
    if (punobt > punmax):
      print(f"El puntaje que escribió es mayor al máximo ({punobt}).")
      punobt = Question("de nuevo el puntaje obtenido en su evaluación")
    if (notamin >= notamax):
      print(f"su nota minima supera a la maxima ({notamin} > {notamax}).\nIntente de nuevo.")
      notamax = Question("la nota máxima de su evaluación")
      notamin = Question("la nota minima")
    if (notamax <= 0):
      print(f"Su nota máxima es 0 o menor ({notamax}), por favor, ingrese de nuevo el valor.")
      notamax = Question("la nota máxima de su evaluación")
    if (notaapr <= 0):
      print(f"su nota minima de aprobación no es valida ({notaapr}).\nIntente de nuevo.")
      notaapr = Question("la nota mínima de aprobación (Generalmente 4.0)")
      if (notaapr >= notamin):
        break
    if (notaapr >= notamax):
      print(f"Su nota minima de aprobación ({notaapr}) supera a la máxima ({notamax}).\nIntente de nuevo.")
      notaapr = Question("la nota mínima de aprobación (Generalmente 4.0)")
      notamax = Question("la nota máxima de su evaluación")
    if (notaapr < notamin):
      print(f"su nota minima de aprobación es menor que la minima ({notaapr} < {notamin}).")
      notaapr = Question("la nota mínima de aprobación (Generalmente 4.0)")
      notamin = Question("la nota minima")
    if (punobt <= punmax and punobt > 0 and notaapr >= notamin and notaapr <= notamax and exig > 0 and exig <= 100 and notamin >= 0 and notamax > notamin):
      break

  if (punobt < exig * punmax):
    n = float((notaapr - notamin) * (punobt / (exig * punmax)) + notamin)
    n = round(n, 1)
  else:
    n = float((notamax - notaapr) * ((punobt - exig * punmax) / (punmax * (1 - exig))) + notaapr)
    n = round(n, 1)
  return n


def save_file (puntaje_max, puntaje_obt, nota):
  if (path.exists("notas.txt")):
    f = open("notas.txt", "a")
    nombre = input("Quiere dejar un nombre o asignatura enlazado con la nota? \nEscríbalo (de caso contrario, no agregue nada y de Enter): ")
    f.write("\nPuntaje máximo: "+ str(punmax) + ", Puntaje: " + str(punobt) + ", Nota: " + str(nota) + " " + nombre)
    f.close()
  else:
    f = open("notas.txt", "w")
    nombre = input("Quiere dejar un nombre o asignatura enlazado con la nota? \nEscríbalo (de caso contrario, no agregue nada y de Enter): ")
    f.write("Puntaje máximo: " + str(punmax) + ", Puntaje: " + str(punobt) + ", Nota: " + str(nota) + " " + nombre)
    f.close()

print("\"Grade Project\", Programa Re-implementado y basado en \"escaladenotas.cl\" (Juan Pumarino Rodríguez), Hecho por Vicente Martínez, BetaTesting practicado por Felipe Toro")
print("Por favor, considere el usar punto (.) para los decimales en vez de la coma (,)")
Repeat = "Si"
times = 0

while (Repeat == "Si" or Repeat == "si" or Repeat == "s" or Repeat == "sI" or Repeat == "SI"):
  if (times >= 1):
    RepeatDirectives = input(f"Directivas:\nNota Máxima: {notamax}\nNota Mínima: {notamin}\nExigencia: {int(exig * 100)}\nNota mínima de aprobación: {notaapr}\nQuiere repetir el proceso con las mismas directivas de calculo? (si/no): ")
    if (RepeatDirectives == "Si" or RepeatDirectives == "si" or RepeatDirectives == "s" or RepeatDirectives == "SI" or RepeatDirectives == "sI"):
      punmax = Question("el puntaje máximo de su evaluación")
      punobt = Question("el puntaje obtenido en esa evaluación")
      resultado = Calc(punmax, punobt, exigencia, notamax, notamin, notaapr)
      print(f"El resultado es: {resultado}")
      save_file(punmax, punobt, resultado)
    else:
      notamax = Question("la nota máxima de su evaluación")
      notamin = Question("la nota mínima de su evaluación")
      notaapr = Question("la nota mínima de aprobación (Generalmente 4.0)")
      exigencia = Question("el porcentaje de exigencia de su evaluación (sin el símbolo de porcentaje, %)")/100
      while (exigencia >= 1):
        print(f"Su exigencia ({exigencia}) es mayor de 100%.\nIntente de nuevo, por favor.")
        exigencia = Question("el porcentaje de exigencia de su evaluación (sin el símbolo de porcentaje, %)")/100
      punmax = Question("el puntaje máximo de su evaluación o prueba")
      punobt = Question("el puntaje obtenido en esa evaluación")
      resultado = Calc(punmax, punobt, exigencia, notamax, notamin, notaapr)
      print(f"El resultado es: {resultado}")
      save_file(punmax, punobt, resultado)
  else:
    notamax = Question("la nota máxima de su evaluación")
    notamin = Question("la nota mínima de su evaluación")
    notaapr = Question("la nota mínima de aprobación (Generalmente 4.0)")
    exigencia = Question("el porcentaje de exigencia de su evaluación (sin el símbolo de porcentaje, %)")/100
    while (exigencia >= 1):
      print(f"Su exigencia ({exigencia}) es mayor de 100%.\nIntente de nuevo, por favor.")
      exigencia = Question("el porcentaje de exigencia de su evaluación (sin el símbolo de porcentaje, %)")/100
    punmax = Question("el puntaje máximo de su evaluación o prueba")
    punobt = Question("el puntaje obtenido en esa evaluación")
    resultado = Calc(punmax, punobt, exigencia, notamax, notamin, notaapr)
    print(f"El resultado es: {resultado}")
    save_file(punmax, punobt, resultado)

  Repeat = input("Quiere repetir el proceso? (si/no): ")
  while (Repeat == "" or Repeat == " "):
    Repeat = input("Quiere repetir el proceso? (si/no): ")
  times += 1
