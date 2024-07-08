d = 11
b = format(d, 'b')
print(b)
g = []
g.append(b[0])
f = b[0]
for i in range(1, len(b)):
    s = b[i]
    g.append(str(int(f) ^ int(s)))
    f = b[i]

final_answer = ''.join(g)
print(final_answer)
