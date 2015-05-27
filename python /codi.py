# -*- coding: utf-8 -*-
import requests
import bs4

i = 0

# comentario de código para mejorar la interacción...

#chords = ('C','C#','Cm',
#'Db','D','D#','Dm',
#'Eb','E','Em',
#'F','F#','Fm',
#'Gb','G','G#','Gm',
#'Ab','A','A#','Am','Am7',
#'Bb','B','Bm')


chords_root = (
'Cb','C','C#',
'Db','D','D#',
'Eb','E','E#',
'Fb','F','F#',
'Gb','G','G#',
'Ab','A','A#',
'Bb','B','B#')

chords_type = ('', 'm', 'M','aug','dim','7')

chords = []

for chords1 in chords_root:
    for chords2 in chords_type:
        final_chords = chords1+chords2
        chords.append(final_chords)

chords = tuple(chords)

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
            #f.write(song_name + '\n')
            for link in doc.find_all('span'):
                for child in link.children:
                    if child in chords:
                                                                        
                        #----Enharmonic Chords----
                        child = child.replace('C#','Db')
                        child = child.replace('D#','Eb')
                        child = child.replace('F#','Gb')
                        child = child.replace('G#','Ab')
                        child = child.replace('A#','Bb')
                       
                        #----Good Format of Representation----
                        if child.endswith('b'):
                            child = child[:2]+':'+child[2:]
                        elif child.startswith('m',1):
                            child = child[:1]+':'+child[1:]
                        elif child.startswith('M',1):
                            child = child[:1]+':'+child[1:]
                            #print child ----NO FA RES!!!
                        elif child.startswith('aug',1):
                            child = child[:1]+':'+child[1:]
                        elif child.startswith('dim',1):
                            child = child[:1]+':'+child[1:]
                        elif child.startswith('7',1):
                            child = child[:1]+':'+child[1:]
                        elif child.startswith('sus4',1):
                            child = child[:1]+':'+child[1:]
                         
                        #----m = min----
                        if child.endswith('dim'):
                            child = child.replace('dim',':dim')
                        elif child.endswith('m'):
                            child = child.replace('m','min')
                        
                        if child.endswith(':'):
                            child = child.replace(':',':maj')
                                                
                        if child.endswith('C'):
                            child = child.replace('C','C:maj') 
                        if child.endswith('D'):
                            child = child.replace('D','D:maj') 
                        if child.endswith('E'):
                            child = child.replace('E','E:maj') 
                        if child.endswith('F'):
                            child = child.replace('F','F:maj') 
                        if child.endswith('G'):
                            child = child.replace('G','G:maj') 
                        if child.endswith('A'):
                            child = child.replace('A','A:maj') 
                        if child.endswith('B'):
                            child = child.replace('B','B:maj') 
                        
                        if child.endswith('bmin'):
                            child = child.replace('bmin','b:min')
                                                
                        child = str(child)
                        print child
                        
                        #----Write to each file----
                        f = open(text_file_name,'a')
                        f.write(child + '\n')
                        f.close