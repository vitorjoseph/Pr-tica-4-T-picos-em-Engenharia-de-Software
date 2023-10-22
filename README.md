# Pratica-4-Topicos-em-Engenharia-de-Software

# Prática de Teste de Código em Python para Processamento de Dados (Big Data)

Esta prática demonstra como testar código em Python no contexto de processamento de dados, com ênfase nas boas práticas de engenharia de software. O projeto é dividido em três arquivos: `dataProcessor.py`, `gerador.py` e `testDataProcessor.py`.

## `dataProcessor.py`

O arquivo `dataProcessor.py` contém uma função que lê um arquivo JSON contendo dados de pessoas. Esta função é projetada para ser robusta e tratar exceções adequadamente. O código é organizado em um módulo.

```python
import json

def read_json_file(file_path):

    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except json.JSONDecodeError:
        raise ValueError(f"Invalid JSON format in file: {file_path}")

```

## ` gerador.py `

O arquivo ```gerador.py``` é um script que gera dados de pessoas aleatórias e os armazena em um arquivo JSON. Os dados gerados incluem nome, idade e país. Este script pode ser usado para criar diferentes tamanhos de conjuntos de dados.

```python
import json
import random
from faker import Faker

def generate_data(num_lines):
    # ... (código omitido para brevidade)
    return data

def save_to_json(data, file_path):
    # ... (código omitido para brevidade)

if __name__ == "__main__":
    # ... (código omitido para brevidade)

```
Execução: ```python gerador.py``` 

## ` testDataProcessor.py `

O arquivo ```testDataProcessor.py``` contém testes unitários para garantir a qualidade do código em ```dataProcessor.py```. Inclui testes para casos de sucesso e casos de erro.
```python
import os
import unittest
from dataProcessor import read_json_file

class TestDataProcessor(unittest.TestCase):
    def test_read_json_file_success(self):
        current_directory = os.path.dirname(__file__)
        file_path = os.path.join(current_directory, "users.json")

        data = read_json_file(file_path)
       
        self.assertEqual(len(data), 10)  # Ajustar o número esperado de registros
        self.assertEqual(data[0]['name'], 'Alice')
        self.assertEqual(data[1]['age'], 25)

    def test_read_json_file_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            read_json_file("non_existent.json")

    def test_read_json_file_invalid_json(self):
        with open("invalid.json", "w") as file:
            file.write("invalid json data")
        with self.assertRaises(ValueError):
            read_json_file("invalid.json")

if __name__ == '__main__':
    unittest.main()

```
Execução: ```python testDataProcessor.py``` 


# Executando a Prática

1. Certifique-se de ter as bibliotecas necessárias instaladas, como o Faker, que pode ser instalado com `pip install Faker`.
2. Execute o script gerador para criar o arquivo JSON: `python gerador.py`.
3. Execute o script de teste para avaliar a qualidade do código: `python testDataProcessor.py`.

Certifique-se de que os arquivos de dados e os arquivos de teste estejam organizados corretamente para a execução adequada. Ajuste os valores esperados nos testes conforme necessário com base nos dados gerados.

## Atividade

- No arquivo `testDataProcessor.py`, escreva mais testes unitários para a função `avgAgeCountry`. Considere cenários como:

    - Arquivo JSON vazio.
    - Valores de idade ausentes ou nulos.
    - Campo `country` ausente ou nulo.

- Implemente mais funções que realizam diferentes tipos de processamento de dados e teste-as.

- Modifique a função `avgAgeCountry` para que ela aceite uma função de transformação como segundo argumento. Esta função deve ser aplicada à idade antes de calcular a média (por exemplo, converter idade de anos para meses). Escreva testes para essa nova funcionalidade.

## Relatório

Depois de concluir a atividade, reflita sobre os desafios de escrever testes para big data e a importância de testar funções que processam grandes volumes de dados. Considere também a otimização de performance com PySpark. Para isso, escreva um relatório técnico que mostre a importância dos seus testes e qual era o seu objetivo. O relatório deve abordar os tipos de teste e qual era a sua intenção com esses testes, por exemplo, quais problemas você estava tentando evitar. Para essa atividade é obrigatório apenas o teste unitário. Porém, o aluno pode desenvolver diferentes asserts para o teste unitário. Explique a importância das outras funções que você criou. O template para o relatório pode ser acessado em: [Overleaf](coloque_aqui_o_link_para_o_template).

## Avaliação

Os critérios de avaliação incluem:

- Correção e robustez dos testes.
- Detecção de problemas.
- Explicação via relatório.


