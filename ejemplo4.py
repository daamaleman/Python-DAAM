# Decir si un numero es par o impar

def esPar(num):
    if(num % 2 == 0):
        return "Es par"
    else:
        return "Es impar"
    
def main():
    num = int(input("Dime un numero: "))
    print(esPar(num))

if __name__ == "__main__":
    main()
