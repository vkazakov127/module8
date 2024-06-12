# -*- coding: utf-8 -*-

def add_everything_up(a,b):
    try:
        c = a + b
    except TypeError as exc:
        Descr = ''
        for arg in exc.args:
            Descr += arg
        print('-----------------------------------------------')
        print(f'Исключение : {exc}. \nПодробности: {Descr}')
        print(f'Операция в виде слияния строк:')
        c = str(a) + str(b)
    else:
        print('-----------------------------------------------')
        print('Операция успешна:')
        return c
    finally:
        return c

print(f'add_everything_up(2,5) = {add_everything_up(2,5)}')
print(f'add_everything_up(2,"5") = {add_everything_up(2,"5")}')
print(f'add_everything_up(3.5," кота") = {add_everything_up(3.5," кота")}')
print(f'add_everything_up(4.5, False) = {add_everything_up(4.5, False)}')
print(f'add_everything_up(2.5, True) = {add_everything_up(2.5, True)}')
print(f'add_everything_up(2.5, ["кошка","собака","попугай"]) = {add_everything_up(2.5, ["кошка","собака","попугай"])}')
print(f'add_everything_up(1.5, ("яблоко","морковь","огурец")) = {add_everything_up(2.5, ("яблоко","морковь","огурец"))}')
