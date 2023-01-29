n = int(input()) # get input
a = list(map(int,input().split())) # An
position = 0 # current position

while True:
    # go right
    while position < n: # while we can go right, go right
        print('R',end='')
        a[position]-=1
        position+=1
    while position > 0 and (a[position-1] != 1 or a[position:n]==[]): # while we can go left, go left
                            # if after we go left we cant go back and we arent finished, we cant go left
        print('L',end='')
        position-=1
        a[position]-=1
        if a[n-1]==0: n-=1 # if we are finished with it, decrease length
    if n == 0: break # we are finished with everything

print() # finishing newline
