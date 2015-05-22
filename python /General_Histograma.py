t = 0
contador = 0
filename = "All_Songs.txt"
FH = open(filename,'w')
FH.write('All Songs' + '\n\n\n')
FH.close()


#f = open('SONG10.txt','r')
#for linea in f:
#    FH.write(linea)
#f.close()
#FH.close()

while t < 100:
    filename = 'SONG{0}'.format(t)+'.txt'
    #try:
    #    f = open(filename, 'r')
    #except IOError:
    #    f.close()
    
    FH = open('All_Songs.txt','a')
    f = open(filename,'r')
    for linea in f:
        FH.write(linea)
    f.close()
    FH.close()   
 
    t = t+1


filename = "All_Songs.txt"
f = open(filename,"r")
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

filename = 'FINAL_HISTOGRAM.txt'
FH = open(filename,'w')
FH.write('FINAL HISTOGRAM')
FH.write('\n\n\n')
FH.write(str(lista_final))
FH.close()