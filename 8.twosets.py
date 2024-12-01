n=int(input())
sum=n*(n+1)/2
arr1=[]
arr2=[]
if(sum%2==0):
      if(n%2==0):
            arr1.append(1)
            for i in range(4,n,2):
                  arr1.append(i)
            arr1.append(n-1)
            arr2.append(2)
            for i in range(3,n-2,2):
                  arr2.append(i)
            arr2.append(n)         
      else:   
            arr1.append(1)
            for i in range(2,n-1,2):
                  arr1.append(i)
            arr1.append(n)
            for i in range(3,n-1,2):
                  arr2.append(i)
            arr2.append(n-1)   
      print("YES") 
      print(len(arr1))
      for i in range (len(arr1)):
            print(arr1[i], end=" ")
      print()
      print(len(arr2))
      for i in range (len(arr2)):
            print(arr2[i],end=" ")        
else:
      print("NO")


      
