import requests
from bs4 import BeautifulSoup

from consultaCNPJ import response

response = requests.get('https://www.stuttgart.com.br/padaria.html')

if response.status_code == 200:
    soup = BeautifulSoup(response.text,'html.parser')
    lista_produtos, lista_precos = [], []
    for nome_produto in soup.select('.type1 .product-item-link'):
        lista_precos.append(nome_produto.text.strip())

    for preco_produto in soup.select('.type1 .price'):
        lista_precos.append(preco_produto.text)

    dados = zip(lista_produtos, lista_precos)


