from itertools import* # Import everything from itertools. We will only be using product though
                       # You can change this to from itertools import product. 

def v(c,F):            # returns whether a set of conFiguration is valid for a set of Cows. 
    S=[0]*100          # Stalls. 
    for f in F:        # Calculate the new temperature
        for i in range(f[0]-1,f[1]):S[i]+=f[2]
    for C in c:
        for i in range(C[0]-1,C[1]):
            if S[i]<C[2]:return 0 # If not valid return 0
    return 1 # Else return 1

_=lambda:[*map(int,input().split())] # Get a list of integer inputs
Z=lambda x:sum([_[3]for _ in x])     # the cost of a configuration

n,m=_()              # Read input
c=[_()for x in[0]*n]
a=[_()for x in[0]*m]

F=[[a[X]for X in range(m)if _[X]]for _ in product([0,1],repeat=m)] # Find the set of all 0110 binary strings
                                                                   # and map to configuration
C=[Z(_)for _ in F if v(c,_)]                                       # calculate Cost

print(min(C)) # minimum Cost
