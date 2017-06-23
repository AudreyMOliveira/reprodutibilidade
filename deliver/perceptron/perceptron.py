# -*- coding: utf-8 -*-


import numpy as np
import matplotlib.pyplot as plt

class perceptron:
    def __init__(self,M,narq_w = 'Pesos.txt',narq_e = 'ErrosEpocas.txt'):
        
        self.num_epocas =1000
        self.tx_apr = 0.05
        self.Tolerancia = 0.00
        
        #Função que verifica se o perceptron aprende ou não (o treino já foi executado)
        # True = 1
        # False = 0      
        self.aprende = False        
        self.N = M.shape[-1]
        self.vet_Erros = []
        self.variavelPlot= []
        
        self.narq_w = narq_w
        self.narq_e = narq_e
                
        # Inicializando vetor de pesos 
        # Media = '0'
        # Desvio Padrão = '1'
        self.W = np.matrix(np.random.randn(1,M.shape[-2]))
        self.W = np.matrix(self.W)
        
       
        # A matriz de entrada é sepadarada do vetor de saida
        self.X =  M[:(M.shape[-2]-1),:]
        
        # Entrada Bias
        X_Bias = -1*np.ones((1,self.N))
        self.X = np.vstack((X_Bias,self.X))
        
        # Saidas
        if (self.aprende == False):
            self.Yd = M[(M.shape[-2]-1),:]
        
        np.savetxt('matriz X',self.X, fmt='%10.4f')
        np.savetxt('matriz Y',self.Yd, fmt='%10.4f')
    
    # Funçao de execuçao do perceptron. 
         
    def saida(self,vx): 

        vx = np.matrix(vx)
        
        # Calcula a saida do neuronio 
        y =  ((self.W*vx) >= 0)
        return 1 if y[0,0] else 0 
        
      
        
    def treino(self):
        
        # Matriz que armazena pesos por época       
        Matriz_w = np.matrix(self.W) 
                       
        while not self.aprende:
        
            
            Idx = np.random.permutation(self.N)
            
            Erroq = 0
            
                  
            for i in range(self.N):
                
                # Chama função saida
                y = self.saida(self.X[:,Idx[i]])
                
                # Erro = saida do perceptron - saida já conhecida 
                Erro = self.Yd[:,Idx[i]] - y
           
                # Calculo vet Delta_W
                Delta_W = self.tx_apr*Erro[0,0]*np.transpose(self.X[:,Idx[i]])
                
                # Atualiza vetor de pesos
                self.W = self.W + Delta_W
                
                # Atualiza o erro quadratico da num_epocas
                Erroq = Erroq + Erro**2

            # Acumula os valores de peso e erro quadratico por num_epocas            
            Matriz_w = np.vstack((Matriz_w,self.W))
            self.vet_Erros.append(Erroq[0,0])
            
            
            self.num_epocas -= 1
            
               
            # Executa o treino ate que o Erro quadratico seja 0
            # ou num_epocas = 
            
            if  (Erroq <= self.Tolerancia) or (self.num_epocas == 0):
                self.aprende = True
        
        #chama funcao para gerar graficos de separacao das classes 
        # e grafico de erro
        self.grafico()
        
        #Gera arquivos com os valores de pesos e erros quadraticos por num_epocas
        np.savetxt(self.narq_w,Matriz_w, fmt='%10.4f')
        np.savetxt(self.narq_e,self.vet_Erros, fmt='%d')      
        self.variavelPlot = (self.vet_Erros/10) 
        
        #Print vetor de pesos         
        print(' Saidas:')
        print(' ')
        
        for i in range(self.W.shape[-1]):
            print(' Valor do peso %d foi: %10.4f' %(i,self.W[0,i]))
        
          
        return self.aprende
    
    def grafico(self):
        
       
        # Se os dados de treino tiverem apenas duas entradas 
        # sera gerado o gráfico do perceptron
        if self.X.shape[-2] <= 3:
            for i in range(self.N):
                if self.Yd[0,i] == 0:
                    plt.plot(self.X[1,i],self.X[2,i],'bo')
                else:
                    plt.plot(self.X[1,i],self.X[2,i],'ro')
        
            X1Aux = np.matrix(np.linspace(int(self.X[1:,:].min())-1,int(self.X[1:,:].max())+1,100))        
        
            plt.axis([int(self.X[1:,:].min())-1, int(self.X[1:,:].max())+1, int(self.X[1:,:].min())-1, int(self.X[1:,:].max())+1])
        
            Rtx_apr = -(self.W[0,1]/self.W[0,2])*X1Aux + self.W[0,0]/self.W[0,2]
            plt.plot(X1Aux,Rtx_apr,'r-^')
            plt.title('Grafico de Separacao das Classes')
            plt.grid('on')
            plt.show()
            
            
        #Gera grafico de erros por num_epocas de treino  
        
        plt.figure()
        plt.plot(np.arange(len(self.variavelPlot)), self.variavelPlot, 'bo')
        plt.grid('on')
        plt.title('Graph of Quadratic Errors x Season')        
        plt.show()
