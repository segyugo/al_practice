#첫 줄에 N명의 학생정보 출력
#두번째 줄부터 이름과 성적정보 주어짐
#성적 낮은 순서대로 이름 출력

def setting(data):
    return data[1]



N = int(input())

info_list = []

for i in range(N):
    name, grade = input().split()
    info = []
    info.append(name)
    info.append(grade)
    info_list.append(info)

info_list.sort(key = setting)
print(info_list)