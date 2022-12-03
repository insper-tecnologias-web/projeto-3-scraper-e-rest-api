# Projeto 3 - TecWeb
## API:


  <div aling="center" >O Django irá auxiliar para o tratamento de dados contendo as seguintes informações salvas em um banco de dados interno como END points, e retorna-os em um .JSON:</div>
  
  | Endpoint | Descrição | 
  |-----------|:-----------:|
| rank | Jogos listados pela avaliação de jogadores| 
| name | nome completo do jogo | string |
| year | Ano de fabricação | 
| random | Escolhe um jogo aleatório | 

  - Ranqueamento, o usuário poderá filtrar os jogos de acordo com a avaliação de outros jogadores.
  - Ranqueamento/Posição na classificação(número inteiro), irá apresentar o jogo que possuí a posição do número inteiro no ranque.
  - Nome, filtra os jogos pelo nome completo.
  - Ano, filtra os jogos pelo ano de criação.
  - Random, irá entregar um jogo aleatório para o usuário.

 No caso do acesso aos itens no JSON, os dados serão apresentados dessa forma:

| Info | Descrição | Tipo|
|-----------|:-----------:|-----------:| 
| rank | Ranque do jogo | integer | 
|id| Número de identificação | integer|
| name | Nome completo do jogo | string |
| geek_rating | Categoria de 0 a 10 | float |
| avg_rating | Categoria de 0 a 10 | float |
| num_votes | Quantidade de pessoas que votaram |integer |
| year | Ano de criação | integer |



