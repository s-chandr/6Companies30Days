def encode(arr):
    temp = " "
    count = 0 
    ans = ''
    for i in range(len(arr)):
        if temp != arr[i]:
            ans+=temp
            ans+=str(count)
            temp = arr[i]
            count = 1
            
        else :
            count +=1 
    ans+=temp
    ans+=str(count)
    return ans[2:]
  
