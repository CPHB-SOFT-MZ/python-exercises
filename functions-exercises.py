
def print_list(li):
    if len(li) == 1:
        print(li[0])
        return
    print(li[0])
    print_list(li[1:])

l = list(range(0, 10))
print_list(l)
