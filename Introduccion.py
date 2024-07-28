# Primer Hello World en Python
print("Hola");
saludo = "Hello, World!";
print(saludo);

# Creacion de variables
car_1 = "Porshe";
city = "Miami";
device_type = "Apple";
name = "Karin";

# Las variables se denominan variables porque los valores que almacenan pueden cambiar,
# podemos actualizar esos valores
status = "Watching Netflix";
status = "Relaxing at the beach";
print(status);

# Tambien podemos darle a las variables valores de otras variables
default_opcion = "Upload"
new_status = "Download"

new_status = default_opcion
print(new_status)

# Suma, resta, multiplicacion, division
# Podemos sumar valores de cadenas con un "+"
print("Followers:" + "55");

followers = "55"
print("Followers: " + followers)

label = "Posts: " + "13"
print(label)

tittle = "Ing. "
name = "Diedereich"
print(tittle + name)

# Los valores numericos no usan comillas (No son cadenas)
active_users = 5

number_of_applications = 5 + 1
print(number_of_applications)

percent = 0.5 * 100
print(percent)

number_of_steps = 70
print("You're on step: ")
print(number_of_steps + 1)

private = 3
public = 10
total = private + public
print("Total posts: ") 
print(total)

# True & False
# Hay un valor que no es una cadena ni un numero: True 
# No esta entre comillas ni es un valor numerico 
correct = True
print(correct)

# False es otro valor especial y el opuesto de True 
print("Load data")
status = False
print(status)

# El código notque se encuentra delante de True hace que 
# el resultado de la expresión sea False. Si algo no es 
# verdadero, tiene que ser falso.

# no tes el operador de negación. Convierte los valores en su opuesto
print(not True)
print(not False)

available = True
print(not available)

morning = True
is_evening = not morning
print(is_evening)

# Comprobacion de igualdad de numeros
# Comparacion de numeros
entered_pin = 5448
expexted_pin = 5440

# Para comparar si dos numeros son iguales, utilizamos "=="
# 5 == 5
# Al comparar solo hay 2 resultados: True o False
print(10 == 10)
print(9 == 10)

votes = 10
print(votes == 11)

# Para comprobar si un numero no es igual a otro numero usamos "!="
print(1 != 10)

result = 1 != 2 # Comparacion de desigualdad
print(result)

result = 1 == 2 # Comparacion de igualdad
print (result)

one = 1
two = 2
print(one == two) #  Ter = False 
print(one != two) # Ter = True

vote_count = 99
target = vote_count == 100
print(target) # Ter = False

orders = 1000
capacity = orders == 1000
print(capacity) # Ter = True

score_one = 100
score_two = 80 
print(score_one != score_two) # Ter = True

# Formatos de cadenas
# Mostrar diferentes tipos de valores juntos en la consola
print("new " + "messages") # Ter = new messages

# No se puede usar un valor numerico con cadenas
# las f-strings, abreviatura de cadenas formateada, nos permiten
# mostrar expresiones como agregar una cadena a un numeros, 
# sin ningun error
print(f"{2} new messages") # Ter = 2 new messages

print(f"{6} new messages ") # Ter = 6 new messages

new_messages = 2
print(f"{new_messages} new messages") # Ter = 2 new messages

new = 5
read = 2
print(f"{new - read} unread messages") # Ter = 3 unread messages

# Podemos usar llaves para insertar valores con la frecuencia
# que queramos dentro de la cadena f.
print(f"{5} new messages and {2} friend requests")
# Ter = 5 new messages and 2 friend requests

new = 5
status = f"{new} new messages"
print(status) # Ter = 5 new messages

print(f"populariey increased by {12}%") # Se puede agregar en 
# cualquier lugar
print(f"I would walk {500} miles") # Ter = I would walk 500 miles

degrees = 70
print(f"Temperature: {degrees}F") # Ter = Temperature: 70%

movie = "Vertigo"
display = f"Airing tonight: {movie}"
print(display) # Ter = Airing tonight: Vertigo