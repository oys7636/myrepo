grade = ('A', 'B', 'C', 'D', 'F')
level = "B"
if level in grade :   # 변수 level 값이 튜플 grade에 있다면
    print ("학점 :", level)
print("최고학점 :", grade[0])
grade[0] =  'A+'
print(grade[0])
