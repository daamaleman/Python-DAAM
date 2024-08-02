# Leer un numero y decir que dia de la semana es.

semana = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"] # Arreglo
meses = {}

dia = int(input("Dime el numero del dia que quieres saber: "))

print(f"El dia es: {semana[dia - 1]}")
