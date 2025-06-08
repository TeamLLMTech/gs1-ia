# Solução de Classificação de Eventos Climáticos Extremos

Este repositório contém uma solução de Machine Learning desenvolvida para prever a ocorrência de eventos climáticos extremos no Brasil, utilizando dados históricos meteorológicos.

## Vídeo de Demonstração

Assista ao vídeo de demonstração do projeto: [Vídeo de Demonstração](https://youtu.be/CmF9GxCWf2c)

## Estrutura do Projeto

- `dataset_climatico.csv`: Base de dados com registros históricos de clima e classificação de eventos extremos.
- `notebook_modelo_climatico.ipynb`: Notebook com análise exploratória, preparação dos dados, treinamento, avaliação e salvamento do modelo.
- `modelo_climatico.pkl`: Modelo treinado (Random Forest) salvo para uso em produção.
- `label_encoder.pkl`: Encoder dos rótulos das classes de eventos.
- `predict.py`: Script para realizar predições com novos dados utilizando o modelo treinado.

## Como utilizar

1. **Requisitos**
   - Python 3.8+
   - Instale as dependências:
     ```sh
     pip install pandas scikit-learn joblib
     ```

2. **Treinamento do Modelo**
   - O notebook [`notebook_modelo_climatico.ipynb`](notebook_modelo_climatico.ipynb) realiza todo o processo de análise, treinamento e salvamento do modelo e do encoder.

3. **Realizando Predições**
   - Edite o arquivo [`predict.py`](predict.py) para inserir os dados meteorológicos desejados.
   - Execute o script:
     ```sh
     python predict.py
     ```
   - O script exibirá a probabilidade de cada classe e a classificação prevista para a entrada informada.

## Classes de eventos previstos

- nenhum
- chuva_torrencial
- ciclone
- enchente
- onda_calor
- onda_frio
- seca

## Autores

Grupo LLM - FIAP - 1º Semestre de 2025  
- Gabriel Marques de Lima Sousa - RM 554889 - 2TDSPW
- Leonardo Matheus Teixeira - RM 556629 - 2TDSPW
- Leonardo Menezes Parpinelli Ribas - RM 557908 - 2TDSPW

---

Projeto acadêmico desenvolvido para a disciplina de DISRUPTIVE ARCHITECTURES - IOT, IOB And GENERATIVE.