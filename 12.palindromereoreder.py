def rev(str):
      return str[::-1]
str=input()
l=len(str)
ans=""
odd=""
cnt=0
dic={}
for i in range (l):
      if str[i] in dic.keys():
            dic[str[i]]+=1
      else:
            dic[str[i]]=1
for x,y in dic.items():
      if(y%2==0):
            for i in range (int(y/2)):
                  ans+=x
      else:
            cnt+=1
            odd=x
if(cnt>1):
      print("NO SOLUTION")
else:
      dummy=ans
      ans+=odd
      revs=rev(dummy)
      ans+=revs
print(ans)

