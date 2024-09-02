def is_fibonacci(n):
#verifica se um número fazer parte da sequência de Fibonacci
    if n < 0:
        return False
    
    a, b = 0, 1
    while a <= n:
        if a == n:
            return True
        a, b = b, a + b
    return False

def main():
    number = int(input("Digite um numero para verificar se ele fazer parte da sequencia de Fibonacci: "))
    
    if is_fibonacci(number):
        print(f"{number} fazer parte da sequencia de Fibonacci.")
    else:
        print(f"{number} NÃO faz parte da sequencia de Fibonacci.")

if __name__ == "__main__":
    main()
