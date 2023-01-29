# Unfortunately, I decided to golf this one
# Read and edit at your own risk


c=[]
i=int
I=input
n=i(I())
s=input()
e=[*map(i,I().split())]
g,h=map(s.index,'GH')
G='G'in s[e[g]:]
H='H'in s[e[h]:]
if~-G:c+=[(s[_]=='H')*e[_]>g for _ in range(g)]
if~-H:c+=[(s[_]=='G')*e[_]>h for _ in range(h)]
_=~-(G|H)
c=sum(c)-_
if _&(g<h&e[g]>h|h<g&e[h]>g):c-=2
print(c)

# Explanation

c=[]    <-- Counter
i=int   |_ Shorthands
I=input |
n=i(I())  <-- read n
s=input() <-- read s
e=[*map(i,I().split())] <-- Read e, a list of integers
g,h=map(s.index,'GH')   <-- g is the first occurance of "G"
G='G'in s[e[g]:]        <-- G is if there are "G"s after g's range (i.e. g is not a leader of all following G's)
H='H'in s[e[h]:]        <-- same for H
A: if~-G:c+=[(s[_]=='H')*e[_]>g for _ in range(g)] <-- if not G, g is a leader
             if it is H and g is in its range, store a 1, else 0
B: if~-H:c+=[(s[_]=='G')*e[_]>h for _ in range(h)] <-- same for H
_=~-(G|H) <-- G|H is G or H. ~-x is 0 if x is True else -1. 
C: c=sum(c)-_ count is how many 1s occured. if not (g not leader or h not leader), subtract -1 (i.e. add 1). 
                                            |-- i.e. g is leader and h is leader
if _&(g<h&e[g]>h|h<g&e[h]>g):c-=2 --> if we have double counted the pair (g, h), 
                                      subtract 2 because we counted it once in A, once in B, and once in C
print(c) <-- output count
