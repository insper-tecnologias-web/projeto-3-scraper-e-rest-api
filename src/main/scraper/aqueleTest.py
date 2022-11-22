import requests
from bs4 import BeautifulSoup
import json 
from pathlib import Path

cur_dir = Path(__file__).parent.cwd()/'src'/'data'/'testejson.json'
print('esse é o diretório:', cur_dir)
# vgm_url = 'https://www.vgmusic.com/music/console/nintendo/nes/'
# html_text = requests.get(vgm_url).text
# soup = BeautifulSoup(html_text, 'html.parser')
bgg_url = 'https://boardgamegeek.com/browse/boardgame'
html_text_bgg = requests.get(bgg_url).text
soup_bgg = BeautifulSoup(html_text_bgg, 'html.parser')
grande_json= []
########## Função para pegar o rank
def get_rank(elemento):
    rank = int(elemento.find("td",{'class':'collection_rank'}).find('a').get('name'))
    return rank
######## Função para pegar o Nome
def get_name_year(elemento):
    name =  elemento.find('a',{'class':"primary"}).string
    try:   
        year = int(elemento.find('span').string.replace('(','').replace(')',''))
    except:
        year = None
    return name , year
######
def get_ratings(elemento):
    ratings = elemento.find_all('td',{'class':"collection_bggrating"})
    geek_rating = float(ratings[0].string)
    avg_rating = float(ratings[1].string)
    num_voters = float(ratings[2].string)
    return [geek_rating,avg_rating,num_voters]
################    
def get_description(elemento):
    description = elemento.find('p').string.strip()
    return description
##############

# get_rank = int(elemento.find("td",{'class':'collection_rank'}).find('a').get('name'))
# print(f'esse é o rank: {get_rank}')
# for link in soup.find_all('a'):
#     print(link)
#     print(link.get('href'))
def constroi_json(name,year,geek_rating,avg_rating,num_voters,rank):
    data = {
        "name": name,
        "year" : year,
        "geek_rating" : geek_rating,
        "avg_rating" : avg_rating,
        "num_voters" : num_voters,
        "rank" : rank
    }
    return data


# linhas = soup_bgg.find_all(id='row_')
# elemento = linhas[0]
bgg_url_page_base = "https://boardgamegeek.com/browse/boardgame/page/"
for i in range(1,30):
    print('entrou aqui',  i)
    bgg_url_page = bgg_url_page_base + str(i)
    html_text_bgg = requests.get(bgg_url_page).text
    soup_bgg = BeautifulSoup(html_text_bgg, 'html.parser')
    linhas = soup_bgg.find_all(id='row_')
    for elemento in linhas:
        rank = get_rank(elemento)
        name, year = get_name_year(elemento)
        geek,avg,voters = get_ratings(elemento)
        # description = get_description(elemento)
        data = constroi_json(name,year,geek,avg,voters,rank)
        grande_json.append(data)
json_object = json.dumps(grande_json, indent=4)
with open(cur_dir, "w") as outfile: 
    outfile.write(json_object)

 
# for element in soup_bgg.find_all("a", {"class": "primary"}):
#     print(element.string)

# prices = elemento.find('td',{'class':"collection_shop"})

# print(prices)

# print(elemento, end='\n\n foi a string anterior\n\n')

# print(get_td, end='\n\n foi a string anterior\n\n')

# get_rank = get_td.find('a')

# print(int(get_rank.get('name')))