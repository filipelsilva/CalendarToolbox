# cal.py -> Programa para calcular o dia da semana dum calendario
# Autor: Filipe Ligeiro Silva

import sys

# Valores do primeiro dia de cada mes e dos dias da semana
primeiro_mes = "ADDGBEGCFADF"
dias = ["domingo", "segunda", "terca", "quarta", "quinta", "sexta", "sabado"]

# Passa uma letra maiuscula para numero de 1 a 7
def letra_para_num(letra):
    return ord(letra) - ord('A') + 1

# Passa um numero de 1 a 7 para dia da semana
def num_para_dia(num):
    print(dias[num - 1])

# Escreve um dia formatado
def print_dia(dia, mes, ano):
    print("Dia {}/{}/{}".format(dia, mes, ano))

# Verifica se e bissexto
def eh_bissexto(ano):
    if ((ano % 400 == 0) or ((ano % 100 != 0) and (ano % 4 == 0))):
        return True
    else:
        return False

# Calcula o dia da semana
def calcula_dia_semana(escolha, dia, mes, ano):
    # Escrita do dia original
    print_dia(dia, mes, ano)
    # Calculo dos valores que serao diferentes
    if (escolha == 'g'): # Calendario gregoriano
        regressoes = (ano - 1) + (ano // 4) - (ano // 100) + (ano // 400)
        n = 7 - regressoes % 7
    elif (escolha == 'j'): # Calendario juliano
        regressoes = (ano - 1) + (ano // 4)
        n = 2 - regressoes % 7
    # Restante calculo, comum a ambos os calendarios
    r = letra_para_num(primeiro_mes[mes - 1]) + dia
    c = 1 + (r - 2) % 7
    if (eh_bissexto(ano) and mes in (1, 2)):
        w = 1 + (c - n + 6) % 7
    else:
        w = 1 + (c - n + 7) % 7
    # Apresentacao do resultado
    num_para_dia(w)

# MAIN FUNCTION
if __name__ == "__main__":
    c = sys.argv[1]
    d = int(sys.argv[2])
    m = int(sys.argv[3])
    a = int(sys.argv[4])
    calcula_dia_semana(c, d, m, a)