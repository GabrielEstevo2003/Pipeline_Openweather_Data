**Inspiração**

Este projeto teve como inspiração um tutorial do canal "vbluuiza" no YouTube. Eu o realizei para aprender conceitos e técnicas de projeto de Engenharia de Dados, agregando e muito nos meus conhecimentos.

**Objetivo**

Este trabalho possui uma complexidade baixa, apenas para fins de aprendizagem, então o objetivo dele é:
- Criar uma Pipeline envolvendo processos de ETL sobre os dados climáticos de São Paulo enviados pela API da OpenWeather.

**Passo a Passo**

Este foi o passo a passo seguido:
1. Criar um login no site da OpenWeather para adquirir a chave de acesso à API.
2. Criar uma função de Extração que retorna uma lista dos dados retornados pela API.
3. Criar uma função de Transformação desses dados retornado para normaliza-los e trata-los.
4. Criar uma função de Carregamento para persistir os dados em um Banco de Dados.
5. Criar um container Docker com os serviços necessários.
6. Criar as Dags e Tasks para a automação da pipeline no Airflow.

**Tecnologias Utilizadas**

Utilizei o WSL, que cria um ambiente Linux dentro do windows, além do gerenciador de pacotes Python chamado UV Python para criação do ambiente virtual. Foi utilizado o Postgres como banco de dados, docker para orquestração dos serviços e airflow na automação da Pipeline. O Visual Studio Code foi meu editor de código e a linguagem usada foi o Python para a realização do projeto. Para versionamento e publicação posterior do projeto utilizei o Git e Git Hub. Portanto as técnologias envolvidas foram:

- WSL
- Python
- UV Python
- Docker
- Airflow
- Postgres
- VSCode
- Git e Git Hub

**Arquitetura Geral do Sistema**

<img width="1022" height="375" alt="image" src="https://github.com/user-attachments/assets/e6180d6f-e931-4e8c-acca-eb8806a0724a" />
OBS: Essa é a imagem da arquitetura apresentada e explicada no vídeo de tutorial.

**Resultados**

O serviço Apache Airflow que está incluido no container docker foi acessado utilizando o localhost da minha máquina na porta 8080. E aqui está um print das Tasks ETL concluídas:
<img width="1906" height="952" alt="image" src="https://github.com/user-attachments/assets/13a3769c-3ebe-48e2-a844-80b3504b1617" />

E para conferir a conclusão do processo da Pipeline eu conectei o banco no PgAdmin4 e dei um SELECT * na tabela gerada (sp_weather), e esse foi o resultado:
<img width="1617" height="953" alt="image" src="https://github.com/user-attachments/assets/e691a064-8ed5-4450-b373-772c67f5ead7" />

**Conclusão**

Este é um trabalho de Engenharia de Dados básico mas que rendeu diversos aprendizados. Tanto os fundamentos quantos os problemas que ocorreram no decorrer do desenvolvimento foram valiosos para mim. A engenharia de Dados é uma área que eu gosto e pretendo cada dia aprender e amadurecer mais nesta área.

