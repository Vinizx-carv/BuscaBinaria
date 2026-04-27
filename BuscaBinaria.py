
#Função receber a lista já ordenada e o valor para ser procurado
def buscaBinaria(vetor, alvo):
        inicio = 0
        fim = len(vetor) - 1

        while (fim >= inicio):
            meio = (inicio + fim) // 2

            if vetor[meio] == alvo:
                return vetor[meio]
            elif vetor[meio] < alvo:
                inicio = meio + 1
            else:
                fim = meio - 1
        # Retorna -1 quando o elemento procurado não existe
        return -1

v2 = [10, 23, 35, 47, 59, 61, 72, 84, 95, 107,
115, 126, 138, 149, 150, 162, 174, 185, 197, 209,
220, 233, 245, 256, 268, 279, 290, 305, 317, 329,
340, 352, 364, 375, 386, 398, 410, 421, 433, 445,
456, 468, 479, 490, 502, 514, 525, 537, 549, 560,
572, 583, 595, 607, 618, 630, 642, 653, 665, 677,
688, 700, 712, 723, 735, 747, 758, 770, 782, 793,
805, 817, 828, 840, 852, 863, 875, 887, 898, 910,
922, 933, 945, 957, 968, 980, 992, 1003, 1015, 1027,
1038, 1050, 1062, 1073, 1085, 1097, 1108, 1120, 1132, 1143]

print(buscaBinaria(v2, 10))
