# cal.py -> Programa para calcular o dia da semana dum calendario
# Autor: Filipe Ligeiro Silva

import sys

primeiro_mes = "ADDGBEGCFADF"
dias = ["domingo", "segunda", "terca", "quarta", "quinta", "sexta", "sabado"]

def letra_para_num(letra):
    return ord(letra) - ord('A') + 1

def translate(num):
    print(dias[num - 1])

def calcula_gregoriano(dia, mes, ano):
    return 0

def calcula_juliano(dia, mes, ano):
    n = 7 - ((ano + 4) + (ano // 4)) % 7
    r = letra_para_num(primeiro_mes[mes - 1]) + dia
    c = 1 + (r - 2) % 7
    w = 1 + (c - n + 7) % 7
    translate(w)

if __name__ == "__main__":
    c = sys.argv[1]
    d = int(sys.argv[2])
    m = int(sys.argv[3])
    a = int(sys.argv[4])
    print("Dia {}/{}/{}".format(d, m, a))
    if (c == "g"):
        calcula_gregoriano(d, m, a)
    elif (c == "j"):
        calcula_juliano(d, m, a)