# This one is trivial

for _ in range(int(input())):
    s=input()
    l=len(s)  # input and length of input
    if not s[1:-1].count('O'):print(-1) # impossible, no middle O
    elif 'MOO'in s:print(l-3) # contains MOO, remove all other letters
    elif 'OOO'in s:print(l-2) # no MOO but OOO, remove all other letters and change O to M
    elif 'MOM'in s:print(l-2) # similar
    elif 'OOM'in s:print(l-1) # similar
