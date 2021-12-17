#Crie um dicionário e armazene nele os dados de livros: título, isbn, autor
# e preço. A chave do dicionários será um código numérico e sequencial,
# gerado automaticamente, iniciando pelo número 101 (cento e um). A leitura de
# uma descrição vazia para o título finaliza a leitura. Imprima todos os dados
# usando o padrão “Nome do Campo: valor”.

chave = 100
dados = {}

while True:
    if 'Titulo' != 0:
        dados['Título'] = input().strip()
        if dados['Título'] == '':break
    
        else:
            dados['ISBN'] = input().strip()
            dados['Autor'] = input().strip()
            dados['Preço'] = float(input().strip())
            chave+=1
        print(f'Código: {chave}')
        print(f'Título: {dados["Título"]}')
        print(f'ISBN: {dados["ISBN"]}')
        print(f'Autor: {dados["Autor"]}')
        print(f'Preço: {dados["Preço"]:.2f}')
       
