
s = "abbcdeacb"

list=[]
list[:0] = s
m = {}
for i in list:
    m[i] = 1 if m.get(i)==None else m[i]+1

for i in m.keys():
    print(i,m.get(i))