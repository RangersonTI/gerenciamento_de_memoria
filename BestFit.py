# Inicializa a memória com espaços livres
memoria = [' '] * 100   # aqui sera uma lista que chamei memoria que ocupa 100 espaços

def aloca_memoria_best_fit(tamanho):  # função que sera alocado o tamanho da lista 
    for i in range(len(memoria)): # laço de repetição for que sera para itera sobre cada posição na lista
        if memoria[i] == ' ' and tamanho <= len(memoria) - i:  # verificar se  a lista esta vazia
            memoria[i:i+tamanho] = ['x'] * tamanho  # Atribui 'x' para o tamanho especificado
            return True 
    return False # não houver espaço disponível para alocar o tamanho especificado.

while True: # : Inicia um loop infinito que continuará até que uma condição de saída seja alcançada.

    print("1 - Alocação de memória usando Best Fit")
    print("2 - Sair")
    opcao = int(input("Escolha uma opção: "))
    
    if opcao == 1:
        tamanho = int(input("Digite o tamanho da informação a ser alocada: "))
        if aloca_memoria_best_fit(tamanho):
            print("Memória alocada com sucesso.")
        break # Encerra o loop while.

# Imprime o estado final da memória
print("\nEstado final da memória:")
for i in range(len(memoria)):
    print(f"Posição {i}: {'x' if memoria[i] == 'x' else ' '}", end=" ")

