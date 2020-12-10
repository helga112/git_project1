a = input()
a = a.split()
b = []
for i in a:
    if i == '-':
        c = b[-1]
        d = b[-2]
        del b[-1]
        del b[-1]
        b.append(d - c)
    elif i == '+':
        c = b[-1]
        d = b[-2]
        del b[-1]
        del b[-1]
        b.append(c + d)
    elif i == '*':
        c = b[-1]
        d = b[-2]
        del b[-1]
        del b[-1]
        b.append(c * d)
    elif i == '~':
        c = b[-1]
        del b[-1]
        b.append(c * -1)
    elif i == '/':
        c = b[-1]
        d = b[-2]
        del b[-1]
        del b[-1]
        b.append(d // c)
    elif i == '!':
        c = b[-1]
        del b[-1]
        for j in range(1, c):
            c = c * j
        b.append(c)
    elif i == '#':
        c = b[-1]
        b.append(c)
    elif i == '@':
        c = b[-1]
        d = b[-2]
        y = b[-3]
        del b[-1]
        del b[-1]
        del b[-1]
        b.append(c)
        b.append(d)
        b.append(y)
    if i != '-' and i != '+' and i != '*' and i != '#' and i != '@' and\
       i != '~' and i != '/' and i != '!':
        b.append(int(i))
print(b[0])