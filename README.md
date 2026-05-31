# 🧠 Formação em Machine Learning e Ciência de Dados - SCTI.SC
## Mini-Projeto Avaliativo - Módulo 1 - Semana 07
<br>
Bem-vindo(a) ao repositório do trabalho de sanitização (limpeza e tratamento de dados) referente ao curso de Lógica de Programação e Machine Learning do SCTI/SENAI!
Este espaço foi criado para centralizar os códigos, notebooks e materiais práticos desenvolvidos durante o projeto.<br>
<hr>

## 🟢 1. Título do Projeto e Descrição Geral
Pipeline de Sanitização de Dados (ETL)

Garantir que os dados estejam adequados para serem utilizados em modelos de machine learning. É fundamental que estes dados passem por um rigoroso processo de ETL (Extract, Transform, Load). A equipe de Engenharia de Dados da Olist extraiu lotes de dados do banco oficial em arquivos estruturados (olist_products_dataset.csv e olist_orders_dataset.csv), mas identificou inconsistências que estão travando os relatórios automatizados.

## 🎯 2. Objetivos
   * **Do Repositório:** Fornecer um ambiente de consulta prática para sanitização de arquivos de dados do tipo csv. Aqui você encontrará os *scripts* passo a passo e anotações correlatas.
   * **Dos Scripts:** Sanitizar (limpar) as colunas de dados das bases de produtos e pedidos de compra, utilizando apenas o "Python Raiz" (sem bibliotecas adicionais). Preencher valores nulos com a mediana, criar novas colunas que possibilitem identificar que ocorreram nulos nas colunas base, padronizar formatos de data para o padrão brasileiro, normalizar colunas, gerar novos arquivos de dados sanitizados e por fim elucidar uma questão da diretoria, que supõe que obrigatoriamente, as datas nulas de entrega ao cliente sejam decorrentes de status do tipo cancelado.

## 👁‍🗨 3. Visão Geral dos Dados (Data Overview)
Origem dos Dados (Input): São 2 arquivos csv, um de produtos gerais e outro de pedidos de compra.<br>
   * **Bases de Dados(.csv):** https://github.com/fiesc-junior-prado/mine_projeto_bloco_1 <br>
Também disponíveis neste repositório, os quais são:<br>
* **Produtos:** olist_products_dataset.csv
* **Pedidos:** olist_orders_dataset.csv

Volumetria/Contexto:
* **Produtos:** 32.951 registros dispostos em 9 colunas de dados.
* **Pedidos:** 99.441 registros dispostos em 8 colunas de dados.

## 🔄 4. Regras de Sanitização Aplicadas
No cenário atual do mercado de tecnologia, os dados são o combustível para qualquer sistema inteligente. Empresas líderes em e-commerce lidam diariamente com milhões de transações que alimentam painéis de Business Intelligence e modelos preditivos de Machine Learning. Contudo, dados do mundo real são notoriamente conhecidos por serem "sujos", incompletos ou mal formatados.<br>
Diante desta realidade aplicaram-se os seguintes tratamentos:<br>
* **Tratamento de Valores Nulos**: O nome da categoria de produtos estava nulo em 1,85% dos casos e foi preenchido com 'sem categoria' e para vários campos númericos foram utilizadas as medianas; 
* **Indicador de Omissão (dummy de ausência):** Várias colunas novas foram criadas para identificar os registros nulos. Desta forma, o valor nulo da coluna original foi substituído pela mediana, e a coluna nova criada recebia 0/1 para identificar a ocorrência, ou não, do valor nulo. 
* **Padronização de Formatos:** Conversão de datas, utilização de regexs, conversão para letras minúsculas.
* **Filtros de Outliers/Anomalias:** Alguns registros que apresentavam uma ocorrência muito baixa não foram para as bases sanitizadas. Foram desconsiderados por não apresentarem relevância no cenário global.

## 🛠️ 5. Tecnologias e Ferramentas Utilizadas
* **Linguagem:** Python 3.14.5
* **Ambiente:** Visual Studio Code (VS Code)
* **Controle de Versão:** Git e GitHub
* **Bibliotecas:** Python (apenas bibliotecas nativas)
   * **- re:** padrão para expressões regulares, usada para manipulação de strings
   * **- csv:** padrão para leitura e escrita de arquivos CSV 
   * **- datetime:** padrão para manipulação de datas e horas
   * **- List, Dict, Any, Union:** padrão para dicas de tipo (type hints), usada para melhorar a legibilidade e manutenção do código

## 🧱 6. Estrutura do Projeto
```text
├── pipeline-sanitizacao/
│   ├── dados_brutos/      # Dados antes da sanitização
│   └── dados_limpos/      # Dados limpos (resultado final)
├── minhas_funcoes.py      # Módulo de funções deste projeto
├── README.md              # Leia-me do projeto
└── sanitizacao.ipynb      # Módulo principal de sanitização dos dados
```
## ▶ 7. Passo a Passo (Git Flow)
Por ser um projeto solo as iterações são bem resumidas. Utilizado no desenvolvimento o ambiente do VS Code.<br>
De um modo minimalista, podemos destacar:<br>
-  Estrutura de Branches Resumida<br>
      * main (ou master): É onde o código funciona. Para executar o script de sanitização hoje para entregar um relatório, é essa branch que será executada.
      * feature/nome-da-tarefa: Branches temporárias - implementar uma melhoria específica e deletar logo em seguida.

- Instalação de Dependências: Este projeto utiliza apenas a biblioteca padrão do Python ("Python Raiz"). Nenhuma instalação externa é necessária.

- Passos:
   * De execução:<br>
      A partir do módulo sanitizacao.ipynb, que é um Jupyter Notebook, basta executar tudo numa única rodada. Utilize o comando `"▶ Run All"` para obter os resultados da sanitização das bases de dados, ou execute cada célula sequencialmente do topo (início) ao fim.<br>

      * Para rodar na Nuvem (Google Colab):
         1. Navegue pelas pastas e clique no arquivo com final `.ipynb` (Jupyter Notebook) que você deseja executar.
         2. Na própria tela do GitHub, você verá os códigos. Para executar e editar, clique no botão "Open in Colab" ou abra o arquivo diretamente no [Google Colab](https://colab.research.google.com/).

      * Para rodar Localmente (VS Code):
         1. ## ✅ Abrir o VS Code
            Ir para o ambiente onde deseja baixar (clonar) o projeto:<br>
            No menu principal clique em *"File/Open Folder"* ou utilize as teclas de atalho Ctrl+K Ctrl+O<br>
            No menu clique em *"Terminal\New Terminal"* ou utilize as teclas de atalho Ctrl+Shift+' e digite:<br>
            ```bash
            git clone https://github.com/PauloSBLima/pipeline-sanitizacao.git
            ```
            Entrar na pasta do diretorio do projeto (pipeline-sanitizacao)<br>
            ```bash
            cd pipeline-sanitizacao
            ```
         2. ## 🔱 Criar uma branch para sua atividade
            Antes de começar, atualizar a branch principal:<br>
            ```bash
            git checkout main
            git pull origin main
            ```
            Criar uma nova branch com um nome descritivo:<br>
            ```bash
            git checkout -b atividade/seu_nome-descricao
            ```
            Exemplo:<br>
            ```bash
            git checkout -b atividade/seu_nome-nova_funcionalidade
            ```
         3. ## 💾 Salvar suas alterações
            Verificar os arquivos modificados:
            ```bash
            git status
            ```
            Adicionar os arquivos alterados:
            ```bash
            git add .
            ```
            Criar um commit com uma mensagem clara:
            ```bash
            git commit -m "feat: mensagem clara"
            ```
            Enviar sua branch para o GitHub:
            ```bash
            git push -u origin atividade/seu_nome-descricao
            ```
         4. ## 🔁 Abrir um Pull Request
            Depois de enviar sua branch:
            1. Acesse o repositório no GitHub.
            2. Clique em **Compare & pull request**.
            3. Confira se a comparação está correta:
               - Base: `main`
               - Compare: sua branch
            4. Escreva um título claro para o Pull Request.
            5. Explique o que foi alterado.
            6. Clique em **Create pull request**.

            Exemplo de descrição:

            ```text
            ## O que foi feito

            - Incluí uma nova coluna booleana para análise.
            - Executei novamente o notebook.
            - Comparei a nova acurácia com o resultado anterior.

            ## Resultado observado

            A acurácia do modelo ficou em aproximadamente XX%.

## 💭 8. Reflexão teórica sobre Machine Learning
A sanitização (limpeza) dos dados que servirão para treinamento de um algoritmo de ML é vital.
Existe o ditado clássico que se você fornecer dados sujos ao modelo, a saída também será lixo (`Garbage In, Garbage Out`).
E esta limpeza está diretamente associada ao efeito de *Overfitting*, que no bom português, nada mais é que sobreajuste. A correlação com o exemplo do estudante que decora as páginas de um livro para a prova, é ótima. Se na prova cair o mesmo livro, o estudante tira 10, mas se for outro livro, ele zera. É o efeito "decoreba". Na ML, esse efeito fica evidenciado quando no treino, o algoritimo se saí otimamente, mas com dados reais, ele fracassa. Esta discrepância caracteriza um overfitting.

## 👨‍🏫 Desenvolvido por 
Paulo Sérgio Barreiros Lima<br>
Bacharel em Ciências da Computação / Aperfeiçoamento em ML e Visão Computacional.<br>
paulosergiobarreiroslima@gmail.com
