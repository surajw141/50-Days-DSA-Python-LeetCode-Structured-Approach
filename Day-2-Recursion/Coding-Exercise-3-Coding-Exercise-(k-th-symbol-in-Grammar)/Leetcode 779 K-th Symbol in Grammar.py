#(k-th symbol in Grammar)
# We build a table of n rows (1-indexed). We start by writing 0 in the 1st row. Now in every subsequent row, we look at the previous row and replace each occurrence of 0 with 01, and each occurrence of 1 with 10. For example, for n = 3, the 1st row is 0, the 2nd row is 01, and the 3rd row is 0110. Given two integer n and k, return the kth (1-indexed) symbol in the nth row of a table of n rows.
def kth_symbol(n, k):
    #0
    #01
    #0110
    #base case
    if n == 1: return 0
    length = 2**(n-1)
    mid = length//2
    if k <= mid:
        return kth_symbol(n-1, k)
    else:
        return int(not kth_symbol(n-1, k-mid))
        #return 1 - kth_symbol(n-1, k-mid) 1-0 = 1, 1-1 = 0
print(kth_symbol(4, 5))