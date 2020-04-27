import requests

header = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'}
url = 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-login.php'
data = {'log':'spiderman',
'pwd': 'crawler334566',
'rememberme': 'forever',
'wp-submit': '登录',
'redirect_to': 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn',
'testcookie': '1'}
login = requests.post(url, headers=header,data=data)
print(login.status_code)
cookies = login.cookies
# print(cookies)
url2 = 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-comments-post.php'
data2 = {'comment': 'heiheiheiheiheiheiheihei',
'submit': '发表评论',
'comment_post_ID': '23',
'comment_parent': '0'}
comment = requests.post(url2,headers=header,data=data2,cookies=cookies)
print(comment.status_code)
