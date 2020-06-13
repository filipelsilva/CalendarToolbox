# cal.py -> Programa para calcular o dia da semana dum calendario
# Autor: Filipe Ligeiro Silva

import sys

primeiro_mes = "ADDGBEGCFADF"
dias = ["domingo", "segunda", "terca", "quarta", "quinta", "sexta", "sabado"]

def letra_para_num(letra):
    return ord(letra) - ord('A') + 1

def translate(num):
    print(dias[num - 1])

def print_dia(dia, mes, ano):
    print("Dia {}/{}/{}".format(dia, mes, ano))

def eh_bissexto(ano):
    if (ano == 2000):
        return True

def calcula_gregoriano(dia, mes, ano):
    return 0

def calcula_juliano(dia, mes, ano):
    print_dia(dia, mes, ano)
    regressoes = (ano - 1) + (ano // 4)
    n = 2 - regressoes % 7
    r = letra_para_num(primeiro_mes[mes - 1]) + dia
    c = 1 + (r - 2) % 7
    if (eh_bissexto(ano) and mes not in (1, 2)):
        w = 1 + (c - n + 6) % 7
    else:
        w = 1 + (c - n + 7) % 7
    translate(w)

if __name__ == "__main__":
    c = sys.argv[1]
    d = int(sys.argv[2])
    m = int(sys.argv[3])
    a = int(sys.argv[4])
    if (c == "g"):
        calcula_gregoriano(d, m, a)
    elif (c == "j"):
        calcula_juliano(d, m, a)