# 이중 for문
for x in range(1,10):
    print(x)
    for y in range(1,10):
        print(y)
    print('-'*10)

for x in range(1,10):
    for y in range(1,10):
        print(x,y)
    print('-'*10)

# 이중 for문을 사용한 구구단
for x in range(1,10):
    print(f'{x}단 입니다')
    for y in range(1,10):
        print(f'{x}*{y}={x*y}')
    print(f'{x}단 끝났습니다\n')

