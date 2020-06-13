
# Autor: Filipe Ligeiro Silva

Python script para calcular o dia da semana de uma data específica
ou o dia de Páscoa de um ano, tanto no calendário Gregoriano como no Juliano.


## Utilização:
```bash
$ python3 cal.py [flag1] [flag2] [flag3] [flag4] [flag5]
```

#### flag1: 'd' (dia da semana) ou 'p' (Páscoa)
* ##### [flag1] = 'd'
    * flag3, 4 e 5 -> dia, mês, ano
    * Ex: ```python3 cal.py d g 25 12 2020```

* ##### [flag1] = 'p'
    * flag3 -> ano
    * Ex: ```python3 cal.py p g 2020```

#### flag2: 'g' (calendário Gregoriano) ou 'j' (calendário Juliano)

###### "I solemnly swear that i am up to no good"