#encoding: UTF-8
#Autor: Eduardo R. Müller Romero, A01745219
#Se calcula el area de una figura en forma de helado (circunferencia y triangulo)

Radio = int(input("¿Cuál es el radio(R) de la figura?"))
Altura = int(input("¿Cuál es la altura(h) de la figura?"))

Area = ((3.1416 * (Radio**2)) / 2) + ((2 * Radio * Altura) / 2)
print("El area total de la figura es de:", Area)