def toh(N, fromm, to, aux):
    count = 0
    def helper(N,fromm,to,aux):
        nonlocal count
        if N==1:
            count+=1
            print("move disk " + str(N) + " from rod " + str(fromm) + " to rod " + str(to))
            return
        helper(N-1,fromm,aux,to)
        count+=1
        print("move disk " + str(N) + " from rod " + str(fromm) + " to rod " + str(to))

        helper(N-1,aux,to,fromm)
    helper(N,fromm,to,aux)  
    return count
print(toh(3, 1, 3, 2))