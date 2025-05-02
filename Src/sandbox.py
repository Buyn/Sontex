a = [None, None, [1, 2 ,4, 5,7] ,[3, 2 ,4, 5,7] , [1, 2 ,4, 5,7], None , [1, 2 ,4, 5], None]
# print([x for lst in a if lst for x in lst ])
b = set([x for lst in a if lst for x in lst ])
# print(set(zip([x for x in a if x])))
# b = set()
# for l in [x for x in a if x]:
# for l in filter(lambda i: True if i else False, a):
#     b.update(l)
# b = sum([x for x in a if x])
print(b)
