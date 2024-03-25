# 0~9 
print(list(range(10)))

# 3~9
print(list(range(3,10)))

# 3~9 2step
print(list(range(3,10,2)))

# "테스트" 3번 반복
for i in range(3):
    print("테스트")

# 곱셈 계산
# x를 0~9 까지 반복 
for x in range(9):
    print(f'3 * {x} = {3 * x}')

# 구구단
for x in range(1,10):
    print(f'3 * {x} = {3 * x}')

# 변수명 _  ( 사용 적을 경우 )
for _ in range(9):
    print(f'3 * {_} = {3 * _}')