import requests
import json

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'

response = requests.get(url)

print(response)  # Código da Resposta

if response.status_code == 200:
    dados_json = response.json()
    print("Resposta bem-sucedida!")
    # print(json.dumps(dados_json, indent=4)) # Resposta formatada
    dados_restaurante = {}
    for item in dados_json:
        nome_do_restaurante = item['Company']
        if nome_do_restaurante not in dados_restaurante:
            dados_restaurante[nome_do_restaurante] = []
        dados_restaurante[nome_do_restaurante].append({
            "item": item['Item'],
            "price": item['price'],
            "descricao": item['description']
        })
else:
    print(f"Erro! Status: {response.status_code}")

for nome_do_restaurante, dados in dados_restaurante.items():
    nome_do_arquivo = f'{nome_do_restaurante}.json'
    with open(nome_do_arquivo, 'w') as arquivo_restaurante:
        json.dump(dados, arquivo_restaurante, indent=4)

print(json.dumps(dados_restaurante['McDonald’s'], indent=4))
