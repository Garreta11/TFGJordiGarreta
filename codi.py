import requests
import bs4

i = 0


chords = ('C','C#','Cm',
'Db','D','D#','Dm',
'Eb','E','Em',
'F','F#','Fm',
'Gb','G','G#','Gm',
'Ab','A','A#','Am','Am7',
'Bb','B','Bm')


chords_root = (
'C','C#','Cb',
'D','D#','Db',
'E','E#','Eb',
'F','F#','Fb',
'G','G#','Gb',
'A','A#','Ab',
'B','B#','Bb')

chords_type = ('', 'm', 'M','aug','dim','7')
'''
si aparece la combinacion de los dos
'''
'''
for chords1 in chords_root:
    for chords2 in chords_type:
        chords = chords1+chords2
'''

url = requests.session()
top100 = url.get('http://www.ultimate-guitar.com/top/top100.htm');
codi = bs4.BeautifulSoup(top100.content)
for link in codi.find_all('a'):
    urls = link.get('href')
    if urls[(len(urls)-3):(len(urls))] == 'htm':
        if urls[0:11] == 'http://tabs':
            songs = urls
            '''
            print songs
            '''
            text_file_name = 'SONG{0}'.format(i)+'.txt'  
            i = i+1      
            session = requests.session()
            req = session.get(songs)
            doc = bs4.BeautifulSoup(req.content)
            f = open(text_file_name,'w')
            endurl = len(songs)-4
            song_name = songs[34:endurl]
            f.write(song_name + '\n')
            for link in doc.find_all('span'):
                for child in link.children:
                    '''
                    ignorar lo que aparece a la derecha del slash (incuido)
                    '''
                    if child in chords:
                        '''
                        print child
                        '''
                        f = open(text_file_name,'a')
                        f.write(child + '\n')
                        f.close
'''
- El acorde inicial     ------------DONE----------------
- El acorde final       -----------NOT DONE-------------
- Quitar duplicados (ordenado!)
- Histograma de los acordes --> grados 1, 4 y 5 son los mas importantes
- Estimar la tonalidad con los datos anteriores
- Encontrar patrones (de 3 a 8 acordes) dentro de la misma cancion (min 3 veces)
- histograma total de todas las canciones (como estadistica) --------DONE-------
                        
'''