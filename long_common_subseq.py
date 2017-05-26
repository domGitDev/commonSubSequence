
def common_subseq_matrix(array_x, array_y):
    
    m = len(array_x)
    n = len(array_y)
    common = (m+1) * [[0] * (n+1)]
    
    for i in xrange(1, m+1):
        for j in xrange(1, n+1): 
            if array_x[i-1] == array_y[j-1]:
                common[i][j] = common[i-1][j-1] + 1
            else:
                common[i][j] = max(common[i-1][j], common[i] [j-1])
    return common


def get_long_common_subseq(array_x, array_y):
    m = len(array_x)
    n = len(array_y)
    
    i = m
    j = n
    common = common_subseq_matrix(array_x, array_y)
    size = common[m][n]
    common_vals = [None] * (size+1)
    
    while i > 0 and j > 0:
        if array_x[i-1] == array_y[j-1]:
            common_vals[size-1] = array_x[i-1]
            i -= 1
            j -= 1
            size -= 1
        elif common[i-1][j] > common[i][j-1]:
            i -= 1
        else:
            j -= 1
        
    res = [str(x) for x in common_vals if x is not None]  
    print '\n' 
    print ' '.join(res)
    return len(res)
    
    

