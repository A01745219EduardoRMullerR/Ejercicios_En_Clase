#encoding: UTF-8
#Autor: Eduardo Roberto Müller Romero, A01745219

print("Este programa funciona con calificaciones en base 0/100")
Examen1 = int(input("Calificación del primer examen: "))
Examen2 = int(input("Calificación del segundo examen: "))
Examen3 = int(input("Calificación del tercer examen: "))
Examen4 = int(input("Calificación del cuarto y ultimo examen: "))

valor1 = Examen1 * .4
valor2 = Examen2 * .2
valor3 = Examen3 * .1
valor4 = Examen4 * .3

Calificacion_Final = valor1 + valor2 + valor3 + valor4
print("Tu promedio de exámenes es", Calificacion_Final)