import requests
#GET - get data
#POST - set data
#PATCH - update data
#DELETE - delete data

url = 'http://127.0.0.1:5000/'
u = url

print("----Selecione uma ação para interagir com seu bichinho----\n")
print("1 - verificar status atual\n2 - alimenta-lo\n3 - brincar\n4 - coloca-lo pra dormir\n5 - dar remedio")

while(True):
    req = int(input("Valor: "))

    if req == 0:
        break
    elif req == 1:
        url+= "status"
        resposta = requests.get(url)
        print(resposta.json())
        url = u
        continue
    elif req == 2:
        url += "food"
    elif req == 3:
        url += "play"
    elif req == 4:
        url += "sleep"
    elif req == 5:
        url += "medicine"

    resposta = requests.put(url)
    print(resposta.json())
    url = u


