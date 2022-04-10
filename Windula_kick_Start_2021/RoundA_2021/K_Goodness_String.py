num = int(input())                  # num = number of cases
for j in range(0,num):
    N,K = map(int,input().strip().split())          # N = string length, K = given goodness score
    S = list(input())              # S = string list
    #print("num:{} j:{} N:{} K:{} S:{}".format(num,j,N,K,S))
    imax = int(N // 2)                               # imax = maximum index, imin = minimum index = 0
    CalK = 0                                    # CalK = calculated goodness score
    for i in range(0,imax):
        SBegin = S[i]                               # element from begin
        SEnd = S[N - i - 1]                         # element from end
        if(SBegin != SEnd):
            CalK = CalK + 1
    NumOper = abs(int(K - CalK))                         # number of operations
    print("Case #{}: {}".format(j + 1,NumOper))
