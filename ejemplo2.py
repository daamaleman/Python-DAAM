# Leer un numero y mostrar la tabla de multiplicar

num = int(input("Dime un numero: "))
for i in range(1, 13):
    print(f"{num} * {i} = {i*num}")