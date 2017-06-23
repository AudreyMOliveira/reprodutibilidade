# Analysis of the validation error of artificial neural networks applied to cardiac diseases.

<b>Estrutura Pastas GITHUB</b>
- data: entrada de dados 
- deliver: versões antigas do projeto
- figures: imagens geradas no teste
- dev: contem a pasta (perceptron - código fonte) e o paper gerado

<b>DOWNLOADS REQUERIDOS:</b>
- Python 2.7 xy (http://python-xy.github.io/downloads.html)
- Arquivos do projeto contidos na pasta perceptron (https://github.com/AudreyMOliveira/reprodutibilidade/tree/master/dev/perceptron)

<b>ESTRUTURA DE ARQUIVOS PASTA DEV:</b>
- DadosHeart.py -> lê o arquivo e separa as classes para treino e validação
- Heart.txt -> dados usados no problema.
- Perceptron.py -> Onde é implementado a rede neural e é plotado o gráfico
- Problema2.py -> Onde é realizado a validação e apresentado a % de erros 

<b>TUTORIAL:</b>
1- Fazer a instalação padrão do python 2.7 xy

2- Abrir o python com as seguintes configurações:
	2.1 - Options: none(IDE)
	2.2 - Applications: IPython QT Console
	2.3 - Interective Consoles: IPython (sh)

3- Clicar em run spyder

4- Ir em file -> newProject 
selecionar os arquivos baixados da pasta PERCEPTRON(1º Passo)

5- Clicar sobre o dadosHeart.py e clicar no ícone de executar.
   
(verifique que na pasta do projeto, foi inserido o as matrizes, os erros    épocas e  foi gerado o gráfico de validação de erros.)

6- No console do python verificar o percentual de validação


<b>PARÂMETROS QUE PODEM SER ALTERADOS NO PROBLEMA:</b>

1- No perceptron.py pode ser alterado os seguintes parâmetros (alterar valores):

     self.num_epocas = xxxx
     self.tx_apr = xxxx
     self.Tolerancia = xxxx
