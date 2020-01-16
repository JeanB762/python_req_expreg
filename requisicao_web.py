import requests

texto = None

try:    
    requisicao = requests.get('https://putsreq.com/cZBYogK4wBfRLdp2CWUv')
    texto = requisicao.text

except Exception as e:
    print("requisicao nao processada, erro:", e)

print(texto)
print('olá')