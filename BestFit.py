memoria = [' '] * 100  # Inicializa a memória com espaços livres

def aloca_memoria_best_fit(tamanho):  
    for i in range(len(memoria)):  
        if memoria[i] == ' ':  
            if i + tamanho <= len(memoria):  
                memoria[i:i+tamanho] = ['x'] * tamanho  
                return True  
    return False  

while True:  
    print("1 - Alocação de memória usando Best Fit")
    print("2 - Sair")
    opcao = int(input("Escolha uma opção: "))
    
    if opcao == 1:
        tamanho = int(input("Digite o tamanho da informação a ser alocada: "))
        if aloca_memoria_best_fit(tamanho):
            print("Memória alocada com sucesso.")
        else:
            print("Não foi possível alocar a memória.")
    elif opcao == 2:
        break  # Encerra o loop while.
    else:
        print("Opção inválida.")

# Imprime o estado final da memória
print("\nEstado final da memória:")
for i in range(len(memoria)):
    print(f"Posição {i}: {'x' if memoria[i] == 'x' else ' '}", end=" ")
