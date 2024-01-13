subjectNum = int(input())
score1 = list(map(int, input().split()))
max = max(score1)

avg = 0
for i in range(len(score1)):
    score1[i] = score1[i]/max*100
    avg += score1[i]

print(avg/len(score1))

#list(map(int, input().split())) 입력 받은 수를 나누어 저장
#
#한 번에 두 개 이상의 값을 입력받는 방법(map, split 함수 )
#
#map() :: map(사용할 함수, 사용할 자료형) 시퀀스의 각 요소(리스트, 배열, 문자열, 숫자 등)를 함수에 적용해서 새로운 리스트로 저장
#
#split() " "공백을 기준으로 나누어 값을 연속적으로 입력받음