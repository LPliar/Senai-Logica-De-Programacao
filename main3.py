def calculos():
    escolher = 0
    resultado = 0
    while escolher <10 : 
        numero = int(input("Escreva um numero"))
        escolher = escolher + 1
        resultado = resultado + numero
        media = resultado / 10
        if escolher >= 10:
         print(f"Resutado da soma desses numeros é {resultado} e a media é { media}")
        elif numero <-0:
           print("BREAk")
           break
        else:
           print("outro numero")
calculos()