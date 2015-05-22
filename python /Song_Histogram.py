t = 0
while t < 100:
    filename = 'SONG{0}'.format(t)+'.txt'
    
    f = open(filename,'r')
    
    contenido = f.readlines()
    f.close()
    
    lista = []
    lista_final = []
    
    for numero in contenido:
        lista += numero.split()
    
    lista.sort()
    set_lista = set(lista)
    set_lista = list(set_lista)
    set_lista.sort()
    
    for numero in set_lista:
        lista_final.append((lista.count(numero), numero))
    
    print lista_final
    
    filename = 'Histogram{0}'.format(t)+'.txt'
    FH = open(filename,'w')
    FH.write('Histogram')
    FH.write('\n\n\n')
    FH.write(str(lista_final))
    FH.close()
    
    t = t+1