def sum__list(angka):
    if not angka:
        return 0
    else:
        return angka[0] + sum__list(angka[1:])

my_list = [1, 2, 3, 4, 5]
print(sum__list(my_list))
