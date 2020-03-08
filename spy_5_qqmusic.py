import requests
import json
from bs4 import BeautifulSoup
# 引用requests模块
def dict_headers(s):
    '''将NETWORK中复制的hearders格式化成字典'''
    return dict([line.split(': ',1) for line in s.split('\n')])
raw_params_list = '''ct: 24
qqmusic_ver: 1298
new_json: 1
remoteplace: txt.yqq.center
searchid: 41093864907415257
t: 0
aggr: 1
cr: 1
catZhida: 1
lossless: 0
flag_qc: 0
p: 1
n: 10
w: 周杰伦
g_tk: 5381
loginUin: 0
hostUin: 0
format: json
inCharset: utf8
outCharset: utf-8
notice: 0
platform: yqq.json
needNewCode: 0'''
params_list = dict_headers(raw_params_list)


def getcomment(p,id):
    url = 'https://c.y.qq.com/base/fcgi-bin/fcg_global_comment_h5.fcg'
    # 请求歌曲评论的url参数前面的部分      
    for i in range(int(p)):
        params = {
        'g_tk':'5381',
        'loginUin':'0', 
        'hostUin':'0',
        'format':'json',
        'inCharset':'utf8',
        'outCharset':'GB2312',
        'notice':'0',
        'platform':'yqq.json',
        'needNewCode':'0',
        'cid':'205360772',
        'reqtype':'2',
        'biztype':'1',
        'topid':id,
        'cmd':'6',
        'needmusiccrit':'0',
        'pagenum':str(i+1),
        'pagesize':'15',
        'lasthotcommentid':'song_449205_3202544866_44059185',
        'domain':'qq.com',
        'ct':'24',
        'cv':'10101010'   
        }
        #不同的歌topid、lasthotcommentid不同。topid为列表中的data.song.list[n].id，或歌词列表中的data.lyric.list[n].songid
        # 将参数封装为字典
        #params参数将上述字典在url中转换为'&pagesize=15&lasthotcommentid=song_102065756_3202544866_44059185&domain=qq.com&ct=24&cv=10101010'
        res_comments = requests.get(url, params=params)
        print(res_comments.url)
        # 调用get方法，下载评论列表
        json_comments = res_comments.json()
        # 使用json()方法，将response对象，转为列表/字典
        list_comments = json_comments['comment']['commentlist']
        # 一层一层地取字典，获取评论列表
        for comment in list_comments:
            # list_comments是一个列表，comment是它里面的元素
            print(comment['rootcommentcontent'])
            # 输出评论
            print('-----------------------------------')
            # 将不同的评论分隔开来

def getlist(p,idol):
    '''get the songs list. 
    p: page number you want to get; idol: singer name
    return json'''
    
    headers_list = {
        'origin':'https://y.qq.com',
        # 请求来源，本案例中其实是不需要加这个参数的，只是为了演示
        'referer':'https://y.qq.com/portal/search.html',
        # 请求来源，携带的信息比“origin”更丰富，本案例中其实是不需要加这个参数的，只是为了演示
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
        # 标记了请求从什么设备，什么浏览器上发出
        'cookie':'pgv_pvi=1528136704; ptui_loginuin=1263594944; RK=ZgQMiZUGV4; ptcz=12042ec9c80b3465ee17161e55308141b962b7282cfc51e7068d003e02b15263; pgv_pvid=8196016265; ts_uid=8847419840; yqq_stat=0; ts_refer=www.pypypy.cn/; pgv_info=ssid=s8319235216; pgv_si=s2944559104; userAction=1; ts_last=y.qq.com/portal/search.html'
        }
    params = {
        'ct':'24',
        'qqmusic_ver': '1298',
        'new_json':'1',
        'remoteplace':'sizer.yqq.song_next',
        'searchid':'64405487069162918',
        't':'0',
        'aggr':'1',
        'cr':'1',
        'catZhida':'1',
        'lossless':'0',
        'flag_qc':'0',
        'p':'1',
        'n':'20',
        'w':'周杰伦',
        'g_tk':'5381',
        'loginUin':'0',
        'hostUin':'0',
        'format':'json',
        'inCharset':'utf8',
        'outCharset':'utf-8',
        'notice':'0',
        'platform':'yqq.json',
        'needNewCode':'0' }   
        #与歌词比较改变结果的就4个参数t=7&p=页数&n=每页条数&w=歌手。
        #专辑 t: 8；MV t: 12；歌词't':'7'；歌名't':'0'
    params['w'] = idol
    url_list = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp'
    num = 1
    for i in range(int(p)):
        params_list['p'] = str(i+1)
        # print(type(params1) == type(params))
        res_music = requests.get(url_list, headers=headers_list, params=params_list)
        res_music.raise_for_status()
        # res_music = res_music.text
        # print(res_music.text)
        json_music = res_music.json()
        print(json_lrc['data']['lyric']['list'])
        for music in json_music["data"]["song"]["list"]:
            print(num, music['name'])
            # print('所属专辑：' + music['album']['name'])
            # # 查找播放时长
            # print('播放时长：' + str(music['interval'])+'秒')
            # # 查找播放链接
            # print('播放链接：https://y.qq.com/n/yqq/song/' + music['mid']+'.html\n\n')
            num += 1
            getcomment(1,music['id'])
            
def getlrc(p, idol, params):
    headers = {
        'origin': 'https://y.qq.com',
        'referer': 'https://y.qq.com/portal/search.html',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36'
    }
    params = {
        'ct':'24',
        'qqmusic_ver': '1298',
        'new_json':'1',
        'remoteplace':'sizer.yqq.song_next',
        'searchid':'64405487069162918',
        'aggr':'1',
        'cr':'1',
        'catZhida':'1',
        'lossless':'0',
        'sem':'1',
        't':'12',
        'p':'1',
        'n':'10',
        'w':'周杰伦',
        'g_tk':'5381',
        'loginUin':'0',
        'hostUin':'0',
        'format':'json',
        'inCharset':'utf8',
        'outCharset':'utf-8',
        'notice':'0',
        'platform':'yqq.json',
        'needNewCode':'0'}
    url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp'
    for i in range(int(p)):
        params['p'] = str(i+1)
        params['w'] = idol
        res_lrc = requests.get(url, headers=headers, params=params)
        res_lrc.raise_for_status()
        # json_lrc = res_lrc.json()
        # # print(json_lrc['data'])
        # for li in json_lrc['data']['lyric']['list']:
        #     lrc = li['content']
        #     for line in lrc.split('\\n'):
        #         print(line)
        #     print('\n>>>>>>>>>>>>>')
        json_lrc = json.loads(res_lrc.text)  #调用 json.loads()
        # print(json_lrc['data']['lyric']['list'])
        for li in json_lrc['data']['lyric']['list']:
            lrc = li['content']
            for line in lrc.split('\\n'):
                print(line)
            print('\n>>>>>>>>>>>>>')

class Getall:
    params = {
        'ct':'24',
        'qqmusic_ver': '1298',
        'new_json':'1',
        'remoteplace':'sizer.yqq.song_next',
        'searchid':'64405487069162918',
        't':'0',
        'aggr':'1',
        'cr':'1',
        'catZhida':'1',
        'lossless':'0',
        'flag_qc':'0',
        'p':'1',
        'n':'20',
        'w':'周杰伦',
        'g_tk':'5381',
        'loginUin':'0',
        'hostUin':'0',
        'format':'json',
        'inCharset':'utf8',
        'outCharset':'utf-8',
        'notice':'0',
        'platform':'yqq.json',
        'needNewCode':'0' } 
    headers = {
        'origin':'https://y.qq.com',
        # 请求来源，本案例中其实是不需要加这个参数的，只是为了演示
        'referer':'https://y.qq.com/portal/search.html',
        # 请求来源，携带的信息比“origin”更丰富，本案例中其实是不需要加这个参数的，只是为了演示
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
        # 标记了请求从什么设备，什么浏览器上发出
        'cookie':'pgv_pvi=1528136704; ptui_loginuin=1263594944; RK=ZgQMiZUGV4; ptcz=12042ec9c80b3465ee17161e55308141b962b7282cfc51e7068d003e02b15263; pgv_pvid=8196016265; ts_uid=8847419840; yqq_stat=0; ts_refer=www.pypypy.cn/; pgv_info=ssid=s8319235216; pgv_si=s2944559104; userAction=1; ts_last=y.qq.com/portal/search.html'
        }
    url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp'
    def __init__(self, writer, page, type_, number=20):
        self.params['w'] = writer
        self.page = page  
        self.type_ = type_  #爬取页数
        self.params['t'] = str(type_)   #专辑 t: 8；MV t: 12；歌词't':'7'；歌名't':'0'
        self.params['n'] = str(number)  #每页条目数
    def test(self):
        print(self.params['w'], self.params['p'],self.params['t'],self.params['n'])
class Getsome(Getall):
    '''专辑 t: 8；MV t: 12；歌词't':'7'；歌名't':'0'
    '''
    num = 1
    def __init__(self, writer, page, type_=7, number=20):
        Getall.__init__(self, writer, page, type_, number)
    def test(self):
        print(self.params['w'], self.params['p'],self.params['t'],self.params['n'])
    def getlrc(self):
        for i in range(self.page):
            self.getjson(i)
            print(self.json_text['data']['lyric']['list'])
            for li in self.json_text['data']['lyric']['list']:
                lrc = li['content']
                for line in lrc.split('\\n'):
                    print(line)
                print('\n>>>>>>>>>>>>>')
    def getjson(self,i):
        self.params['p'] = str(i+1)
        res = requests.get(self.url, headers=self.headers, params=self.params)
        print(res.url)
        self.json_text = json.loads(res.text)  #调用 json.loads()
    def getmv(self):
        for i in range(self.page):
            self.getjson(i)
            print(self.json_text['data']['mv']['list'])
            for mv in self.json_text["data"]["mv"]["list"]:
                print(self.num, mv['mv_name'])
                print('播放链接：https://y.qq.com/n/yqq/mv/v/' + mv['v_id']+'.html\n\n')
                self.num += 1
    def menu(self):
        if self.type_ == 7:
            self.getlrc()
        elif self.type_ == 12:
            self.getmv()

# idol = input('请输入要查询的歌手：')
# page = input('请输入要查询的页数：')
# getlist(page, idol) 
# getlrc(page, idol)           
# getcomment(page)
# a = Getall('周旭',1,0)
a = Getsome('周杰伦',1,7)
# a.test()
a.menu()