# API para Detecção de Fraudes em Cartões de Crédito

Neste projeto desenvolvemos uma solução de uma API que retorna se uma transação de cartão de crédito é ou não fraudulenta.

Foi utilizado o seguinte dataset presente no Kaggle:

[Credit Card Fraud Detection](https://www.kaggle.com/mlg-ulb/creditcardfraud)

Principais tecnologias utilizadas no projeto:
- Python 3.9.16
- [Poetry](https://python-poetry.org/) para gerenciamento de dependências
- FastAPI para criação da API
- Docker para conteinarização da solução


Para análise de dados e construção do modelo, devido ao tempo, foi feito algo básico: um classificador que separa as transações entre fraudulentas e não-fraudulentas utilizando o XGBoost Classifier. Os dados utilizados são altamente desbalanceados, então claramente a acurácia da classificação é alta. Nesse caso, utilizamos outros tipos de métricas para classificação, como o F1-score. Podemos inserir nesse processo o MLFlow para gerenciamento do ciclo de vida do modelo.

Para ver análises e modelos mais detalhados em outro projetos anteriores, confira:

- https://github.com/diascarolina/project-insurance-forecast
- https://github.com/diascarolina/vacinacao-geral-no-brasil
- https://github.com/diascarolina?tab=repositories

O modelo foi salvo em `.pkl` e importado para o script da API.

Finalmente, para realizarmos predições instantâneas construímos uma API utilizando a biblioteca FastAPI. Essa biblioteca foi escolhida pela sua facilidade de uso, funções existentes, suporte e velocidade.

Para predições em lotes (batch), também foi utilizada uma solução com uma API do FastAPI. Em um sistema mais robusto, nesse caso pode ser utilizado o Airflow para schedular quando as predições serão enviadas em lotes para o modelo. Com o Kubernetes também conseguimos disponibilizar uma arquitetura que se adapte à quantidade de dados utilizada. Já o Kafka seria o componente utilizado para gerar eventos dos dados, os armazenando em um banco de dados adequado. Com as predições, podemos usar soluções para criação e análise de métricas, como o Grafana ou o Datadog.

Utilizamos o Poetry para o gerenciamento de dependências Python. Foi escolhido pois se mostra como uma solução moderna, simples e rápida. 

## Rodando o projeto com Docker:

Faça o clone do projeto e vá para a pasta criada.

Para rodar o projeto certifique-se que o Docker está instalado e rodando e utilize o comando:

```shell
docker build  \
      -t fraud-detection-api \
      --no-cache .
```

E, finalmente,

```shell
docker run -it -p 8000:8000 fraud-detection-api
```

Com o build do projeto em docker já é rodado o pytest para o teste de predições.

## Realizando requisições para a API

Com o app rodando localmente ou pelo contâiner, podem ser realizadas as requisições.

Conferindo se está tudo funcionando:

```bash
curl --location 'http://localhost:8000/health'
```

Resultado esperado:

```bash
{"status": "Up and running"}
```

Exemplo de request único:

```bash
curl --location 'http://localhost:8000/predict' \
--header 'Content-Type: application/json' \
--data '{
    "Time": 0.0,
    "V1": -1.3598071337,
    "V2": -0.0727811733,
    "V3": 2.536346738,
    "V4": 1.3781552243,
    "V5": -0.3383207699,
    "V6": 0.4623877778,
    "V7": 0.2395985541,
    "V8": 0.0986979013,
    "V9": 0.3637869696,
    "V10": 0.090794172,
    "V11": -0.5515995333,
    "V12": -0.6178008558,
    "V13": -0.9913898472,
    "V14": -0.3111693537,
    "V15": 1.4681769721,
    "V16": -0.4704005253,
    "V17": 0.2079712419,
    "V18": 0.0257905802,
    "V19": 0.4039929603,
    "V20": 0.2514120982,
    "V21": -0.0183067779,
    "V22": 0.2778375756,
    "V23": -0.1104739102,
    "V24": 0.0669280749,
    "V25": 0.1285393583,
    "V26": -0.1891148439,
    "V27": 0.1335583767,
    "V28": -0.0210530535,
    "Amount": 149.62
}'
```

Resultado esperado:

```shell
{
    "status": "success",
    "predicted_class": "0"
}
```



Exemplo de request em batch (a quantidade de dados enviados pode ser modificada):

```bash
curl --location 'http://localhost:8000/predict_batch' \
--header 'Content-Type: application/json' \
--data '[
    {
        "Time": 0.0,
        "V1": -1.3598071337,
        "V2": -0.0727811733,
        "V3": 2.536346738,
        "V4": 1.3781552243,
        "V5": -0.3383207699,
        "V6": 0.4623877778,
        "V7": 0.2395985541,
        "V8": 0.0986979013,
        "V9": 0.3637869696,
        "V10": 0.090794172,
        "V11": -0.5515995333,
        "V12": -0.6178008558,
        "V13": -0.9913898472,
        "V14": -0.3111693537,
        "V15": 1.4681769721,
        "V16": -0.4704005253,
        "V17": 0.2079712419,
        "V18": 0.0257905802,
        "V19": 0.4039929603,
        "V20": 0.2514120982,
        "V21": -0.0183067779,
        "V22": 0.2778375756,
        "V23": -0.1104739102,
        "V24": 0.0669280749,
        "V25": 0.1285393583,
        "V26": -0.1891148439,
        "V27": 0.1335583767,
        "V28": -0.0210530535,
        "Amount": 149.62
    },
    {
        "Time": 0.0,
        "V1": -1.3598071337,
        "V2": -0.0727811733,
        "V3": 2.536346738,
        "V4": 1.3781552243,
        "V5": -0.3383207699,
        "V6": 0.4623877778,
        "V7": 0.2395985541,
        "V8": 0.0986979013,
        "V9": 0.3637869696,
        "V10": 0.090794172,
        "V11": -0.5515995333,
        "V12": -0.6178008558,
        "V13": -0.9913898472,
        "V14": -0.3111693537,
        "V15": 1.4681769721,
        "V16": -0.4704005253,
        "V17": 0.2079712419,
        "V18": 0.0257905802,
        "V19": 0.4039929603,
        "V20": 0.2514120982,
        "V21": -0.0183067779,
        "V22": 0.2778375756,
        "V23": -0.1104739102,
        "V24": 0.0669280749,
        "V25": 0.1285393583,
        "V26": -0.1891148439,
        "V27": 0.1335583767,
        "V28": -0.0210530535,
        "Amount": 149.62
    },
    {
        "Time": 0.0,
        "V1": -1.3598071337,
        "V2": -0.0727811733,
        "V3": 2.536346738,
        "V4": 1.3781552243,
        "V5": -0.3383207699,
        "V6": 0.4623877778,
        "V7": 0.2395985541,
        "V8": 0.0986979013,
        "V9": 0.3637869696,
        "V10": 0.090794172,
        "V11": -0.5515995333,
        "V12": -0.6178008558,
        "V13": -0.9913898472,
        "V14": -0.3111693537,
        "V15": 1.4681769721,
        "V16": -0.4704005253,
        "V17": 0.2079712419,
        "V18": 0.0257905802,
        "V19": 0.4039929603,
        "V20": 0.2514120982,
        "V21": -0.0183067779,
        "V22": 0.2778375756,
        "V23": -0.1104739102,
        "V24": 0.0669280749,
        "V25": 0.1285393583,
        "V26": -0.1891148439,
        "V27": 0.1335583767,
        "V28": -0.0210530535,
        "Amount": 149.62
    }
]'
```

Resultado esperado:

```shell
{
    "status": "success",
    "predictions": "[0,0,0]"
}
```

## Enviando um arquivo .csv

Também é possível enviar um arquivo .csv para a API. Será retornado um arquivo .csv igual ao submetido com a adição das predições calculadas de cada linha.

Isso pode ser feito atráves da própria URL de docs que o FastAPI sobe junto com a API.

Acesse `http://localhost:800/docs` após o app subir.

Procure pela url `upload_csv` e clique em `Try it out`.

Envie o arquivo de teste disponível em `data/request_test_data.csv`: https://raw.githubusercontent.com/diascarolina/fraud-detection-api/main/data/request_test_data.csv

Serão retornadas as predições para esse arquivo.
