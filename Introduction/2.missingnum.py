n=int(input())
str=input().split()
sum=0
for i in range (len(str)):
      if(str[i]==' '):
            continue
      num=int(str[i])
      sum+=num
print(int((n*(n+1)/2)-sum))





