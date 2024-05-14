class firstFit:
    def FirstFit(bloco, processo, tam_bloco, tam_processo):
        alocacao = [-1] * tam_processo  # Inicializando a lista de alocação com -1

        for i in range(tam_processo):
            # Procurando o primeiro bloco com tamanho suficiente para o processo atual
            for j in range(tam_bloco):
                if bloco[j] >= processo[i]:
                    alocacao[i] = j
                    bloco[j] -= processo[i]
                    break

        # Imprimindo os resultados
        print("\nN° do Processo.\tTam. Processo \tN° do Bloco.\n", end="")
        for i in range(tam_processo):
            print(str(i + 1) + "\t\t" + str(processo[i]) + "\t\t", end="")
            if alocacao[i] != -1:
                print(str(alocacao[i] + 1))
            else:
                print("Não alocado", end="")
                print("")

bloco = [15, 20, 25]
processo = [10, 6, 10, 9, 1]
tam_bloco = len(bloco)
tam_processo = len(processo)

firstFit.FirstFit(bloco, processo, tam_bloco, tam_processo)