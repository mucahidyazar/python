print('Add new player')

firstName = input('Player first name : ')
lastName = input('Player last name : ')
team = input('Team : ')

informations = [firstName, lastName, team]

print('Informations are saving...')

print('Player first name: {}\nPlayer last name: {}\nPlayer team: {}'.format(informations[0], informations[1], informations[2]))

print('Informations are saved.')