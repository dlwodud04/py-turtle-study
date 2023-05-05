#%%
bts = ["슈가",174,57,
       "지민",173,58,
       "제이홉",177,59,
       "진",179,61,
       "뷔",180,60,
       "정국",178,65,
       "RM",181,70]

def BTS_sort(x,y) :
    if y == "name" :
        y = bts[::3]
    elif y == "height" :
        y = bts[1::3]
    elif y == "weight" :
        y = bts[2::3]
    else :
        y = None
    return y

bts_name = BTS_sort(bts,"name")
print("bts_name : ", bts_name)
bts_height = BTS_sort(bts,"height")
print("bts_height : ", bts_height)
bts_weight = BTS_sort(bts,"weight")
print("bts_weight : ", bts_weight)
bts_age = BTS_sort(bts,"age")
print("bts_age : ", bts_age)