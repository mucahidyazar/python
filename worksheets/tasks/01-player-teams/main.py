
with open('players.txt', 'r', encoding='utf-8') as readPlayers:
  players = []
  for x in readPlayers:
    player = x.split(',')
    players.append({
      'name': player[0],
      'team': player[1][:-1]
    })
  
  with open('galatasaray.txt', 'w', encoding='utf-8') as writeGalatasaray:
    for x in players:
      if x['team'] == 'Galatasaray':
        writeGalatasaray.write(x['name'] + ' - ' + x['team'] + '\n')

  with open('besiktas.txt', 'w', encoding='utf-8') as writeBesiktas:
    for x in players:
      if x['team'] == 'Beşiktaş':
        writeBesiktas.write(x['name'] + ' - ' + x['team'] + '\n')

  with open('fenerbahce.txt', 'w', encoding='utf-8') as writeFenerbahce:
    for x in players:
      if x['team'] == 'Fenerbahçe':
        writeFenerbahce.write(x['name'] + ' - ' + x['team'] + '\n')