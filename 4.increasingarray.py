n=int(input())
num=list(map(int,input().strip().split()))[:n]
sum=0
num1=num[0]
for i in range (1,n):
      num2=num[i]
      if(num1>num2):
            diff=num1-num2
            sum+=diff
            num2=num[i]
      else:
            num1=num[i]
print(sum)