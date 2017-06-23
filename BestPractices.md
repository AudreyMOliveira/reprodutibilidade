# BEST PRACTICES IA369Z - Computational Reproducibility Research

A multidisciplinaridade e a complexidade das pesquisas de modo geral vem fazendo com que seja cada dia mais difícil reproduzir o trabalho de outras equipes. Diante deste cenário, a comunidade científica vem buscando alternativas e boas práticas na execução das pesquisas para simplificar futuras reproduções. surgiu, assim, o termo reprodutibilidade em pesquisa científica. 
Considera-se reprodutível, a pesquisa que, quando executada pela comunidade obtém-se resultados coerentes em relação a execução anterior. Portanto, é desejável que se disponibilize todos o pacote e todas as dependências desde o dado até o ambiente de execução. Abaixo segue alguns tópicos que foram tomados como boas práticas para desenvolvimento de um paper executável:

### 1- LITERATE COMPUTER - JUPYTER NOTEBOOK

Todos os códigos do trabalho foram armazenados em no notebook. o Jupyter é uma ferramenta interativa, de fácil instalação, bem documentada, e muito poderosa para a organização do código e paper. Porém, ao tentar importar o paper feito no [OverLeaf](https://www.overleaf.com/), o conteúdo veio desformatado. 

<b>DICAS:</b>
- Mantenha o diretório organizado.
- Dê nomes objetivos aos notebooks e aproveite para inserir algum versionamento.
- Se o código é orientado a objetos, as classes podem ficar em notebooks separados, mas é necessário fazer uma pesquisa mais detalhada sobre o assunto pois até hoje não encontrei uma forma simples de importar classes em outro notebook.
- É uma excelente opção para trabalhar com gráficos (Matplotlib) e com o matrizes. Tanto a biblioteca matplotlib quanto a numpy funcionaram perfeitamente. 

<b>LINKS</b>
- Documentação: http://jupyter-notebook.readthedocs.io/en/latest/
- Download: http://jupyter.org/install.html

### 2- REPOSITÓRIO E VERSIONAMENTO - GIT/GITHUB
 
O repositório e o versionamento do código garantem a organização da pesquisa, é muito util quando se trabalha em equipe. O versionamento é fundamental para o controle de alterações e para caracterizar aplicação. 
O github é um repositório público com suporte para mac, unix e windows. Apesar de não muito conhecido, tem sua versão desktop e funciona muito bem, sua interface apresenta informações sobre os últimos arquivos alterados e onde foi realizada a alteração. Seu repositório online simples, rápido, e democrático pois apresenta quase todos os códigos sem a necessidade de fazer download. 
 
<b>DICAS:</b>
- A antes de cada commit faça uma update do código, principalmente se for compartilhado com outras pessoas. Isto evita que você comit sobre um código antigo. 
- Opte por pequenos commites para manter um controle melhor do código. 
- A cada atualização significativa do código, detalhe no commit o que foi alterado, uma breve descrição poderá ser útil no futuro. 
- Dentro das pastas criadas, aproveite o read.me para explicar o que está contido ali. 
 
<b>LINKS:</b>
- Site oficial: https://github.com
- GitHub Desktop download: https://desktop.github.com/

### 3- WORKFLOW - DRAW.IO
 
O workflow é fundamental na visualização do projeto de uma maneira ampla e objetiva. No caso da pesquisa reprodutiva, pode exercer duas funções: 
 
- Apresentar o fluxo do projeto a fim de enfatizar os conceitos e o fluxo da informação.
- Apresentar a arquitetura do projeto, ilustrando quais são os passos necessários para se executar a pesquisa. 
 
O DRAW.io é uma ferramenta online que pode ser vinculada ao google chrome.A principal vantagem que ele apresenta é a permanência do arquivo na nuvem, podendo ser gerado e alterado facilmente sem a necessidade de se atualizar o repositório.
 
<b>DICAS:</b>
- Comece pelo workflow! Analisar visualmente a pesquisa, lhe trará um olhar crítico sobre as ferramentas que podem ser ajudas na reprodutibilidade.
- Existem ferramentas para o desenho do workflow e existem ferramentas para o gerenciamento do workflow, cabe a você verificar a viabilidade do uso destas. Vale salientar, que algumas ferramentas pesquisadas, como a Loni Pipeline e a Pegasus são específicas para algumas áreas e possuem usabilidades comprometidas. 
 
<b>LINKS:</b>
- Site Oficial: https://www.draw.io

### 4 - DISTRIBUIÇÃO/ AMBIENTE - DOCKER, VIRTUAL BOX.
 
Para garantir a reprodução do código nas mesmas condições ou seja, no mesmo ambiente, máquinas virtuais podem ser configuradas, ou até mesmo uma imagem do docker. Estas ferramentas evitam que fatores externos possam afetar no resultado da execução. Utilizando a Virtual box, é possível configurar facilmente um sistema operacional, seja ele unix, ou windows. As configurações da máquina também podem ser ajustadas na ferramenta. 
O docker possuí mesma finalidade da virtual box para reprodutibilidade, entretanto os repositórios de imagens pré configurado facilitam a instalação e configuração. 
 
 
<b>DICAS:</b>
 
- Esteja atenta ao tamanho da máquina virtual exportada.
- Verifique se já não existe uma imagem no docker hub que atenda as necessidades do projeto.
 
<b>LINKS:</b>
- Site Oficial Docker: https://www.docker.com/
- Site Oficial Virtual Box: https://www.virtualbox.org/
- Docker Tools: https://download.docker.com/win/stable/DockerToolbox.exe
- Tutorial criação de novo container no docker:  https://www.dataquest.io/blog/docker-data-science/
 







    
