#encoding: UTF-8
#autor :Eduardo Müller
#Escribe un programa que lea el peso y la altura de una persona e imprima el índice de masa corporal con 2 decimales

peso= float(input("Teclea tu peso en kg: "))
altura = float(input("Teclea tu estatura en metros: "))
IMC = peso / (altura ** 2)
print("Tu índice de masa corporal es de %.2f" % IMC)