global a

global b

global c

ls = [[0, 2], [2, 4], [4, 6], [6, 8], [8, 10], [1, 0], [3, 1], [5, 2], [7, 3], [9, 4]]
re_a = []
re_b = []
re_c = []
def sonsil(a,b,c):
    re_ls = []
    for i in range(10):
        re_ls.append(((a*(ls[i][0])**2+b*ls[i][0]+c)-(ls[i][1]))**2)
    return (sum(re_ls)/10)**0.5

def d(x, y, z):
    delta = 0.00000001
    a = x
    b = y
    c = z
    f1 = sonsil(a,b,c)
    a += delta
    f2 = sonsil(a,b,c)
    a -= delta
    b += delta
    f3 = sonsil(a,b,c)
    b -= delta
    c += delta
    f4 = sonsil(a, b, c)
    c -= delta
    return [(f2-f1)/delta, (f3-f1)/delta, (f4-f1)/delta]

stepsize = 0.001

for x in range(-5,-4):
    for y in range(1,2):
        for z in range(1,2):

            a = x
            b = y
            c = z
            test = 0
            while (sum(list(map(abs, d(a, b, c)))) / 3 > 0.000001):
                if test > 1500000:
                    break
                test += 1
                print((a, b, c ,sonsil(a, b, c)))
                a = a - d(a, b, c)[0] * stepsize
                b = b - d(a, b, c)[1] * stepsize
                c = c - d(a, b, c)[2] * stepsize
            print((a, b, c, sonsil(a, b, c)))
            if test <= 1500000:
                re_a.append(round(a, 3))
                re_b.append(round(b, 3))
                re_c.append(round(c, 3))
re_a = list(set(re_a))
re_b = list(set(re_b))
re_c = list(set(re_c))

print(re_a,re_b,re_c,test)
