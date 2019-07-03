import numpy
import numpy as np, scipy.stats as st
import math

def desvioPadrao(d):
    soma = 0
    media = numpy.mean(d)
    for xi in d:
        soma = soma + math.pow(xi - media,2)
    return math.sqrt(soma/(len(d)-1))

def desvioPadraoDiferencas(sa,na,sb,nb):

    return math.sqrt((math.pow(sa,2)/na) + (math.pow(sb,2)/nb))

def grausEfetivosLiberdade(sa,na,sb,nb):

    numerador = math.pow((math.pow(sa,2)/na) + (math.pow(sb,2)/nb),2)
    den1  = (1/(na-1))* math.pow((math.pow(sa,2)/na),2)
    den2  = (1/(nb-1))* math.pow((math.pow(sb,2)/nb),2)

    return numerador/(den1 + den2) - 2

alg1 = [3221, 3452, 3359, 3487, 3262]
alg2 = [3322, 3365, 3341, 3389, 3314]
t90 = 2.353
t50 = 0.765

print('Media\n\t',numpy.mean(alg1),numpy.mean(alg2))
print('Desvio Padrao\n\t',desvioPadrao(alg1),desvioPadrao(alg2))
DifMedia = numpy.mean(alg1)- numpy.mean(alg2)
print('Diferenca Medias\n\t',DifMedia)
print('Desvio Padrao Diferencas\n\t',desvioPadraoDiferencas(desvioPadrao(alg1),len(alg1),desvioPadrao(alg2),len(alg2)))
print('Graus Efetivos Liberdade\n\t',grausEfetivosLiberdade(desvioPadrao(alg1),len(alg1),desvioPadrao(alg2),len(alg2)))

print('\n*** Para IC de 90% ***\n')
print('Valor de t utilizado\n\t',t90)
TxS90 = (desvioPadraoDiferencas(desvioPadrao(alg1),len(alg1),desvioPadrao(alg2),len(alg2)))*t90
print('t x s\n\t',TxS90)
print('IC 90%(',DifMedia - TxS90,';',DifMedia + TxS90,')\n')

print('*** Para IC de 50% ***\n')
print('Valor de t utilizado\n\t',t50)
TxS50 = (desvioPadraoDiferencas(desvioPadrao(alg1),len(alg1),desvioPadrao(alg2),len(alg2)))*t50
print('t x s\n\t',TxS50)
print('IC 50%(',DifMedia - TxS50,';',DifMedia + TxS50,')\n')



