dictionary1 = {
  "one": 1,
  "two": 2,
  "three": 3,
  "four": 4,
  "five": 5
}
print(type(dictionary1)) #<class 'dict'>
dictionary2 = dict()
print(dictionary1) #{}

#erismek
print(dictionary1['one']) #1
print(dictionary1['four']) #4
#!olmayana erismek
#print(dictionary1['six']) #!KEYERROR

#yeni key eklemek veya degistirmek
dictionary1['six'] = 6
dictionary1['one'] += 1
print(dictionary1['one']) #2

#ic ice dictionary
dictionary3 = {
  "fruits": ["apple", "peace"],
  'players': {
    'one': { 'name': 'Andrew', 'age': 28 },
    'two': { 'name': 'Malik', 'age': 35 },
  }
}
print(dictionary3['fruits']) #['apple', 'peace']
print(dictionary3['fruits'][0]) #apple
print(dictionary3['players']['one']) #{'name': 'Andrew', 'age': 28}
print(dictionary3['players']['one']['name']) #Andrew

#keysleri array olarak almak
print(dictionary1.keys()) #dict_keys(['one', 'two', 'three', 'four', 'five', 'six'])
#valuesleri almak
print(dictionary1.values()) #dict_values([2, 2, 3, 4, 5, 6])
#her bir sozluk elemanini liste icinde demet olarak tutmak
print(dictionary1.items()) #dict_items([('one', 2), ('two', 2), ('three', 3), ('four', 4), ('five', 5), ('six', 6)])


