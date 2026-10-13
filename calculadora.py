def somar(a: float, b: float) -> float:
    """Retorna a soma de dois números."""
    return a + b

def subtrair(a: float, b: float) -> float:
    """Retorna a subtração de dois números."""
    return a - b

def executar_calculadora():
    """Executa a interface interativa da calculadora no terminal."""
    print("\n---  Calculadora Simples ---")
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        
        print(f"Soma: {somar(num1, num2)}")
        print(f"Subtração: {subtrair(num1, num2)}")
    except ValueError:
        print(" Erro: Por favor, digite apenas números válidos!")
