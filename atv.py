import json
pessoas = []
for i in range(2):
    nome1 = input('Digite seu nome: ')
    idade1 = input('Digite sua idade: ')
    pessoal = {
        'nome' : nome1,
        'idade': idade1
}
pessoas.append(pessoal)
with open("pessoas.json", 'w') as jsonfile:
    json.dump(pessoas, jsonfile)