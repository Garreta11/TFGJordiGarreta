import requests
import bs4


#chords = ('C','C#','Db','D','D#','Eb','E','F','F#','Gb','G','G#','Ab','A','A#','Bb','B')
name_song = 'I see Fire'
version = 'ver4'
text_file_name = name_song +' - '+  version + '.txt'

chords = ('Em','G','D','C','Am7','Bm')
session = requests.session()

req = session.get("http://tabs.ultimate-guitar.com/e/ed_sheeran/i_see_fire_ver4_crd.htm")

doc = bs4.BeautifulSoup(req.content)
f = open(text_file_name,'w')
f.write(name_song + ' - ' + version + '\n\n')
for link in doc.find_all('span'):
    for child in link.children:
        if child in chords:
            print child
            f = open(text_file_name,'a')
            f.write(child + '\n')
            f.close()
