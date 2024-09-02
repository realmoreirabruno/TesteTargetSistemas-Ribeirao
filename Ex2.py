def counter(s):
#contar a ocorrência de a ou A
    count = s.lower().count('a')
    return count

def main():
    input_string = input("Digite uma string para verificar a quantidade de letras a: ")
    
#contagem letras a
    count = counter(input_string)
    
    if count > 0:
        print(f"A letra a ou A ocorre {count} vezes na string.")
    else:
        print("A letra a ou A nao ocorre na string.")

if __name__ == "__main__":
    main()
