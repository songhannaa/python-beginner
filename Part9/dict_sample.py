# dictionary -> dict 
# create
# key : value 형식으로 저장한다 
user1 = {'name':'Spencer', 'colleage' : 'programers', 'year' : 20}
user2 = {
    'name':'Spencer',
    'colleage' : 'programers', 
    'year' : 20
}

# find (정보 출력)
print(user1['name']) # 없으면 error
print(user1.get('name')) # get 으로 가져오면 안전하게 가져올 수 있다 / 없으면 None

# access > update
user1['name'] = 'Mussg' # 이름 바뀐거 확인 할 수 있다..
# user1.get('name') = 'Spencer' get으로는 이름을 바꿀 수 없다
user1['year'] += 1
print(user1)

#add
user1['lang'] = 'Python'
print(user1)

#delete
del user1['lang']
print(user1)

if user1.get('lang'):
    del user1['lang']