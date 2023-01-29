# input

n = int(input())

directions = [] # store directions, cows, cost
cows = [
    [1 for _ in range(n)] + [0]
    for _ in range(n)
] + [[0 for _ in range(n+1)]]
cost = [
    [0 for _ in range(n)] for _ in range(n)
]

for i in range(n):
    line = input().split()
    directions.append(list(line[0]))
    cost[i].append(int(line[1]))

cost.append(list(map(int,input().split()))+[0])

# calculate how many cows pass through where

for i in range(n):
    for j in range(n):
        if directions[i][j] == 'R':
            cows[i][j+1] += cows[i][j]
        else:
            cows[i+1][j] += cows[i][j]

# calculate sum
            
sum = 0

for i in range(n):
    # consider row n, column i
    sum += cows[n][i] * cost[n][i]
    sum += cows[i][n] * cost[i][n]

# print(cows)
# print(directions)

# print sum

print(sum)

for i in range(int(input())):
    i, j = map(int,input().split()) # input
    i-=1;j-=1
    if directions[i][j]=='R': _='D' # get before and after
    else:                     _='R'

    ammount = cows[i][j]

    I=i;J=j

    # subtract before
    
    while I<n>J:
        if directions[I][J]=='R': J+=1
        else: I+=1
        cows[I][J]-=ammount

    directions[i][j]=_
    
    # add after

    I=i;J=j

    while I<n>J:
        if directions[I][J]=='R': J+=1
        else: I+=1
        cows[I][J]+=ammount

    # calculate and print sum

    sum = 0

    for i in range(n):
        # consider row n, column i
        sum += cows[n][i] * cost[n][i]
        sum += cows[i][n] * cost[i][n]

    print(sum)
