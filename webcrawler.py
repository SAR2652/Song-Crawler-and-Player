import requests
import webbrowser
from bs4 import BeautifulSoup
def search_song(name):
    page = 1
    webbrowser.register('firefox', None, webbrowser.GenericBrowser('firefox'), 1)
    finalList=[]
    while page <= 1:
        url = 'https://gaana.com/search/' + name
        f = open(name + '.txt', 'w')
        source = requests.get(url)
        # Gets the source code of the page
        text = source.text
        soup = BeautifulSoup(text, 'html.parser')
        ref=True
        for link in soup.findAll('a', {'class': 'rt_arw'}):
            # print('hello')
            # print(link)
            href = link.get('href')
            title = link.string
            final = title + ' - ' + href
            f.write(final)
            f.write('\n')
            if ref==True:
                webbrowser.get('firefox').open(href)
                ref=False
        page += 1

def getSongName(name,opt):
    name = name.lower()
    temp = name.split()
    name = '-'.join(temp)
    if opt==True:
        search_song(name)
    else:
        return name
'''if __name__ == '__main__':
    main()'''
