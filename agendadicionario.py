# Crie um programa que, usando dicionário, crie uma agenda de tamanho fornecido
# inicialmente pelo usuário. Leia os dados de todos os contatos do usuário
# (nome, cidade, estado, telefone) de forma que a agenda fique completa e por
# fim imprima todos os
# contatos.



agenda = {}
princ = []

n = int(input().strip())
for c in range(0, n+1):
    princ.clear()
    agenda['nome'] = input().strip()
    agenda['cidade'] = input().strip()
    agenda['estado'] = input().upper().strip()
    agenda['telefone'] = input().strip()
    #lista  recebendo dicionário
    princ.append(agenda.copy())
    #tem essa outra forma que tambèm consegue o mesmo resultado.
    #princ = agenda
    
    # o "ESTADO" é para receber a formatação :<30 não consegui colocar.
    for i in princ:
        print(
            f'{i["nome"]:<25} {i["cidade"]} ({i["estado"]}) {i["telefone"]:>30}')
   
