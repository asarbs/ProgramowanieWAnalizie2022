import random

l1 = random.sample(range(10, 100), 10)
l2 = random.sample(range(60, 160), 15)

print('l1={}'.format(l1))
print('l2={}'.format(l2))

#zad 5a
z5a = l1 + l2
print(u'l1 + l2 = {}'.format(z5a))

#zad5b
z5b = list(set(l1) - set(l2))
print(u'l1 - l2 = {}'.format(z5b))

#zad5c
z5c = list(set(l2) - set(l1))
print(u'l2 - l1 = {}'.format(z5c))

#zad5d
z5d = []
for x in z5a:
    if x in l1 and x in l2:
        z5d.append(x)
print(u'l2 * l1 = {}'.format(z5d))

#zad53 https://pl.wikipedia.org/wiki/R%C3%B3%C5%BCnica_symetryczna_zbior%C3%B3w
z53 = (z5b) + (z5c)

print(u'l2 ∸ l1 = {}'.format(z5d))

#zad5f
print('max(l1)={}, max(l2)={}, max(l1 + l2)={}'.format( max(l1), max(l2), max(z5a) ))

#zad5g
l2.append(l1[0])
del(l1[0])
print('new l1 = {}, new l2 = {}'.format(l1, l2))

#zad5h
l2.extend(l1)
print(l2)

#zad5i
l1.clear()
l2.clear()
print("l1 = {}, l2={}".format(l1, l2))