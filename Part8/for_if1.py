member = [ 'Spencer', 'Mussg', 'Allen', 'Chen','Hun']
thief = "Chen"

for person in member:
    print(person)
    if person == thief:
        print("도둑입니다!")
        break
print("검문이 끝났습니다")