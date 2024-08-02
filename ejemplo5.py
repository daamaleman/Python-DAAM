# Factorial de un numero con while

def factorial(num):
    fact = 1
    i = 1
    while i <= num:
        fact *= i 
        i += 1
    return fact

def main():
    num = int(input("Dime un numero: "))
    print(factorial(num)) # La multiplicacion de todos sus antecesores

main()