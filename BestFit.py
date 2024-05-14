def melhorEncaixe(tamanhoBloco, m, tamanhoProcesso, n):
    # Armazena o ID do bloco alocado para cada processo
    alocacao = [-1] * n 
    
    # Para cada processo, encontre os blocos adequados de acordo com seu tamanho e atribua a ele
    for i in range(n):
        # Encontre o bloco de melhor encaixe para o processo atual
        melhorIdx = -1
        for j in range(m):
            if tamanhoBloco[j] >= tamanhoProcesso[i]:
                if melhorIdx == -1: 
                    melhorIdx = j 
                elif tamanhoBloco[melhorIdx] > tamanhoBloco[j]: 
                    melhorIdx = j
  
        # Se pudermos encontrar um bloco para o processo atual
        if melhorIdx != -1:
            # aloque o bloco j para o processo p[i] 
            alocacao[i] = melhorIdx 
            # Reduza a memória disponível neste bloco
            tamanhoBloco[melhorIdx] -= tamanhoProcesso[i]
  
    print("No. Processo  Tamanho do Processo  Número do Bloco")
    for i in range(n):
        print(i + 1, "     	", tamanhoProcesso[i], end="     	") 
        if alocacao[i] != -1: 
            print(alocacao[i] + 1) 
        else:
            print("Não Alocado")
  
# Código de execução 
if __name__ == '__main__': 
    tamanhoBloco = [100, 500, 200, 300, 600] 
    tamanhoProcesso = [212, 417, 112, 426] 
    m = len(tamanhoBloco) 
    n = len(tamanhoProcesso) 
  
    melhorEncaixe(tamanhoBloco, m, tamanhoProcesso, n)
