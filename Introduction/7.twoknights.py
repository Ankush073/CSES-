def comb (n,r):
      return (n*(n-1))/2
k=int(input())
print(0)
if(k>1): print(6)
x=3
prev1=0
prev2=0
while(x<=k):
      num=comb(x**2,2)
      prev2+=8
      prev1+=prev2
      ans=num-(prev1)
      x+=1
      print(int(ans))
      
      
