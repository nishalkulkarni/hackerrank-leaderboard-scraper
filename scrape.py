from collections import Counter 
mp = dict()
for i in range(121):
    name = input().strip()
    score = float(input().strip())

    if name in mp:
        mp[name] += score
    else:
        mp[name] = score

# print(mp)
k = Counter(mp) 
high = k.most_common(55) 

# for i in high: 
#     print(i[0]," :\t\t",i[1]," ") 

o = 1
for i in high:
    print(i[0]," --> ",i[1])
print(len(mp))
