#Crie um programa que cadastre informações de 20 pessoas (nome, idade e cpf)
#e coloque em um dicionário. Após a leitura, remova todas as pessoas menores
#de 18 anos do dicionário e coloque-as separadas em outro dicionário. Imprima
#os dois dicionários separando os campos por ;
#(ponto-e-vírgula).




pessoa={}
grupo=[]

menoresgp=[]
maioresgp=[]

for c in range(20):
    pessoa.clear()
    pessoa['nome']=input().strip()
    pessoa['idade']=int(input())
    pessoa['cpf']=input().strip()
    grupo.append(pessoa.copy())

for p in grupo:
    if p['idade']>=18:
        maioresgp.append(p.copy())
    if p['idade']<18:
        menoresgp.append(p.copy())

print('========== MAIORES DE 18 ANOS ==========')

for p in maioresgp:
    print(f"{p['nome']};{p['idade']};{p['cpf']}")

print('========== MENORES DE 18 ANOS ==========')

for p in menoresgp:
    print(f"{p['nome']};{p['idade']};{p['cpf']}")
