import numpy as np

list1 = [90,92,97,94,98,]
list2 = [94,98,95,91,99]

#合并列表
list3 = list1 + list2
print(list3)
#排序
list3.sort()
print(list3)

#筛选
list4 = np.array(list3)
print(list4[list4 < 95])

