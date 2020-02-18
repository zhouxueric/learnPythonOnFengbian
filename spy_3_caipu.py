import requests
from bs4 import BeautifulSoup

url = 'http://www.xiachufang.com/explore/'
res = requests.get(url)
print(res.status_code)
html = res.text
soup = BeautifulSoup(html,'html.parser')
info = soup.find_all(class_="info pure-u") #.find_all结果可以按列表方式进行下标[0]操作
for item in info:
    name_a = item.find('a') #item.find(class_="name").find('a')
    name_url = url[:-1] + name_a['href']
    name = name_a.text.split()[0]  #去空格，取第0个元素  .split()[0] | [17:-13]
    inglist = item.find('p',class_="ing ellipsis") #'span'
    # print(inglist)
    # li = []
    # for food in inglist:
    #     li.append(food.text) 
    #.text可以向下穿透,读取元素内所有text
    li = inglist.text
    print(name,li,name_url)


# 获取数据
res_foods = requests.get('http://www.xiachufang.com/explore/')
# 解析数据
bs_foods = BeautifulSoup(res_foods.text,'html.parser')

# 查找包含菜名和URL的<p>标签
tag_name = bs_foods.find_all('p',class_='name')
# 查找包含食材的<p>标签
tag_ingredients = bs_foods.find_all('p',class_='ing ellipsis')
# 创建一个空列表，用于存储信息
list_all = []
# 启动一个循环，次数等于菜名的数量
for x in range(len(tag_name)):
    # 提取信息，封装为列表。注意下面[18:-14]切片和之前不同，是因为此处使用的是<p>标签，而之前是<a>
    list_food = [tag_name[x].text[18:-14],'http://www.xiachufang.com'+tag_name[x].find('a')['href'],tag_ingredients[x].text[1:-1]]
    # 将信息添加进list_all
    list_all.append(list_food)
# 打印
print(list_all)

# 以下是另外一种解法

# 查找最小父级标签
list_foods = bs_foods.find_all('div',class_='info pure-u')
# 创建一个空列表，用于存储信息
list_all = []

for food in list_foods:
    # 提取第0个父级标签中的<a>标签
    tag_a = food.find('a')
    # 菜名，使用[17:-13]切掉了多余的信息
    name = tag_a.text[17:-13]
    # 获取URL
    URL = 'http://www.xiachufang.com'+tag_a['href']
    # 提取第0个父级标签中的<p>标签
    tag_p = food.find('p',class_='ing ellipsis')
    # 食材，使用[1:-1]切掉了多余的信息
    ingredients = tag_p.text[1:-1]
    # 将菜名、URL、食材，封装为列表，添加进list_all
    list_all.append([name,URL,ingredients])

# 打印
print(list_all)