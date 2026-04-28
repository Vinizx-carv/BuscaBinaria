import time

#  Função receber a lista já ordenada e o valor para ser procurado
def buscaBinaria(vetor, alvo):
    inicio = 0
    fim = len(vetor) - 1

    while (fim >= inicio):

        # Fica na variavel "meio" o valor inteiro da divisão
        meio = (inicio + fim) // 2

        if vetor[meio] == alvo:
            return vetor[meio]
        elif vetor[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1

    # Retorna -1 quando o elemento procurado não existe
    return -1

# Entradas padronizadas
# Vetor com 100 elementos ordenados 
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

# Alvos de busca padronizados:
#   - Início do vetor   (melhor caso)
#   - Meio do vetor     (caso médio)
#   - Fim do vetor      (caso médio/pior)
#   - Elemento ausente  (pior caso)
ALVOS = [
    (10,   "Início (melhor caso)"), #primeiro elemento do v2
    (560,  "Meio   (caso médio) "), #meio elemento do v2
    (1143, "Fim    (caso médio) "), #ultimo elemento do v2
    (999,  "Ausente(pior caso)  "), #inexistência de elemento do v2
]
REPETICOES = 1000   # execuções por alvo para média de tempo]

#===========================================================================================
# anotação para o grupo: como todos os números do v2 estão fixos, coloquei os alvos como 
# fixos também, entretanto, acho legal a ideia de criar um vetor de 100 elementos de números
# aleatórios, e fazer um alvo com base na geração de números randomizados.

# ex.: randomiza 100 números, podendo ser entre 1 à 1500, e então, guarda essa informação;
# logo após, começa a busca, ordena, vê qual o pior caso, melhor caso e etc...
#===========================================================================================

#  Coleta de tempos de execução
def coletar_metricas(vetor, alvos, repeticoes):
    # Lista que vai acumular o resultado de cada cenário de teste
    resultados = []
 
    # Percorre cada cenário: "alvo" é o número buscado, "descricao" é o nome do caso
    for alvo, descricao in alvos:
        tempos = []  
 
        # Repete a busca várias vezes para obter uma média de tempo confiável,
        for _ in range(repeticoes):
            inicio_tempo = time.perf_counter()       
            resultado = buscaBinaria(vetor, alvo)    
            fim_tempo = time.perf_counter()          
            tempos.append(fim_tempo - inicio_tempo)  
 
        # Calcula as métricas a partir de todas as execuções coletadas
        tempo_total  = sum(tempos)               
        tempo_medio  = tempo_total / repeticoes  
        tempo_min    = min(tempos)               
        tempo_max    = max(tempos)               
 
        # Armazena todas as informações do cenário em um dicionário
        resultados.append({
            "descricao"   : descricao,        # Nome do cenário (ex: "melhor caso")
            "alvo"        : alvo,           
            "resultado"   : resultado,      
            "encontrado"  : resultado != -1,
            "tempo_medio" : tempo_medio,
            "tempo_min"   : tempo_min,
            "tempo_max"   : tempo_max,
            "repeticoes"  : repeticoes,
        })
 
    return resultados
 
#  Exibição da tabela de resultados no console
def exibir_tabela(resultados):
    # Linha separadora usada entre cabeçalho e dados
    sep = "-" * 92
 
    # Cabeçalho da tabela
    print("\n" + "=" * 92)
    print(" BUSCA BINÁRIA — TABELA DE TEMPOS DE EXECUÇÃO")
    print("=" * 92)
    print(f" {'Cenário':<26} {'Alvo':>6}  {'Encontrado':^10}  "
          f"{'T. Médio (µs)':>14}  {'T. Mín (µs)':>12}  {'T. Máx (µs)':>12}  {'Repetições':>10}")
    print(sep)
 
    # Imprime uma linha por cenário testado
    for r in resultados:
        encontrado_str = "Sim" if r["encontrado"] else "Não"
        print(
            f" {r['descricao']:<26} {r['alvo']:>6}  {encontrado_str:^10}  "
            # Multiplica por 1e6 para converter segundos -> microssegundos 
            # O .4f exibe 4 casas decimais
            f"{r['tempo_medio']*1e6:>14.4f}  "
            f"{r['tempo_min']*1e6:>12.4f}  "
            f"{r['tempo_max']*1e6:>12.4f}  "
            f"{r['repeticoes']:>10}"
        )
 
    print("=" * 92)
    print(f" Tamanho do vetor: {len(v2)} elementos   |   Tempos em microssegundos \n")
 
 
#  Execução principal
# Ponto de entrada do programa — garante que o código só roda
# quando o arquivo é executado diretamente, não quando importado
if __name__ == "__main__":
    print("\nIniciando testes de busca binária...")
    resultados = coletar_metricas(v2, ALVOS, REPETICOES)
    exibir_tabela(resultados)