def NextFit(bloco, processo, tam_bloco, tam_processo):
    alocacao = [-1] * tam_processo  # Inicializando a lista alocacao com -1
    
    for i in range(tam_processo):
        j = 0  # Reinicializa j a cada iteração do loop externo
        while (j < tam_bloco):
            if bloco[j] >= processo[i]:
                alocacao[i] = j
                bloco[j] -= processo[i]
                break
            j = (j+1) % tam_bloco
        
    print("\nProcesso No. \tProcesso Size \tBlock no.\n", end="")
    
    for i in range(tam_processo):
        print(str(i+1) + "\t\t" + str(processo[i]) + "\t\t", end="")
        
        if (alocacao[i] != -1):
            print(str(alocacao[i] + 1))
        else:
            print("Não alocado", end="")
            
        print("")

bloco = [5, 10, 20]  # Corrigido
processo = [40, 10, 5]  # Corrigido
tam_bloco = len(bloco)
tam_processo = len(processo)

NextFit(bloco, processo, tam_bloco, tam_processo)