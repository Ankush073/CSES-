n=int(input())
if(n==2 or n==3):
      print("NO SOLUTION")
elif(n==1):
      print(1)
else:
      arr=[]
      for i in reversed(range(2,n,2)):
            arr.append(i)
      arr.append(n)
      for i in range(1,n,2):
            arr.append(i)
      print(*arr)


