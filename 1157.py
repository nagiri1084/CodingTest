word = input().lower()      # word = mississipi / baaa
word_list = list(set(word)) # word_list = ['m','i','s','p'] / ['b','a']
cnt = []

for i in word_list:         # i = m, i, s, p / b, a
    count = word.count(i)
    cnt.append(count)       # cnt = [4, 4, 1, 1] / [1, 3]

if(cnt.count(max(cnt))) >= 2:
    print("?")
else:
    print(word_list[(cnt.index(max(cnt)))].upper())


#**변수 설정**
#변수 word를 설정하고 lower()을 이용해서 입력받은 문자열을 소문자로만 입력받고 이것은 **set()**을 이용해서 자료형의 중복으로 제거한 뒤 list()로 묶는다
#cnt 변수를 [] 리스트로 초기화해서 변수 설정한다.
#**
#문자 수 세기**
#word 변수에서 특정 문자가 몇 개 있는지 count()를 이용해서 세고, cnt 변수 리스트에 append 추가해준다.
#
#**조건 설정**
#if문을 사용해서 cnt 변수 리스트에 가장 큰 값 max(cnt)를 count()함수를 이용해서 센 개수가 cnt 변수 리스트 안에 2개 이상이라면 "?"를 출력하는 조건을 만족해준다.
#
#
#set() 자료형의 중복을 제거하기 위한 필터(리스트나 배열 등에 동일한 요소 제거)
#count() 리스트 안에 x요소가 몇 개 있는지 조사하여 그 개수를 반환해주는 함수: 리스트.count(x)
#index() 리스트 안에 x요소가 어느 위치에 있는지 Index 값 반환 함수: 리스트.index(x)