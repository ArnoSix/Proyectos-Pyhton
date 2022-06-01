
titulo = ("Bienvenido a al test Gamer uwu\n")
print("\n" + titulo + "\n" + "_" * len(titulo) + "\n")

puntuacion = 0

opcion = input ('''pregunta 1: que haces cuando te enojas por los troll
                A: Apagas la pc.
                B: Sigo jugando y reporto.
                C: Me relajo y trato de ayudar al team.''')

if opcion == "A":
    puntuacion = puntuacion + 0

elif opcion == "B":
    puntuacion = puntuacion + 5

elif opcion == "C":
    puntuacion = puntuacion + 10
else:
    print("Las opciones posibles A, B, C")
    exit()

opcion = input ('''Pregunta 2: Te gustaria jugar de forma profecional 
                A: Si
                B: No
                C: Prefiero estudiar''')
if opcion == "A":
    puntuacion = puntuacion + 0

elif opcion == "B":
    puntuacion = puntuacion + 5

elif opcion == "C":
    puntuacion = puntuacion + 10
else:
    print("Las opciones posibles A, B, C")
    exit()

opcion = input ('''pregunta 3: Te gusta mas los juegos de roll o los shotter 
A: roll
B: shotter
C: Minicraft''')

if opcion == "A":
    puntuacion = puntuacion + 0

elif opcion == "B":
    puntuacion = puntuacion + 5

elif opcion == "C":
    puntuacion = puntuacion + 10
else:
    print("Las opciones posibles A, B, C")
    exit()
   
if puntuacion >= 25:
    print ("Felicidades eres un Gamer experto")
elif puntuacion >= 15:
    print ("Eres un gamer casual") 
else:
    print ("Eres un gamer casual") 