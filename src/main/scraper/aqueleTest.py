import requests
from bs4 import BeautifulSoup


# vgm_url = 'https://www.vgmusic.com/music/console/nintendo/nes/'
# html_text = requests.get(vgm_url).text
# soup = BeautifulSoup(html_text, 'html.parser')
bgg_url = 'https://boardgamegeek.com/browse/boardgame'
html_text_bgg = requests.get(bgg_url).text
soup_bgg = BeautifulSoup(html_text_bgg, 'html.parser')

########## Função para pegar o rank
def get_rank(elemento):
    rank = int(elemento.find("td",{'class':'collection_rank'}).find('a').get('name'))
    return rank
#############
######## Função para pegar o Nome
def get_name(elemento):
    name =  elemento.find('a',{'class':"primary"}).string
    year = int(elemento.find('span').string.replace('(','').replace(')',''))
    return name , year
##########
def get_ratings(elemento):
    ratings = elemento.find_all('td',{'class':"collection_bggrating"})
    geek_rating = float(ratings[0].string)
    avg_rating = float(ratings[1].string)
    num_voters = float(ratings[2].string)
    return [geek_rating,avg_rating,num_voters]
    # get_rank = int(elemento.find("td",{'class':'collection_rank'}).find('a').get('name'))
    # print(f'esse é o rank: {get_rank}')
# for link in soup.find_all('a'):
#     print(link)
#     print(link.get('href'))

linhas = soup_bgg.find_all(id='row_')

# for element in soup_bgg.find_all("a", {"class": "primary"}):
#     print(element.string)
elemento = linhas[0]

a,b = get_name(elemento)
print(a , b)

# prices = elemento.find('td',{'class':"collection_shop"})

# print(prices)

# print(elemento, end='\n\n foi a string anterior\n\n')

# print(get_td, end='\n\n foi a string anterior\n\n')

# get_rank = get_td.find('a')

# print(int(get_rank.get('name')))