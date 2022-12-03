# Projeto 3 - TecWeb
## Integrantes:
- Vinícius Matheus Morales
- Pedro Cliquet do Amaral
- Lincoln Rodrigo Pereira Melo

#### Projeto
  <div aling="center">Desenvolveu-se uma interface web interativa utilizando serviços de API-RESTful, seguindos os padrões em rotas, crawler/scrappe, o CRUD em Django e ter essa aplicação publicada na internet. O tema da interface será sobre jogos de tabuleiros, com intuito de faicilitar a busca deles, utilizando novas ferramentas e características para que o usuário tenha melhor desempenho ao procura-los.</div>
___

1. Criar ambiente virtual
```bash
python3 -m venv env
```
ou
```bash
python -m venv env
```

2. Iniciar ambiente virtual
Windows PowerShell:
```bash
env\Scripts\Activate.ps1
```

Windows Prompt de Comando:
```bash
env\Scripts\activate.bat
```

Linux/MacOS:
```bash
source env/bin/activate
```

3. Instalar requirements.txt
Com o ambiente virtual rodando:
```bash
pip install -r requirements.txt
```

4. Rodar o scraper
Feito tudo mencionado anteriormente, rode:
```bash
python3 main_page_scraper.py
```
ou
```bash
python main_page_scraper.py
```

E você verá os resultados num arquivo no root chamado "data.json".

Pronto! Agora você rodou o scraper principal :-)

Os dados coletados podem ser vistos nesse arquivo ".json" que são os seguintes:

rank, name, year, geek_rating, avg_rating, num_voters.

Os dados coletados pelo scraper são armazenados no nosso banco de dados e acessamos com nossa REST API.
___
