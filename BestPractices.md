# BEST PRACTICES IA369Z - Computational Reproducibility Research

A multidisciplinaridade e a complexidade das pesquisas de modo geral vem fazendo com que seja cada dia mais difícil reproduzir o trabalho de outras equipes. Diante deste cenário, a comunidade científica vem buscando alternativas e boas práticas na execução das pesquisas para simplificar futuras reproduções. surgiu, assim, o termo reprodutibilidade em pesquisa científica. 
Considera-se reprodutível, a pesquisa que, quando executada pela comunidade obtém-se resultados coerentes em relação a execução anterior. Portanto, é desejável que se disponibilize todos o pacote e todas as dependências desde o dado até o ambiente de execução. Abaixo segue alguns tópicos que foram tomados como boas práticas para desenvolvimento de um paper executável:

## 1- LITERATE COMPUTER - JUPYTER NOTEBOOK

Todos os códigos do trabalho foram armazenados em no notebook. o Jupyter é uma ferramenta interativa, de fácil instalação, bem documentada, e muito poderosa para a organização do código e paper. Porém, ao tentar importar o paper feito no overleaf, o conteúdo veio desformatado. 

<green>DICAS:</green>
- Mantenha o diretório organizado.
- Dê nomes objetivos aos notebooks e aproveite para inserir algum versionamento.
- Se o código é orientado a objetos, as classes podem ficar em notebooks separados, mas é necessário fazer uma pesquisa mais detalhada sobre o assunto pois até hoje não encontrei uma forma simples de importar classes em outro notebook.
- É uma excelente opção para trabalhar com gráficos (matplotlib) e com o matrizes. Tanto a biblioteca matplotlib quanto a numpy funcionaram perfeitamente. 



    
