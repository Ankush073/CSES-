t=int(input())
while(t!=0):
      first=0
      num=list(map(int,input().strip().split()))[:2]
      row=num[0]
      col=num[1]
      if(row>=col):
            if(row%2==0):
                  first=row**2
                  print(first-(col-1))
            else:
                  first=(row-1)**2+1
                  print(first+(col-1))
            
            
      else:
            if(col%2==0):
                  first=(col-1)**2+1
                  print(first+(row-1)) 
                  
            else:
                  first=col**2
                  print(first-(row-1)) 
                    
      t-=1
