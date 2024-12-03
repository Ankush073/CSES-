n=int(input())
total_sum=n*(n+1)//2
maxele=n
set1=[]
set2=[]
vis=[False]*(n+1)
set1sum=0
if(total_sum%2==0):
      print("YES")
      while(set1sum<(total_sum//2)):
            remaining=total_sum//2-set1sum
            if(remaining>maxele):
                  set1.append(maxele)
                  vis[maxele]=True
                  set1sum+=maxele
                  maxele-=1
            else:
                  set1.append(remaining)
                  vis[remaining]=True
                  set1sum=total_sum//2
      for i in range (1,n+1):
            if(vis[i]==False):
                  set2.append(i)
      print(len(set1))
      for i in range(len(set1)):
            print(set1[i],end=" ")
      print()
      print(len(set2))
      for i in range(len(set2)):
            print(set2[i],end=" ")

            
else:
      print("NO")

