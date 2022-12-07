# Turimas "users" masyvas. 

# Parašykite funkcijas, kurios atlikas nurodytas užduotis:
# 1. funkcija "getUserAverageAge" - kaip argumentą priims masyvą ir duoto masyvo 
# atveju grąžins visų "users" amžiaus visurkį kaip skaičių.
# 2. funkcija "getUsersNames" -  kaip argumentą priims masyvą ir duoto masyvo 
# atveju grąžins visų "users" vardus naujame list'e pvz., ['Alex John', 'Ann Smith'...].

# Pastaba: rezultatai turi būti išrikiuoti abėcėlės tvarka

users = [
  { "id": '1', "name": 'John Smith', "age": 20 },
  { "id": '2', "name": 'Ann Smith', "age": 24 },
  { "id": '3', "name": 'Tom Jones', "age": 31 },
  { "id": '4', "name": 'Rose Peterson', "age": 17 },
  { "id": '5', "name": 'Alex John', "age": 25 },
  { "id": '6', "name": 'Ronald Jones', "age": 63 },
  { "id": '7', "name": 'Elton Smith', "age": 16 },
  { "id": '8', "name": 'Simon Peterson', "age": 30 },
  { "id": '9', "name": 'Daniel Cane', "age": 51 },
]

# function 1

print("function 1:")

def getUserAverageAge(object):
  print(sum(d['age'] for d in object) / len(object))

getUserAverageAge(users)

#separation

print("\n")

#function 2

print("function 2:")

def getUserNames(object):
  newlist = []
  for user in users:
    newlist.append(user['name'])
  newlist.sort()
  print(newlist)
  
getUserNames(users)