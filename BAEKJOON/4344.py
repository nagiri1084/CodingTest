count = int(input())
avgup = [] #비율 저장할 배열
for i in range(count):
    score = list(map(int, input().split())) #점수 입력
    #avg =0 #평균 저장할 정수
    k=0 #평균 넘는 점수 수 저장 정수
    #avg = (sum(score)-score[0])/score[0] #평균 구하기
    a = score.pop(0)
    avg = sum(score)/a

    for j in range(a):
        if score[j] > avg:
            k += 1
            
    avgup.append(k/a*100) #비율 구하기
    #print(f"{avgup[i]:.3f}%")

for i in range(count):
    print(f"{avgup[i]:.3f}%")

# 소수점 자리수 표기 방법
# round(실수, 표기할 자리 수): 소수점 자리수 지정
# f-string: f"{실수:.표기할 자리수f}" 
# format(): "{index:.표기할 자리수f}".format(실수)
# format(실수, ".표기할 자리수f")