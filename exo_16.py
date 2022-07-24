set1={2,4,2,"True",None,"Lime"}
set2={3,8,4,9}
def exist(a,set_2):
    if a in set_2:
        return True
    else:
        return False

print(exist(2,set1))
print(exist(10,set2))