# -*- coding: UTF-8 -*-
'''
@author: TangRen
@time: 2019/12/31
@file: __init__.py.py
@desc: 

'''

if __name__ == '__main__':
    num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    num_list_new = [str(x) for x in num_list]

    print(",".join(num_list_new))