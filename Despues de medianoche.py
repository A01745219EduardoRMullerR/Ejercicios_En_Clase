#encoding: UTF-8
#Autor: Eduardo R. Müller Romero
#Escribe un programa que reciba los segundos que han pasado desde la media noche y regrese la hora actual

segundos = int(input("¿Cuántos segundos han pasado desde la medianoche? "))
horas = segundos // 3600
minutos = (segundos % 3600) // 60
_segundos = (segundos % 3600) % 60

print("Estimo que la hora actual es de %i:%02i:%02i" % (horas, minutos, _segundos))
