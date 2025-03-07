# -*- coding: utf-8 -*-
"""
@Time ： 2025/2/16 22:14
@Auth ： liyaya
@File ：test.py
@IDE ：PyCharm

"""
original_list = [3, 1, 2, 1, 3, 2]

# 使用 enumerate 获取每个元素的索引，然后通过 sorted 进行排序
sorted_list = sorted(enumerate(original_list), key=lambda x: (x[1], x[0]))

# 只取排序后的值
sorted_values = [item[1] for item in sorted_list]
print(sorted_values)
