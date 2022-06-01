import random


numero_ganador = random.randint(1,10)

numero_elegido = int(input("Elige un numero:  "))

if numero_elegido == numero_ganador:
  print("Has ganado!")

if numero_elegido > 10: 
  print("Te has pasado un poco... Era entre 1 y 10")

if numero_elegido < 1:
  print("Has quedado corto... Era entre 1 y 10")

if numero_elegido == 666:
  print("Has elegido el numero de la bestia")

if numero_elegido == -666:
  print("Has elegido el numero de la bestia en negativo eso es doblemente maligno")

print("El numero ganador era: {}".format(numero_ganador))