separarPalavra = []
voga = []
voge = []
vogai = []
vogo = []
vogu = []
n = 0

texto = input('Digite seu texto: ').lower()
while n < 1:
    for i in texto:
        separarPalavra.append(i)
        if i in "aáã":
            voga.append(i)
            separarPalavra.remove(i)
        elif i in "eéê":
            voge.append(i)
            separarPalavra.remove(i)
        elif i in "ií":
            vogai.append(i)
            separarPalavra.remove(i)
        elif i in "oóô":
            vogo.append(i)
            separarPalavra.remove(i)
        elif i in "uú":
            vogu.append(i)
            separarPalavra.remove(i)
          
    n = n + 1    
    print('A:', len(voga))
    print('E:', len(voge))
    print('I:', len(vogai))
    print('O:', len(vogo))
    print('U:', len(vogu))
 
    
