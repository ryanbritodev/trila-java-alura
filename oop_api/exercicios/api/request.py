import requests
import json

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'

status = requests.get(url)

dados_restaurante = {}

if status.status_code == 200:
    print(f"Requisição bem-sucedida! Status: {status.status_code}")
    dados_json = status.json()
    # print(json.dumps(dados_json, indent=4))

    for itens in dados_json:
        nome_restaurante = itens['Company']
        if nome_restaurante not in dados_restaurante:
            dados_restaurante[nome_restaurante] = []

        dados_restaurante[nome_restaurante].append({
            "item_menu": itens['Item'],
            "preco": itens['price'],
            "descricao": itens['description']
        })

else:
    print(f"Erro na requisição. Status: {status.status_code}")

print(json.dumps(dados_restaurante, indent=4))