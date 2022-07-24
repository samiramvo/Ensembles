set1={2,4,2,"True",None,"Lime"}
set2={3,8,4,9}
set3={1,2}
def elmnt_com(set1,set2):
    if set1.isdisjoint(set2):
        return True
    else:
        return False

print(elmnt_com(set1,set2))
print(elmnt_com(set2,set3))