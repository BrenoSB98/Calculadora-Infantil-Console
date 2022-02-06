import math
# coding: UTF-8

# Brincando de Calcular
print("Olá, me chamo Calcubrink. Vamos brincar de Matemática?")

while True:
    # MENU DE OPERAÇÕES
    opcao = int(input(f"""
⚠ MENU DE OPÇÕES ⚠
1 - Adição
2 - Subtração
3 - Multiplicação
4 - Divisão
5 - Exponenciação
6 - Fatorial
7 - Raiz Quadrada
8 - Logaritmo
9 - Trigonomitria
0 - Sair

Por Favor, indice o número de qual Operação vamos brincar: """))
    # CALCULADORA 
    
    # Adição
    if opcao == 1:
        soma = 0
        quant_values = int(input(f"Quantos números vamos somar? "))
        for i in range(1, quant_values + 1):
            value = int(input(f"Digite o {i}º valor: "))
            soma += value
        print(f"O resultado da sua Soma é {soma}.")
    
    #Subtração
    elif opcao == 2:
        quant_values = int(input(f"Quantos números vamos Subtrair? "))
        value1 = int(input(f"Digite o 1º valor: "))
        value2 = int(input(f"Digite o 2º valor: "))
        sub = value1 - value2
        for i in range(3, quant_values + 1):
            value = int(input(f"Digite o {i}º valor: "))
            sub -= value
        print(f"O resultado da sua Subtração é {sub}.")
    
    #Multiplicação
    elif opcao == 3:
        mult = 1
        quant_values = int(input(f"Quantos números vamos Multiplicar? "))
        for i in range(1, quant_values + 1):
            value = int(input(f"Digite o {i}º valor: "))
            mult *= value
        print(f"O resultado da sua Multiplicação é {mult}.")
    
    #Divisão
    elif opcao == 4:
        dividendo = int(input(f"Digite o Dividendo? "))
        divisor = int(input(f"Digite o Divisor: "))
        if divisor > 0:
            div = dividendo/divisor
            print(f'O resultado da divisão é {div}.')
        else:
            print('Não é possível realizar divisão por ZERO')
    
    # Exponenciação
    elif opcao == 5:
        value = int(input(f"Digite um valor: "))
        elevado = int(input(f"Digite a Potencia: "))
        exp = math.pow(value, elevado)
        print(f'O resultado de {value} elevado a {elevado} é {exp}.')
    
    # Fatoração
    elif opcao == 6:
        value = int(input(f"Deseja saber o Fatorial de qual valor?: "))
        fat = math.factorial(value)
        print(f'O Fatorial de {value} é {fat}.')
    
    # Raiz Quadrada
    elif opcao == 7:
        value = int(input(f"Deseja saber a Raiz Quadrada de qual valor? "))
        raiz_quadrada = math.sqrt(value)
        print(f'A Raiz Quadrada de {value} é {raiz_quadrada}.')
    
    # Logaritmo
    elif opcao == 8:
        opcao_logaritmo = int(input(f"""
Qual Logaritmo deseja fazer?
1 - Logaritmo Natural
2 - Logaritmo na Base 2
3 - Logaritmo na Base 10        

Qual das 3 opções deseja realizar? """))
        
        # Logaritmo Natural
        if opcao_logaritmo == 1:
            x = int(input(f"Digite o valor de X: "))
            base = int(input(f"Digite a base: "))
            logn = math.log(x, base)
            print(f'O Logaritmo Natural de {x} na base {base} é {logn}.')
        
        # Logaritmo Base 2
        elif opcao_logaritmo == 2:
            x = int(input(f"Digite o valor de X: "))
            logb2 = math.log2(x)
            print(f'O Logaritmo de {x} na base 2 é {logb2}.')

        # Logaritmo Base 10
        else:
            if opcao_logaritmo == 3:
                x = int(input(f"Digite o valor de X: "))
                logb10 = math.log10(x)
                print(f'O Logaritmo de {x} na base 10 é {logb10}.')
    
    # Trigonomitria
    elif opcao == 9:
        opcao_trigo = int(input(f"""
Qual Função Trigonometrica deseja fazer?
1 - Seno
2 - Cosseno
3 - Tangente        

Qual das 3 opções deseja realizar? """))
        
        # Seno
        if opcao_trigo == 1:
            x = int(input(f"Digite o valor de X: "))
            seno = math.sin(x)
            print(f'O Seno de {x} é {seno}.')
        
        # Cosseno
        elif opcao_trigo == 2:
            x = int(input(f"Digite o valor de X: "))
            cosseno = math.cos(x)
            print(f'O Cosseno de {x} é {cosseno}.')

        # Tangente
        else:
            if opcao_trigo == 3:
                x = int(input(f"Digite o valor de X: "))
                tangente = math.tan(x)
                print(f'A Tangente de {x} é {tangente}.')
    
    else:
        if opcao == 0:
            print(f'ACABOU A BRINCADEIRA 😢😢😢')
            break
