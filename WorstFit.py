def WorstFit(tam_bloco, processo):
    alocação = [-1] * len(processo) # Lista para manter o resultado da alocação    
    for i in range(len(processo)): # Processo para cada processo
        WorstIndice = -1 # Inicializa a variável para manter o índice do maior bloco
        
        for j in range(len(tam_bloco)):
            if tam_bloco[j] >= processo[i]:
                if WorstIndice == -1 or tam_bloco[j] > tam_bloco[WorstIndice]:
                    WorstIndice = j
                    
        if WorstIndice != -1: # Se encontramos um bloco que pode acomodar processes[i]
            alocação[i] = WorstIndice # Aloca o bloco de memória ao processo            
            tam_bloco[WorstIndice] -= processo[i] # Reduz o tamanho do bloco alocado
    
    print("nº do Processo\tTamanho\tnº do bloco") # Imprimir resultado da alocação
    for i in range(len(processo)):
        if alocação[i] != -1:
            print(f"{i + 1}\t\t{processo[i]}\t\t{alocação[i] + 1}")
        else:
            print(f"{i + 1}\t\t{processo[i]}\t\tNão alocado")

# Exemplo de uso:
tam_bloco = [100, 500, 200, 300, 600]
processo = [212, 417, 112, 426]

WorstFit(tam_bloco, processo)
