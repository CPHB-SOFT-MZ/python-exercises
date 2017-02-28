import timeit
int_list = list(range(1, 1000001))
print(min(int_list))
print(max(int_list))

sum_result = (int_list[-1] + 1) * len(int_list) / 2
# print(timeit.timeit("sum(range(1,1000001))"))
# t = timeit.Timer("sum(int_list)", setup="int_list = list(range(1,1000001))")
# print(t.timeit())

x = timeit.Timer("(int_list[-1] + 1) * len(int_list) / 2", setup="int_list = list(range(1,1000001))")
print(x.timeit())
print(sum_result)
print(sum(int_list))

uneven_int_list = list(range(1, 20, 2))
print(uneven_int_list)

multiply_by_3 = [value * 3 for value in range(3, 30)]
print(multiply_by_3)

cubes = [value ** 3 for value in range(1, 10)]

print(cubes)
