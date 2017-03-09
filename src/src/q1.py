'''
Created on 9 de mar de 2017

@author: maxwell ponte
'''
from math import log

number = int(input("tamanho da mensagem?"))

bits = int(log(number, 2) + 1)

print("quantidade de bits = {0} ".format(bits))