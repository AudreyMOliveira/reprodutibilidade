# Analysis of the validation error of artificial neural networks applied to cardiac diseases.

<b>Estrutura Pastas GITHUB</b>
- data: entrada de dados 
- deliver: última versão do projeto  e o paper gerado
- figures: imagens geradas no teste
- dev: arquivos antigos

<b>DOWNLOADS REQUERIDOS:</b>

- Jupyter Notebook (Compatível com Python 2.7): http://jupyter.org/install.html

<b>ESTRUTURA DE CLASSES:</b>
- DadosHeart -> lê o arquivo e separa as classes para treino e validação
- Heart.txt  -> dados usados no problema.
- Perceptron -> Onde é implementado a rede neural e é plotado o gráfico
- Problema2  -> Onde é realizado a validação e apresentado a % de erros 

<b>TUTORIAL:</b>
  - Fazer a instalação padrão do python 2.7 xy
  - Instalar o Anaconda
  - Fazer download do projeto
  - Executar o Paper:

<b>PARÂMETROS QUE PODEM SER ALTERADOS NO PROBLEMA:</b>

1- No perceptron.py pode ser alterado os seguintes parâmetros (alterar valores):

     self.num_epocas = xxxx
     self.tx_apr = xxxx
     self.Tolerancia = xxxx

<b>DISTRIBUIÇÃO:</b>

- Maquina Virtual(MEGA): https://mega.nz/#!JiBglbLK!PwnG6AuEoYIVvqaIVErKKSu3KFKHIuz2IDURm1r5bBs
- Repositório Docker: https://hub.docker.com/r/audoliveira/reprodutibilidade/
