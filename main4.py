def repetir():
    numero = 0
    while  numero  <11:
        resultado = numero * numero
        numero = numero + 1
        print(resultado)
repetir()

def enquanto():
     escolher = int(input("AAAAAAAA"))
     zero = 0
     while zero < escolher:
          zero = zero + 2
          print(zero)
enquanto()

def fatorial():
    num = int(input("Digite um número: "))
    resultado = 1
    while num > 0:
        resultado *= num
        num -= 1
    print(f"O fatorial é: {resultado}")
fatorial()

def vogal():
    palavra = input("Digite uma palavra: ")
    contagem = 0  # Inicializa a contagem de vogais

    for letra in palavra.lower():  # Converte para minúsculas para facilitar a verificação
        if letra in "aeiou":  # Verifica se a letra é uma vogal
            contagem += 1
    
    print(f"A palavra possui {contagem} vogais.")

vogal()

def maior_q_zero():
    usuario = float(input("DIGITa"))
    num = 0
    while usuario < num: 
        usuario = int(input("Digiteeeeeeeeeeeeee"))
    if usuario > num: 
        print("Break")
    else:
        print("Numero")
        
maior_q_zero()

def menu():
    menu1 = ("Abacate", "Entrada", "Sobremesa", "Sair")

    while True: 
        escolha = input("Escolha uma das opções (Abacate, Entrada, Sobremesa, Sair): ")

        if escolha in menu1:  
            if escolha == "Sair":
                print("Encerrando o menu...")
                break 
            else:
                print(f"Você escolheu: {escolha}")
        else:
            print("Opção inválida, tente novamente.")

menu()
    
