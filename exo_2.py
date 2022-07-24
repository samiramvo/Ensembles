def iterate(*ensemble):
    for i in ensemble:
        print(i)
print(iterate([1,3,4]))
print(iterate((1,2,7,9)))
print(iterate({2,6,"dali"}))