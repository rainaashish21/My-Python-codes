def fib(n):
    if n<=0:
        return[]
    if n==1:
        return[0]
    seq=[0,1]
    for i in range(2,n+1):
        next_term = seq[i-1]+seq[i-2]
        seq.append(next_term)
    return seq
    
print(fib(6))