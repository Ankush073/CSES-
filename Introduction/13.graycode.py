def decimaltobinary(n):
      binary=''
      while(n>0):
            binary=str(n%2)+binary   
            n=n//2
           
      return binary 
n=int(input())
num=2**n
for i in range (num):
      ans=decimaltobinary(i)
      print(ans.zfill(n))
