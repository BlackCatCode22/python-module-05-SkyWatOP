fname = input('Enter File: ')
if len(fname) < 1 : fname = 'clown.txt'
hand = open(fname)

many = dict()
for lin in hand:
    lin = lin.rstrip()
    # print(lin)
    wds = lin.split()
    # print(wds)
    for w in wds:
        many[w] = many.get(w,0) + 1

# Find the top 5 word by freq

tmp = dict()
newList = list()
for k,v in many.items():
    tup = (v,k)
    newList.append(tup)

cool = sorted(newList, reverse=True)

for v,k in cool[:5] :

    print(k,v)

