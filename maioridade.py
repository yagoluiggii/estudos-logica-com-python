def verificar_maioridade(idade: int) -> str:
    """Verifica se uma idade corresponde à maioridade civil."""
    if idade >= 18:
        return "Maior de idade"
    return "Menor de idade"

def executar_maioridade():
    """Executa a interface interativa de maioridade no terminal."""
    print("\n--- 🔞 Verificador de Maioridade ---")
    try:
        idade = int(input("Digite a sua idade: "))
        if idade < 0:
            print("❌ Erro: A idade não pode ser um valor negativo!")
            return
        resultado = verificar_maioridade(idade)
        print(f"Resultado: Você é {resultado}.")
    except ValueError:
        print("❌ Erro: Digite um número inteiro válido para a idade!")
