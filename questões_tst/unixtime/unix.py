# coding: utf -8
# PROG1 - UFCG
# ALUNO: EMANUEL VINICIUS | DATA: 14/12/2021
# EXERCICIO: CALCULAR A QUANTIDADE DE DIAS EM UNIX

#|ENTRADA| ENTRADA DE SEGUNDOS COMO INTEIROS
segundos = int(input())

#|CALCULO| TRANSFORMA OS SEGUNDOS EM DIAS |1 DIA EM UNIX —> 86400|
dias = segundos // 86400

#|SAIDA| EM DIAS
print(f"{dias}")
