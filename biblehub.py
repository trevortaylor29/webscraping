import random
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
from twilio.rest import Client

chapter = random.randint(1,21)



webpage = 'https://biblehub.com/asv/' +  'john/' + str(chapter) + '.htm'

print(webpage)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
req = Request(webpage, headers=headers)



webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser')

verses = soup.findAll('div', attrs={'class': 'p'})


verse_list = []

for verse in verses:
    print(verse.text)

#myverse = 'Chapter: '+  str(chapter) + ' Verse: ' + random.choice(verse_list[:len(verse_list)-2])

#print(myverse)