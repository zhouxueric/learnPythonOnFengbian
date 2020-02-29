import requests
import openpyxl
import json
import time



class Getqqmusic:
    '''公共信息:params,hearders,url'''
    params = {
        't':'0',        
        'p':'1',
        'n':'20',
        'w':'',
        'ct':'24', 'qqmusic_ver': '1298','new_json':'1','remoteplace':'sizer.yqq.song_next',
        'searchid':'64405487069162918','aggr':'1','cr':'1','catZhida':'1','lossless':'0',
        'flag_qc':'0','g_tk':'5381', 'loginUin':'284066224', 'hostUin':'0','format':'json',
        'inCharset':'utf8','outCharset':'utf-8','notice':'0','platform':'yqq.json','needNewCode':'0', 
        } 
    headers = {
        'origin':'https://y.qq.com',
        # 请求来源，本案例中其实是不需要加这个参数的，只是为了演示
        'referer':'https://y.qq.com/portal/search.html',
        # 请求来源，携带的信息比“origin”更丰富，本案例中其实是不需要加这个参数的，只是为了演示
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
        # 标记了请求从什么设备，什么浏览器上发出
        'cookie':'pgv_pvi=1528136704; ptui_loginuin=1263594944; RK=ZgQMiZUGV4; ptcz=12042ec9c80b3465ee17161e55308141b962b7282cfc51e7068d003e02b15263; pgv_pvid=8196016265; ts_uid=8847419840; yqq_stat=0; pgv_info=ssid=s8319235216; pgv_si=s2944559104; ts_refer=www.baidu.com/link; userAction=1; player_exist=1; qqmusic_fromtag=66; _qpsvr_localtk=0.36589674553356555; psrf_access_token_expiresAt=1590736275; psrf_qqopenid=07684D790CBD1EAFDF35B3FF216CF730; qm_keyst=Q_H_L_2Cf3Qv50euAJ-q-21tskctpTIJtfGd9lb1vd69qRsQPh0HHw6--xv6cRKldTOE3; psrf_qqaccess_token=C1B5DE250749C900CABBDFC7481A9456; psrf_qqunionid=A91A0474E985380A4B7A17FFFFEBF5D0; qqmusic_key=Q_H_L_2Cf3Qv50euAJ-q-21tskctpTIJtfGd9lb1vd69qRsQPh0HHw6--xv6cRKldTOE3; psrf_musickey_createtime=1582960275; psrf_qqrefresh_token=2312E8A9F3A6B6B1ADF634A10623B257; uin=284066224; yq_index=0; yplayer_open=1; ts_last=y.qq.com/portal/search.html'
        }
    url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp'
    def __init__(self, singer, page, type_, number=20):
        self.singer = singer
        self.params['w'] = singer
        self.page = int(page)
        self.type_ = int(type_)  #爬取页数
        self.params['t'] = str(type_)   #专辑 t: 8；MV t: 12；歌词't':'7'；歌名't':'0'
        self.params['n'] = str(number)  #每页条目数
    def test(self):
        print(self.params['w'], self.params['p'],self.params['t'],self.params['n'])
class Getsongs(Getqqmusic):
    '''使用歌手名字搜索，
    专辑 't': 8；MV 't': 12；歌词't':7；歌名't':0
    '''
    num = 1
    def __init__(self, singer, page, type_=7, number=20):
        Getqqmusic.__init__(self, singer, page, type_, number)
    def test(self):
        print(self.params['w'], self.params['p'],self.params['t'],self.params['n'])
    def getjson(self,i,params):
        params['p'] = str(i+1)
        res = requests.get(self.url, headers=self.headers, params=params)
        self.json_text = json.loads(res.text)  #调用 json.loads()
    def getlrc(self):
        for i in range(self.page):
            self.getjson(i,self.params)
            # print(self.json_text['data']['lyric']['list'])
            for li in self.json_text['data']['lyric']['list']:
                lrc = li['content']
                for line in lrc.split('\\n'):
                    print(line)
                print('\n>>>>>>>>>>>>>')
    def getmv(self):
        for i in range(self.page):
            self.getjson(i,self.params)
            # print(self.json_text['data']['mv']['list'])
            for mv in self.json_text["data"]["mv"]["list"]:
                print(self.num, mv['mv_name'])
                print('播放链接：https://y.qq.com/n/yqq/mv/v/' + mv['v_id']+'.html\n\n')
                self.num += 1
    def getsong(self):
        '''get the songs list, and save to excle. '''
        wb = openpyxl.Workbook()
        sheet = wb.active
        sheet.title = 'song'
        sheet['A1'] = '序号'
        sheet['B1'] = '歌名'
        sheet['C1'] = '歌手'
        sheet['D1'] = '专辑'
        sheet['E1'] = '时长'
        sheet['F1'] = '链接'
        sheet['G1'] = 'MV链接'
        for i in range(self.page):
            self.getjson(i,self.params)
            for music in self.json_text["data"]["song"]["list"]:
                name = music['name']
                album =  music['album']['name']
                interval = time.strftime('%M:%S', time.gmtime(music['interval']))
                # interval = str(music['interval']//60) + ':' + str(music['interval']%60)
                song_url = 'https://y.qq.com/n/yqq/song/' + music['mid'] + '.html'
                mv_url = 'https://y.qq.com/n/yqq/mv/v/' + music['mv']['vid'] + '.html'
                if music['mv']['vid'] == '':
                    mv_url = '无MV链接'
                # print(self.num, name)
                # print('所属专辑：',album)
                # # 查找播放时长
                # print('播放时长：' + interval)
                # # 查找播放链接
                # print('播放链接:%s\n\n'% song_url)
                sheet.append([self.num, name, self.singer, album, interval, song_url, mv_url])
                wb.save('qqmusic.xlsx')
                self.num += 1
    def menu(self):
        if self.type_ == 7:
            self.getlrc()
        elif self.type_ == 12:
            self.getmv()
        elif self.type_ == 0:
            self.getsong()

class Getcomment(Getsongs):
    '''输入“歌手 歌名”,以空格隔开。
    不同的歌曲，有唯一的topid，因此先通过getid()获取topid,再通过getcomment()获取评论。
    '''
    def __init__(self,singer_song,page=1):
        self.singer_song = singer_song
        self.page = page
    def getid(self):
        params = {
            'ct': '24', 'qqmusic_ver': '1298', 'new_json': '1', 
            'remoteplace': 'txt.yqq.center', 'searchid': '39614776944676191', 
            't': '0', 'aggr': '1', 'cr': '1', 'catZhida': '1', 'lossless': '0', 
            'flag_qc': '0', 'p': '1', 'n': '10', 'w': '周笔畅 思愁', 'g_tk': '5381', 
            'loginUin': '284066224', 'hostUin': '0', 'format': 'json', 'inCharset': 'utf8', 
            'outCharset': 'utf-8', 'notice': '0', 'platform': 'yqq.json', 'needNewCode': '0'
            }
        params['w'] = self.singer_song
        res = requests.get(self.url, headers=self.headers, params=params)
        json_text = json.loads(res.text)
        self.topid = json_text['data']['song']['list'][0]['id']
    def getcomment(self):
        url = 'https://c.y.qq.com/base/fcgi-bin/fcg_global_comment_h5.fcg'
        params = {
            'topid':'254329915',
            'pagenum':'1',
            'loginUin':'0', 'hostUin':'0', 'format':'json', 'inCharset':'utf8',
            'outCharset':'GB2312', 'notice':'0', 'platform':'yqq.json',
            'needNewCode':'0', 'cid':'205360772', 'reqtype':'2',
            'biztype':'1', 'cmd':'6', 'needmusiccrit':'0', 'pagesize':'15',
            'lasthotcommentid':'song_449205_3202544866_44059185', 'domain':'qq.com',
            'ct':'24', 'cv':'10101010', 'g_tk':'5381'  
            }
        self.getid()
        params['topid'] = str(self.topid)
        for i in range(self.page):
            params['pagenum'] = str(i+1)
            res = requests.get(url, headers=self.headers, params=params)
            json_text = json.loads(res.text)   
            for comment in json_text['comment']['commentlist']:
                print(comment['rootcommentcontent'])
                print('-----------------------------------')

if __name__ == '__main__':
    # singer = input('请输入要查询的歌手：')
    # page = input('请输入要查询的页数：')
    # t = int(input('请输入要查询的类型（专辑: 8；MV :12；歌词:7；歌名:0）：'))
    # a = Getsongs(singer,page,t)
    # a.menu()
    singer_song = input('请输入要查询的歌手 歌名，以空格隔开：')
    b = Getcomment(singer_song,2)
    b.getcomment()