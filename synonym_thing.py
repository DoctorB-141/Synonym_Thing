import requests
from bs4 import BeautifulSoup
import random
def findSynonym(word, num):
    word = str(word)
    r = requests.get("http://www.thesaurus.com/browse/" + word)
    soup = BeautifulSoup(r.content, "html.parser")
    links = []
    synonyms = []
    for link in soup.find_all('a'):
        links.append(link.get('href'))
    for x in links:
        test = "/browse/" in str(x)
        if(test == True):
            x = x.replace("/browse/","")
            synonyms.append(x)
    return synonyms[num + 2]
sentence = input("input sentence: ")
sentence = sentence.split(" ")
print(sentence[0])
for z in sentence:
    print(findSynonym(z, random.randrange(1, 5)) + " ", end = "")
