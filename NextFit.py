class nextFit:
    def NextFit(bloco, processo, tam_bloco, tam_processo):
        
        alocacao = [-1] * tam_processo  # Inicializando a lista alocacao com -1
        t = tam_bloco - 1
        cont = 0  # Reinicializa j a cada iteração do loop externo

        for i in range(tam_processo):
            while (cont < tam_bloco):
                print("\t",i,"")
                if bloco[cont] >= processo[i]:
                    alocacao[i] = cont
                    bloco[cont] -= processo[i]
                    t = (cont - 1) % tam_bloco
                    print(t)
                    break

                if t == cont:
                    # sets a new end point
                    t = (cont - 1) % tam_bloco
                    print(t)
                    # breaks the loop after going through all memory block
                    break

                cont = (cont + 1) % tam_bloco
            #print(cont)

        print("\nN° do Processo.\tTam. Processo \tN° do Bloco.\n", end="")

        for i in range(tam_processo):
            print(str(i+1) + "\t\t" + str(processo[i]) + "\t\t", end="")
            if (alocacao[i] != -1):
                print(str(alocacao[i] + 1))
            else:
                print("Não alocado", end="")

            print("")

bloco = [1, 12, 12, 12]
processo = [10, 20, 51, 34, 11, 11, 11, 11]
tam_bloco = len(bloco)
tam_processo = len(processo)

nextFit.NextFit(bloco, processo, tam_bloco, tam_processo)