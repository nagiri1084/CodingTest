a=int(input())
b=int(input())
x=b//100
y=b%100//10
z=b%10

z=a*z
print(z)
y=a*y
print(y)
x=a*x
print(x)

print(z+y*10+x*100)