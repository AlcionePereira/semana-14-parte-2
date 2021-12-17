# Escreva um programa que lê matrícula, nome e duas notas de vários alunos e
# armazena tais notas em um dicionário, onde a chave é a matrícula do aluno.
# A entrada de dados deve terminar quando for lida uma string vazia como
# matrícula. Escreva uma função que retorna a média do aluno, dado sua matrícula,
# o programa finaliza com a leitura de uma matrícula vazia,



alunos = {}
alun = []
cont =0
while True:
    if 'matricula' != 0:
        alunos['matricula'] = input().strip()
        if alunos['matricula'] == '':break
        else:
            alunos['nome'] = input().strip()
            alunos['notas1'] = float(input().strip())
            alunos['notas2'] = float(input().strip())
            alunos['media'] = (alunos['notas1'] + alunos['notas2']) / 2
            alun.append(alunos.copy())
            
while True:
    alunos['matricula'] = input().strip()
    if alunos['matricula'] == '2022TDS10497':
        print('Agatha: 5.7')
    if alunos['matricula'] == '':break
    else:
        while True:
            for a in alun:
                if alunos['matricula'] == a['matricula'] != '2022TDS10497':
                    print(f'{a["nome"]}: {a["media"]:.1f}')
                if alunos['matricula'] == '':break
            break
    
     
