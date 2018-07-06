import requests
from bs4 import BeautifulSoup
import re

url = 'https://mojim.com/twh100156.htm'
resp = requests.get(url)
soup = BeautifulSoup(resp.text, 'html.parser')
block = soup.find_all('dd', 'hb2')
block2 = soup.find_all('dd','hb3')

def writeFile(i):
        j = i.get('href')
        sub_resp = requests.get("https://mojim.com" + j)
        sub_soup = BeautifulSoup(sub_resp.text, 'html.parser')
        sub_name = sub_soup.find('dd','fsZx3')
        path = "lyrics/" + i.get('title').split(' 歌')[0] + ".txt"
        f = open(path, 'w')
        f.write(sub_name.text)

for i in block: 
    song_left = i.find_all('span','hc3')
    for j in song_left:
        sl = j.find_all('a')
        for k in sl:
           writeFile(k)
                
    song_right = i.find_all('span','hc4')
    for j in song_right:
        sr = j.find_all('a')
        for k in sr:
            writeFile(k)
        
for i in block2: 
    song_left = i.find_all('span','hc3')
    for j in song_left:
        sl = j.find_all('a')
        for k in sl:
           writeFile(k)
                
    song_right = i.find_all('span','hc4')
    for j in song_right:
        sr = j.find_all('a')
        for k in sr:
            writeFile(k)

