# O codigo foi analizado e corrigido via ChatGPT
# O uso da ferramenta se deve a estudos autônomos
# Apenas as seções com comentário abaixo foram modificados
# O código em si foi produzido manualmente

def main():
    print("Hello World!")
    print("Sou um conversor de temperatura!")
    print("Digite o valor da temperatura...:")
    
    temperatura_origem = float(input())  # Convertido para float para realizar cálculos

    print("Qual a escala dessa temperatura?")
    print("OBS: Digite o numero da escala desejada.")
    print("1 - Celsius")
    print("2 - Fahrenheit")
    print("3 - Kelvin")

    escala_origem = input()  # Removido o erro de sintaxe

    if escala_origem == "1":
        print("Para qual escala você deseja converter?")
        print("1 - Fahrenheit")
        print("2 - Kelvin")
        
        escala_desejada = input()

        if escala_desejada == "1":
            resultado = (temperatura_origem * 9/5) + 32
            print(f"{temperatura_origem} graus Celsius é igual a {resultado:.2f} graus Fahrenheit.")
        elif escala_desejada == "2":
            resultado = temperatura_origem + 273.15
            print(f"{temperatura_origem} graus Celsius é igual a {resultado:.2f} Kelvin.")
        else:
            print("Escolha inválida. Por favor, escolha 1 ou 2.")

    elif escala_origem == "2":
        print("Para qual escala você deseja converter?")
        print("1 - Celsius")
        print("2 - Kelvin")
        
        escala_desejada = input()

        if escala_desejada == "1":
            resultado = (temperatura_origem - 32) * 5/9
            print(f"{temperatura_origem} graus Fahrenheit é igual a {resultado:.2f} graus Celsius.")
        elif escala_desejada == "2":
            resultado = (temperatura_origem + 459.67) * 5/9  # Corrigido o cálculo
            print(f"{temperatura_origem} graus Fahrenheit é igual a {resultado:.2f} Kelvin.")
        else:
            print("Escolha inválida. Por favor, escolha 1 ou 2.")

    elif escala_origem == "3":
        print("Para qual escala você deseja converter?")
        print("1 - Celsius")
        print("2 - Fahrenheit")
        
        escala_desejada = input()

        if escala_desejada == "1":
            resultado = temperatura_origem - 273
            print(f"{temperatura_origem} Kelvin é igual a {resultado:.2f} graus Celsius.")
        elif escala_desejada == "2":
            resultado = (temperatura_origem - 273) * 9/5 + 32  # Corrigido o cálculo
            print(f"{temperatura_origem} Kelvin é igual a {resultado:.2f} graus Fahrenheit.")
        else:
            print("Escolha inválida. Por favor, escolha 1 ou 2.")
    
    else:
        print("Escolha inválida")

if __name__ == "__main__":
    main()
