def calcNote(line):
  
  #print('Adana'[:-1]) #Adan
  line = line[:-1] #Salih Orbay,60,10,30/n => Salih Orbay,60,10,30
  list = line.split(',') #['Abdullah Ekşioğlu', '40', '60', '10']
  name = list[0]
  note1 = int(list[1])
  note2 = int(list[2])
  note3 = int(list[3])
  harf = 'FF'
  lastNote = note1 * (3/10) + note2 * (3/10) + note3 * (4/10)
  if lastNote >= 90:
    harf = 'AA'
  elif lastNote >= 80:
    harf = 'BA'
  elif lastNote >= 75:
    harf = 'BB'
  elif lastNote >= 70:
    harf = 'CB'
  elif lastNote >= 65:
    harf = 'CC'
  elif lastNote >= 60:
    harf = 'DC'
  elif lastNote >= 55:
    harf = 'FD'
  else:
    harf == 'FF'

  return name + '----------------> ' + harf + '\n'

with open('notes.txt', 'r', encoding='utf-8') as file:
  addedList = []
  for i in file:
    addedList.append(calcNote(i))
  with open('noteResult.txt', 'w', encoding='utf-8') as file2:
    for i in addedList:
      file2.write(i)
  with open('fail.txt', 'w', encoding='utf-8') as fail:
    for i in addedList:
      if 'FD' in i or 'FF' in i:
        fail.write(i)
  with open('success.txt', 'w', encoding='utf-8') as success:
    for i in addedList:
      if 'AA' in i or 'BB' in i or 'CB' in i or 'CC' in i or 'DC' in i:
        success.write(i)


