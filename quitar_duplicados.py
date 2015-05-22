FH = open('FINAL_HISTOGRAM.txt','r')
for linea in FH:
    linea = linea
    
    wordList = []

    for x in range(len(linea)):
        for y in range(x+1,len(linea)):
            if linea[x] == linea[y]:
                wordList.append(linea[x])
                            
    for y in wordList:
        list(linea).remove(y)
        print linea