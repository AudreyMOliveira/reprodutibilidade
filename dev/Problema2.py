# -*- coding: utf-8 -*-

import DadosHeart as dh
from perceptron import perceptron as cp
import numpy as np


# Importa da DadosHeart 
VTreino, VValida = dh.DadosHeart()

# Carrega a matriz de treino para o objeto perceptron
Perceptron = cp(VTreino)

# Função de treino
Perceptron.treino()

# Validaçao do perceptron
N = VValida.shape[-1] 

#Separação das entradas X das Saidas Y
XV = VValida[0:13,:]   
YV = VValida[13,:]   
  
# Add entrada nas bias
X_Bias = -1*np.ones((1,N))
XV = np.vstack((X_Bias,XV))

erro_valida = 0

# Inicializaçao das variaveis de resposta do perceptron (y_perceptron) 
y_perceptron = []
#resposta real (y_real) dos pacientes
y_resposta = []
#contador dos erros de validaçao
erro_valida = 0

# Verifica saidas da validação

for i in range(N):
    y_perceptron = Perceptron.saida(XV[:,i])
    y_real = YV[0,i]
    erro_valida += (1 if (int(y_perceptron) != int(y_real)) else 0)
    
    
# Calculo do % de erro
perc_erro = (erro_valida * 100)/N

print(" Erros Validacao: %d" %erro_valida)
print(" Erros Validação %2.2f:" %perc_erro)

#print(" Erros Validação (%): %2.2f" %perc_erro)
