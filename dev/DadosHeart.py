# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------------
# Funcao DadosHeart baseada na funcao DadosHeart.m escrita por Renato Dourado Maia em Matlab
#-----------------------------------------------------------------------------
import numpy as np

def DadosHeart():

    #-----------------------------------------------------------------------------
    # Carrega arquivo com dados de pacientes reais para matriz V_heart
    V_heart = np.empty([0,14])    

    with open('heart.txt') as arq_heart:
        for linhas in arq_heart.readlines():       
            V_heart = np.vstack((V_heart,linhas.rstrip().split(' ')))
    
    V_heart = V_heart.astype(np.float)
    
    #-----------------------------------------------------------------------------
    # Organizando dados em conjunto de treinamento 

    # Número de padrões para treinamento: serão separados 100 pacientes doentes e 
    # 100 saudáveis no conjunto de treinamento, ficando o restante no conjunto de 
    # validaçao
    
    PadroesTrei = 100

    # Ordena o vetor de dados pela coluna 14 (doentes/saudáveis)
    # Alterei o programa original para retornar a matriz no modelo de entrada 
    # do perceptron com vetor X1...X13 na vertical e o ultimo elemento deste vetor é o Y.
    # No programa original foi utilizad uma funcao sorte que aqui foi substituda 
    # por um for que separa doentes e saudaveis em dois vetores V_um e V_dois 
    
    V_um = np.empty([0,14])
    
    V_dois = np.empty([0,14])

    for i in range(270):
        if V_heart[i,13] == 1:
            V_heart[i,13] =  V_heart[i,13] -1           
            V_um = np.vstack((V_um,V_heart[i,:]))
        else:
            V_heart[i,13] =  V_heart[i,13] -1            
            V_dois = np.vstack((V_dois,V_heart[i,:])) 
    
    
    # Criaçao de vetores com valores aleatorios para sorteio dos dados de treinamento 
   
    h1 = np.random.permutation(150)  
    h2 = np.random.permutation(120)
   
    # Dados para treinamento
    # Escolha aleatória de 100 pacientes saudáveis e 100 pacientes doentes para treinamento
    MTreino = np.hstack((np.transpose(V_um[h1[0:PadroesTrei],:]), np.transpose( V_dois[h2[0:PadroesTrei], :])))
    MTreino = np.matrix(MTreino)
    
    # O restante dos dados não utilizados no treinamento serão utilizados para validação
    MValidacao = np.hstack((np.transpose(V_um[h1[PadroesTrei:],:]), np.transpose( V_dois[h2[PadroesTrei:], :])))
    MValidacao = np.matrix(MValidacao)    
    
    return MTreino, MValidacao
    
    #--------------------------------------------------------------------    
    # Abaixo eu mantive o codigo original reescrito em python    
    
    #hordenado = np.vstack((V_um,V_dois)) 
    
    #x1_treinamento = hordenado[h1[0:PadroesTrei],:]
    #x1_treinamento = np.matrix(x1_treinamento)

    # Escolha aleatória de 100 pacientes doentes para treinamento
    #h2 = np.random.permutation(120)
    #x2_treinamento   = hordenado[150 + h2[0:PadroesTrei], :]  
    #x2_treinamento = np.matrix(x2_treinamento)

    # Montando matrizes de dados de maneira adequada:
    # padrões por coluna na matriz de entrada e saidas
    # por linha na matriz de saídas
    #XTreino  = np.hstack((np.transpose(x1_treinamento[:,0:13]), np.transpose( x2_treinamento[:,0:13])))		
    # Subtrai-se um para que se tenha classes 0 e 1, ao invés de 1 e 2
    #YTreino  = np.hstack((np.transpose(x1_treinamento[:,13]), np.transpose(x2_treinamento[:,13])))
    #YTreino  = YTreino -1
        
    #-----------------------------------------------------------------------------

    #-----------------------------------------------------------------------------
    # Organizando dados em conjunto de validação

    # Seleciona dados para validação e monta matrizes de dados tal como foi feito 
    # para os dados de treinamento
    #x1_validacao  = hordenado[h1[PadroesTrei + 0:120],:] 	
    #x1_validacao = np.matrix(x1_validacao)
    #x2_validacao  = hordenado[150 + h2[PadroesTrei + 0:120], :] 
    #x2_validacao = np.matrix(x2_validacao)
    
    
    #XValidacao =  np.hstack((np.transpose(x1_validacao[:,0:13]),np.transpose(x2_validacao[:,0:13])))	
    #YValidacao =  np.hstack((np.transpose(x1_validacao[:,13]), np.transpose(x2_validacao[:,13])))
    #YValidacao = YValidacao -1   	
#-----------------------------------------------------------------------------
    #return XTreino,YTreino, XValidacao, YValidacao