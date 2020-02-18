#! python3
# -*- coding: utf-8 -*-
# Author: zhouxu
# Version 0.1
import csv

class Book:
    def __init__(self, id, name, author, comment, state):
        self.id = id
        self.name = name
        self.author = author
        self.comment = comment
        self.state = state
        # print('Book.',state)
    
class FictionBook(Book):
    def __init__(self, id, name, author, comment, state=0, type='未分类'):
        # print('FictionBook.',state)
        Book.__init__(self, id, name, author, comment, state) 
        self.type = type  
    def __str__(self): 
        '''
        打印对象即可打印出该方法中的返回值，而无须再调用方法。
        '''
        if self.state == 0:
            status = '未借出'
        else:
            status = '已借出'
        # print('__str__',status)
        return '名称：《%s》 作者：%s 推荐语：%s\n状态：%s 类型：%s' % (self.name, self.author, self.comment, status, self.type)



class BookManager:
    books = [] #书单，元素为Book实例对象
    authors = [] #作者名单
    book_info = {} #储存从文件中读取的信息,并在书籍状态改变或新增时，临时储存数据
    book_ID = 0
    def __init__(self):
        # 利用try-except检查图书馆数据文件是否存在，若不存在则创建文件
        try:
            f = open('my_labrary_book.csv')
            f.close()
        except FileNotFoundError:
            with open('my_labrary_book.csv', 'w+', newline='', encoding='utf-8') as f:
                pass
            print('已创建数据文件 my_labrary_book.csv')
        
        # 读取图书馆数据
        with open('my_labrary_book.csv', 'r+', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # print(type(row)) #<class 'collections.OrderedDict'>
                # print(row['状态'])
                book = FictionBook(row['id'],row['书名'], row['作者'], row['推荐语'], state=int(row['状态']), type=row['类型'])
                # print('book',book.state)
                # 全部信息
                self.book_ID += 1
                self.book_info[self.book_ID] = {'书名':row['书名'], '作者':row['作者'], '推荐语':row['推荐语'],
                                                '状态':int(row['状态']), '类型':row['类型']}
                self.books.append(book)
                self.authors.append(book.author)
                # self.book_info.append({'书名':row['书名'], '作者':row['作者'], '推荐语':row['推荐语'], '状态':row['状态'], '类型':row['类型']})
            # next(reader)
        # print(self.book_info)
    
    def menu(self):
        print('欢迎使用流浪图书管理系统，每本沉默的好书都是一座流浪的岛屿，希望你有缘发现并着陆，为精神家园找到一片栖息地。\n')
        while True:
            print('1.查询所有书籍\n2.添加书籍\n3.借出书籍\n4.归还书籍\n5.查询作者\n6.退出系统\n')
            choice = input('请输入数字选择对应的功能：')
            if choice == '1':
                self.show_all_book()
            elif choice == '2':
                self.add_book()
            elif choice == '3':
                self.lend_book()
            elif choice == '4':
                self.return_book()
            elif choice == '5':
                self.show_author_book()            
            elif choice == '6':
                print('感谢使用流浪图书管理系统，欢迎再次使用！')
                break
    
    def show_all_book(self):
        for book in self.books:
            print(book)   #若Book中无__str__,则输出的其实是一个object和内存地址
        print('本馆一共有%s本书'% self.book_ID)
    
    def add_book(self):
        new_name = input('请输入书名')
        new_author = input('请输入作者')
        new_commend = input('请输入推荐语')
        new_book = FictionBook(self.book_ID,new_name,new_author,new_commend) #创建实例
        # info = [new_name,new_author,new_commend,0,'未分类'] #新书信息，为csv的1行
        self.books.append(new_book) #加入书单
        self.authors.append(new_book.author) #加入作者名单
        self.book_ID += 1
        self.book_info[self.book_ID] = {'书名':new_name, 
                                   '作者':new_author, 
                                   '推荐语':new_commend, 
                                   '状态':int(new_book.state), 
                                   '类型':new_book.type
                                   }
        self.writeCSV(self.book_info)
        print('录入成功！')
        print(new_book)
    
    def lend_book(self):
        '''
        调用check_book()方法，将结果赋给a，a为None或为实例。
        '''        
        name = input('输入你要借的书名：')
        a = self.check_book(name)
        if a == None:
            print('抱歉，图书馆中暂时没有该书！')
        else:
            if a.state == 0:
                print('借出成功！')
                a.state = 1    #改写借出状态
                self.book_info[int(a.id)]['状态'] = 1
                # print(self.book_info) #这一步，self.book_info已经被重置了！！！#什么鬼，'w'>'a'
                self.writeCSV(self.book_info) 
            else:
                print ('很遗憾，该书已被借出！')
    
    def return_book(self):
        name = input('输入你要归还的书名：')
        a = self.check_book(name)  #若该书存在，则a为该书的实例。
        if a == None:
            print('抱歉，图书馆中不存在该书！但你可以向图书馆添加此书！')
        else:
            a.state = 0
            self.book_info[int(a.id)]['状态'] = 0
            self.writeCSV(self.book_info)
            print('归还成功')

    def show_author_book(self):
        author = input('请输入要查询的作者：')
        if author in self.authors:
            for book in self.books:
                if book.author == author:
                    print('本馆%s的著作有《%s》'% (author, book.name))
        else:
            print('暂时还没有该作者的书籍。') 
    
    def writeCSV(self,info_Dict):
        '''传入字典，将其格式化为1维，格式化后写入CSV文件'''
        # 刷新文件 太低级,需要直接操作单元格的方法
        fieldnames = ['id','书名','作者','推荐语','状态','类型']
        with open('my_labrary_book.csv', 'w', newline='', encoding='utf-8') as f:
            # f.truncate()
            writer = csv.DictWriter(f,fieldnames=fieldnames)
            writer.writeheader()

        for k,v in info_Dict.items():
            info_unzip = {'id':int(k),'书名':v['书名'],'作者':v['书名'],'推荐语':v['推荐语'],'状态':int(v['状态']),'类型':v['类型']}
            # print(info_unzip)
            with open('my_labrary_book.csv', 'a+', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f,fieldnames=fieldnames)
                writer.writerow(info_unzip)
    
    def check_book(self,name):
        '''
        检查该书是否存在于图书馆中，即books列表中是否存在name为name的实例。
        存在返回实例book，不存在则返回None。
        '''
        for book in self.books:
            if book.name == name:
                return book
        else:
            return None
    
manager = BookManager()
manager.menu()
