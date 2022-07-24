def sous_ens(set1,set2):
    if set1.issubset(set2):
        return True
    else:
        return False

print(sous_ens({1,2,3},{1,2,3,"La",3,9,0}))
print(sous_ens({1,2},{5,6,7}))