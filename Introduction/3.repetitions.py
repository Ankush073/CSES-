str=input()
maxans=1
ans=1
for i in range(len(str)-1):
      if(str[i]==str[i+1]):
            ans+=1
      else:
            if(ans>maxans):
                  maxans=ans
            ans=1
if(ans>maxans):
      maxans=ans
if(maxans==1):
      print(ans)
else:
      print(maxans)
      

