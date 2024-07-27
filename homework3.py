def print_params(a = 1, b = 'строка', c = True):
    print (a, b, c)


print_params(b = 25)
print_params(c = [1,2,3])

values_list = (2, 'ммм', False)
values_dict = {'a': 3, 'b': 'длина', 'c': True}

print_params (*values_list)
print_params (**values_dict)

values_list_2 = (2, 4.1)
print_params(*values_list_2,42)