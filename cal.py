# cal.py -> Programa para calcular o dia da semana dum calendario
# Autor: Filipe Ligeiro Silva

import sys
from datetime import datetime, timedelta

# Valores do primeiro dia de cada mes e dos dias da semana
primeiro_mes = "ADDGBEGCFADF"
dias = ["Domingo", "Segunda", "Terca", "Quarta", "Quinta", "Sexta", "Sabado"]

# Passa uma letra maiuscula para numero de 1 a 7
def letra_para_num(letra):
    return ord(letra) - ord("A") + 1

# Passa um numero de 1 a 7 para dia da semana
def num_para_dia(num):
    print(dias[num - 1])

# Escreve um dia formatado
def print_dia(dia, mes, ano):
    print("Dia {}/{}/{}".format(dia, mes, ano))

# Verifica se e bissexto
def eh_bissexto(ano):
    return ((ano % 400 == 0) or ((ano % 100 != 0) and (ano % 4 == 0)))

# Calcula o dia da semana
def calcula_dia_semana(escolha, dia, mes, ano):
    # Escrita do dia original
    print_dia(dia, mes, ano)

    # Calculo dos valores que serao diferentes
    if (escolha == "g"): # Calendario gregoriano
        regressoes = (ano - 1) + (ano//4) - (ano//100) + (ano//400)
        n = 7 - regressoes % 7

    elif (escolha == "j"): # Calendario juliano
        regressoes = (ano - 1) + (ano//4)
        n = 2 - regressoes % 7

    # Restante calculo, comum a ambos os calendarios
    r = letra_para_num(primeiro_mes[mes - 1]) + dia
    c = 1 + (r - 2) % 7

    if (eh_bissexto(ano) and mes in (1, 2)):
        w = 1 + (c - n + 6) % 7

    else:
        w = 1 + (c - n + 7) % 7

    # Apresentacao do resultado
    print("Calculos auxiliares:\n\tRegressoes = {}\n\tn = {}\n\tr = {}\
        \n\tc = {}\n\tw = {}".format(regressoes, n, r, c, w))
    num_para_dia(w)

# Calcula o dia de pascoa de um ano
def calcula_dia_pascoa(escolha, ano):
    # Print do ano
    print("Pascoa do ano {}".format(ano))

    g = 1 + ano % 19 # Numero de ouro

    # Calculo dos valores que serao diferentes
    if (escolha == "g"): # Calendario gregoriano
        regressoes = (ano - 1) + (ano//4) - (ano//100) + (ano//400)
        e0 = (57 + (11 * g) - (ano//100) + ((ano//100)//4) +
             (((ano//100) - (((ano//100) - 17)//25))//3)) % 30
        v = (e0/24 - e0/25) + (g/12) * (e0/25 - e0/26)
        e = e0 + v # Epacta

    elif (escolha == "j"): # Calendario juliano
        regressoes = (ano + 4) + (ano//4)
        e0 = "nao importante"
        v = "nao importante"
        e = (11 * g - 3) % 30 # Epacta

    # Restante calculo, comum a ambos os calendarios
    d = 20 + (54 - e) % 30
    c = 1 + (d + 2) % 7
    n = 7 - regressoes % 7

    if (c < n):
        s = d + n - c % 7

    else:
        s = d + 7 - (c - n) % 7

    dia = datetime(ano, 3, 1)
    res = dia + timedelta(s - 1)

    # Apresentacao do resultado
    print("Calculos auxiliares:\n\tg = {}\n\tRegressoes = {}\n\te0 = {}\
        \n\tv = {}\n\te = {}\n\td = {}\n\tc = {}\n\tn = {}\n\ts = {}"
        .format(g, regressoes, e0, v, e, d, c, n, s))
    print_dia(res.day, res.month, res.year)

# MAIN FUNCTION
if __name__ == "__main__":
    c = sys.argv[1]

    if (c == "d"):
        cal = sys.argv[2]
        d = int(sys.argv[3])
        m = int(sys.argv[4])
        a = int(sys.argv[5])
        calcula_dia_semana(cal, d, m, a)
        
    elif (c == "p"):
        cal = sys.argv[2]
        a = int(sys.argv[3])
        calcula_dia_pascoa(cal, a)
