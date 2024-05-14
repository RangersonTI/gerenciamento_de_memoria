class nextFit:
    def NextFit(bloco, processo, tam_bloco, tam_processo):
        
        alocacao = [-1] * tam_processo  # Inicializando a lista alocacao com -1
        t = tam_bloco - 1
        cont = 0  # Inicializa cont a cada iteração do loop externo

        for i in range(tam_processo):
            while (cont < tam_bloco):
                if bloco[cont] >= processo[i]:
                    alocacao[i] = cont
                    bloco[cont] -= processo[i]
                    t = (cont - 1) % tam_bloco
                    break

                if t == cont:
                    break
 
                cont = (cont + 1)

        print("\nN° do Processo.\tTam. Processo \tN° do Bloco.\n", end="")

        print("\nN° do Processo.\tTam. Processo \tN° do Bloco.\n", end="")
        for i in range(tam_processo):
            print(str(i + 1) + "\t\t" + str(processo[i]) + "\t\t", end="")
            if alocacao[i] != -1:
                print(str(alocacao[i] + 1))
            else:
                print("Não alocado", end="")

bloco = [15, 20, 25, 20]
processo = [10, 6, 10, 9, 1, 12, 15, 8]
tam_bloco = len(bloco)
tam_processo = len(processo)

nextFit.NextFit(bloco, processo, tam_bloco, tam_processo)