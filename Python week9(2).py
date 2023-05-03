#%%
List = ['F','B','C','A','E','D']

List = List[::-1]
print(List)
List = List[1:5]
print(List)
List = List[-2::-1]
print(List)
List.sort(reverse = True)
print(List)
List.append('G')
print(List)
List.sort()
print(List)