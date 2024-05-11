
class nextFit:
    def NextFit(bloco, processo, tam_bloco, tam_processo):
        alocacao = [-1] * tam_processo  # Inicializando a lista alocacao com -1
        
        for i in range(tam_processo):
            j = 0  # Reinicializa j a cada iteração do loop externo
            while (j < tam_bloco):
                if bloco[j] >= processo[i]:
                    alocacao[i] = j
                    bloco[j] -= processo[i]
                    break
                j = (j+1)
                print(j)
            
        print("\nN° do Processo.\tTam. Processo \tN° do Bloco.\n", end="")
        
        for i in range(tam_processo):
            print(str(i+1) + "\t\t" + str(processo[i]) + "\t\t", end="")
            
            if (alocacao[i] != -1):
                print(str(alocacao[i] + 1))
            else:
                print("Não alocado", end="")
                
            print("")