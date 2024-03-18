'''
문제 설명
아래 정보를 참고하여, 머쓱이의 정보를 출력하는 코드를 완성하세요

정보	값
이름(Name)	머쓱이
과(Family)	벌새과
키(Height)	17


출력

머쓱이(벌새과, 17cm)
'''

name = "머쓱이"
family = "벌새과"
height = 17

text = "머쓱이({1}, {2}cm)".format(name, family, height)
print(text)