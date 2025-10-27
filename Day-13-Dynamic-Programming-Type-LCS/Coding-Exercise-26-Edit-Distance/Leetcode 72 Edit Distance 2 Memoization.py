def minDistance(word1, word2):
    n = len(word1)
    m = len(word2)
    arr=[[-1]*m for _ in range(n)]
    def helper(index1,index2):
        #base condition
        if index1<0: return index2+1
        if index2<0:return index1+1
        #if index1 <0 and index2<0:return 0
        if arr[index1][index2] != -1:
            return arr[index1][index2]
        if word1[index1]==word2[index2]:
            arr[index1][index2] = helper(index1-1,index2-1) 
            return arr[index1][index2]
        #replace
        replace = 1 + helper(index1-1,index2-1)
        #delete
        delete = 1 + helper(index1-1,index2)
        #insert
        insert = 1 + helper(index1,index2-1)
        arr[index1][index2]= min(replace,delete,insert)
        return arr[index1][index2]
    return helper(n-1,m-1)   

print(minDistance("hodse", "dos"))
