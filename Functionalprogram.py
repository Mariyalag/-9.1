def apply_all_func(int_list, *functions):
    result = {}
    for func in functions:
        result[func.__name__] = func(int_list)
    return result


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))








# def get_russian_names():
#     print(['Ваня', 'Коля', 'Маша',])
#
# get_russian_names()
# print(type(get_russian_names))
# print(get_russian_names.__name__)

# пример 2
# def get_russian_names():
#     return ['Ваня', 'Коля', 'Маша',]
# print(get_russian_names.__name__)
# my_func = get_russian_names
# print(my_func())
# print(my_func.__name__)


# пример 3
# def get_russian_names():
#     return ['Ваня', 'Коля', 'Маша',]
#
# def get_british_names():
#     return ['Oliver', 'Jack', 'Harry',]
#
# name_getters = [get_russian_names, get_british_names]
#
# for name_getter in name_getters:
#
#     print(name_getter())

# пример 4

#
# def adder(args):
#     res = 0
#     for number in args:
#         res += number
#     return res
#
# def multiplier(args):
#     res = 1
#     for number in args:
#         res *= number
#     return res
#
# def process_numbers(numbers, function):
#     result = function(numbers)
#     print(f'Получилось {result}')
#
#
# my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
# process_numbers(numbers=my_numbers, function=adder)
# process_numbers(numbers=my_numbers, function=multiplier)

# пример 5
# def mul_by_2(x):
#     return x * 2
#
# my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
#
# result = map(mul_by_2, my_numbers)
# print(result)
# print(list(result))

# пример 6
# def is_odd(x):
#     return x % 2
#
# my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
#
# result = filter(is_odd, my_numbers)
# print(result)
# print(list(result))

