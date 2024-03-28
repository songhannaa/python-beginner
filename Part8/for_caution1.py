member = ['Spencer', 'Mussg', 'Allen', 'Chen','Hun','Andy','Darby']

# member 배열을 반복문 돌면서 
for user in member:
    if user[0] in ['A','a']:
        member.remove(user)
print(member)

#기대 : ['Spencer', 'Mussg', 'Allen', 'Chen','Hun']
#실제 : ['Spencer', 'Mussg', 'Allen', 'Chen','Hun','Andy','Darby']