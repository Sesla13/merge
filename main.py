def merge(*lists):
    new_one = []
    for i in range(len(lists)):
        new_one += lists[i]
    new_one.sort()
    return print(new_one)
