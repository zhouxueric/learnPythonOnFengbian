import re

target = '''
'abc','acc','adc','aec','afc','abd','acd','add'
'''
print(re.findall('a[bc]d',target))                    #匹配abd或acd
print(re.findall('a[b-f]d',target))                   #匹配中间的b到f
print(re.findall('a[^c-f]d',target))                   #匹配中间 不是 c到f
