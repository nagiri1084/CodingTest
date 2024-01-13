addNum = int(input())
newAddNum = 100
firstNum = 0
secondNum = 0
roofNum = 0
result = addNum

def calc1(num1):
    num1 = num1//10
    return num1

def calc2(num2):
    num2 = num2%10
    return num2

if(addNum<10):
    firstNum = 0
    secondNum = addNum
else:
    firstNum = calc1(addNum)
    secondNum = calc2(addNum)

while(addNum != newAddNum):
    result = firstNum + secondNum
    newAddNum = str(secondNum) + str(calc2(result))
    newAddNum = int(newAddNum)
    firstNum = calc1(newAddNum)
    secondNum = calc2(newAddNum)
    roofNum+=1
    
print(roofNum)

# ---------------더 짧은 다른 사람 풀이---------------

N = int(input())

cur_num = N
repeated = 0

while True:
    repeated += 1
    cur_num = cur_num % 10 * 10 + sum(map(int, str(cur_num)))%10
    if N == cur_num:
        print(repeated)
        break