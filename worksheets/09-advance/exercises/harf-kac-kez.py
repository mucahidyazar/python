print("""
  QUESTION:
  Elinizde uzunca bir string olsun.
      "ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb"
  Bu string içindeki harflerin frekansını (bir harfin kaç defa geçtiği) bulmaya çalışın.
""")

newString = "ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb"

newList = dict()

for x in newString:
  if x in newList:
    newList[x] += 1
  else:
    newList[x] = 1

print(newList)

