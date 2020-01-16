import re
import requests


requisicao = requests.get('http://carmodorioclaro.mg.gov.br/portal/?Link=Contato')

padrao = re.findall(r'[\w\.-]+@[\w\.-]+', requisicao.text)

if padrao:
    print(padrao)
else:
    print("Padrão não encontrado")