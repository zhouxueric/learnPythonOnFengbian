import re
import time


def waiting(times=6):
    # 制造等待效果
    for i in range(times):
        time.sleep(0.5)
        print('·')


def delay_print(content, delay=0.5):
    # 延迟输出
    time.sleep(delay)
    print(content)


def choice_fortune(key):
    # 抽签函数
    # encoding = '{{encoding}}'
    # 什么意思？起什么作用吗？
    # print(encoding)

    # if 'encoding' in encoding:
    #     encoding = str(key.encode('utf8'))
        # 转成UTF8编码
        # print(encoding)
    # 换成下面一行会怎样？
    encoding = str(key.encode('utf8'))

    fortune_pool = ['升职', '考神', '暴富', '变瘦', '涨薪', '自由', '健康', '脱单']
    lucky_number = 0
    nums = re.findall('\d+', encoding)
    # 将16进制数中的数字筛选出,效果为去掉特殊字符
    # print(nums)

    for num in nums:
        lucky_number += int(num)
    # print(lucky_number)
    lucky_number += len(key)
    # print(lucky_number)
    lucky_number %= len(fortune_pool)
    # 求余数
    # print(lucky_number)

    return fortune_pool[lucky_number]


def main():
    # 个人信息
    name = '二师兄'
    gender = '男猴子'
    browser = '西天浏览器'
    address = '大唐'
    ip_address = '112.10.232.23'

    # 开头
    print('亲爱的{name}，预示你未来的新年签正在抽取'.format(name=name))
    waiting()

    # 抽签过程
    delay_print('我已经知道你是个有佛运的{gender}，'.format(gender=gender))
    waiting(3)
    delay_print('你所用的{browser}让我们相遇，'.format(browser=browser), delay=2)
    waiting(3)
    delay_print('现在根据你的地址{address}、IP{ip_address}，与你的2020产生感应'.format(address=address, ip_address=ip_address), delay=2)
    waiting()

    # 抽签
    seed = name + gender + browser + address + ip_address
    # print(seed)
    fortune = choice_fortune(seed)
    # print(fortune)

    # 抽签结果
    delay_print('恭喜你，你的2020年专属幸运签已生成！这是你的新年关键词：{fortune}'.format(fortune=fortune), delay=2)

    # 本地执行需要请求图片
    try:
        from urllib.parse import quote
        from urllib.request import urlretrieve
        from urllib.error import HTTPError
        import os
        import platform
    except ImportError:
        pass
    else:
        filename = '新年幸运签.png'
        img_source = quote(fortune, encoding="GBK")
        # print(img_source)
        try:
            urlretrieve('https://res.pandateacher.com/{img_source}.png'.format(img_source=img_source),
                        filename=filename)
        except HTTPError:
            print('该幸运签不存在或网络异常,请稍后重试！')
            exit()
        if 'windows' in platform.platform().lower():
            os.system(filename)
        else:
            os.system('open {filename}'.format(filename=filename))


if __name__ == '__main__':
    main()

# 分解
# from urllib.parse import quote
# from urllib.request import urlretrieve
# import os
# import platform
# fortune_pool = ['升职', '考神', '暴富', '变瘦', '涨薪', '自由', '健康', '脱单']
# filename = '新年幸运签.png'
# for s in fortune_pool:
#     img_source = quote(s, encoding="GBK")
#     print(img_source)
#     urlretrieve('https://res.pandateacher.com/{img_source}.png'.format(img_source=img_source))
#     # 返回的全是考神
#     if 'windows' in platform.platform().lower():
#         os.system(filename)
#     else:
#         os.system('open {filename}'.format(filename=filename))