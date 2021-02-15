from datetime import date
from datetime import datetime
import math

anoNacimiento = int(input("Introduce año de nacimiento: "))
mesNacimiento = int(input("Introduce mes de nacimiento: "))
diaNacimiento = int(input("Intorduce dia de nacimimiento: "))

def diasVividos(ano, mes, dia):
    fechaHoy = datetime.now()
    fechaNacimiento = datetime(ano, mes, dia, 0, 0, 0, 0)
 
    anoDia = (fechaHoy.year - fechaNacimiento.year)*360
    mesDia = (fechaHoy.month - fechaNacimiento.month)*30
    totalDias =  anoDia + mesDia + fechaNacimiento.day + fechaHoy.day
    return(totalDias)

def cicloFisico():
    fisico = math.sin((math.pi * diasVividos(anoNacimiento, mesNacimiento, diaNacimiento))/23)
    return fisico

print("Dias vividos: " + str( diasVividos(anoNacimiento, mesNacimiento, diaNacimiento)))
print("Tu ciclo fisico es: " + str(cicloFisico()))