if __name__=="__main__":
  
  L=[

  for i in range(len(L)):
    for j in range(len(L[0])):
      
      if(L[i][j]==1):
        L[i][j]=0
      else:
        L[i][j]=1
  
  print(L)