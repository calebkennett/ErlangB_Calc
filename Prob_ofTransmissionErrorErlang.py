def factorial(n):
    if n <= 1:
        factn = 1
    else :
        
        factn = n * factorial(n-1)
    return factn


##################################################
#  A is traffic, N is Nc(number of channels)

# same as erlangB
def Erlang(A, N):
    L = (A**N / factorial(N)) 
    sum_ = 0
    for i in range(N):
        sum_ += (A**i) / factorial(i)
    return (L / (sum_ + L))
