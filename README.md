# Teste técnico para vaga de estágio na Dell

## Programa IT Academy – Processo Seletivo

### Problema

Internações em Porto Alegre

### Instruções para Desenvolvimento e Empacotamento
---------------
Desenvolva uma solução para o problema utilizando a linguagem/ambiente que preferir. Mesmo que não consiga concluir, que faça apenas partes da solução ou que tenha uma solução com erros, faça o envio e entregue o que tiver conseguido fazer.
Também deve ser enviado um arquivo em PDF com a explicação da solução. Além dessa explicação, o arquivo também poderá conter capturas de tela demonstrando a execução, os resultados e os seus testes, utilizando as estratégias e ferramentas que conhecer.
Empacote todos os arquivos em .zip e faça o envio conforme for instruído.
Para explicações do código fonte adicione comentários.

### Descrição
---------------
Devido a pandemia do COVID-19 o número de internações nos hospitais de todo mundo aumentou consideravelmente. No Rio Grande do Sul isso não foi diferente. Os hospitais passaram a ficar superlotados, não somente com  pessoas infectadas pelo coronavírus, mas também por pessoas que possuem outros tipos de comorbidades, que sofreram acidentes entre diversos motivos.

Você como cidadão rio-grandense e por curiosidade resolveu analisar essas internações, o tempo de duração delas e os hospitais mais requisitados, para facilitar sua análise você decidiu escrever um programa para ajudá-lo. Neste link você encontra o dicionário de dados e a respeito dessas internações: http://datapoa.com.br/dataset/gerint-gerenciamento-de-internacoes/resource/68958cc6-1712-4a7c-b20c-0d912286cfc8

### Funcionalidades
---------------
Ao iniciar o programa, deve-se fazer a leitura do arquivo .csv que está sendo enviado junto com esta explicação. Neste arquivo você encontra as informações sobre as internações no Rio Grande do Sul. A partir delas, você deve implementar as seguintes funcionalidades:

>1. `Consultar média de idade dos pacientes - ` Permitir que o usuário informe o nome do município residencial e como resultado o programa deverá exibir:
>    - O número total de pacientes do município;
>    - A média de idade dos pacientes separados por gênero;
>    - A média de idade de todos os pacientes;

>2. `Consultar internações por ano - ` Permitir que o usuário informe o nome do município residencial e como resultado o programa deverá exibir uma lista com os anos de 2018 a 2021 e a quantidade de pacientes que foram internados por ano;

>3. `Consultar hospitais - ` Permitir que o usuário digite o nome do executante e como resultado o programa deverá exibir todos os pacientes que foram internados, sua idade, o município residencial e solicitante de cada um deles, as datas de autorização, de internação e alta e o executante;

>4. `Calcular tempo de internação - ` Permitir que o usuário digite o nome do solicitante e como resultado o programa deverá exibir:
>    - Uma lista com todos os pacientes;
>    - O nome dos hospitais executantes;
>    - O número de dias que os pacientes permaneceram internados desde a solicitação até a alta deste paciente;

>5. `Determinar tempos de espera na fila - ` O programa deverá determinar e exibir os cinco casos com maior tempo de espera na fila;

>6. `Terminar o programa - ` Permitir que o usuário saia do programa.

#### Observações:
---------------
- Sugere-se o desenvolvimento de um programa na linguagem de sua preferência, com uma interface também de sua preferência podendo ser gráfica ou textal/console, com um menu com as opções enumeradas nos requisitos;

- Juntamente a este enunciado foi fornecido um arquivo no formato CSV contendo os municípios, gêneros, datas em um formato tabular;

- Você deve escrever o código que lê o arquivo e armazena os dados lidos em memória (do jeito que você quiser).

- Não é necessário gravar dados em nenhum formato, nem usar sistemas de bancos de dados.

- O programa deverá lidar com dados de entrada inválidos e informar uma mensagem adequada caso ocorram.

- Para facilitar, não é necessário lidar com a acentuação de palavras.

- Na escrita do relatório apresente comentários sobre como você realizou a implementação dos testes.