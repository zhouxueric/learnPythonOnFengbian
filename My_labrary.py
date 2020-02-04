class Book:
    def __init__(self, name, author, comment, state = 0):
        self.name = name
        self.author = author
        self.comment = comment
        self.state = state
    
class FictionBook(Book):
    def __init__(self, name, author, comment, state = 0, type = '虚构类'):
        Book.__init__(self, name, author, comment, state = 0)  
        self.type = type  
    def __str__(self): 
        '''
        打印对象即可打印出该方法中的返回值，而无须再调用方法。
        '''
        if self.state == 0:
            status = '未借出'
        else:
            status = '已借出'
        return '类型：%s 名称：《%s》 作者：%s 推荐语：%s\n状态：%s ' % (self.type, self.name, self.author, self.comment, status)



class BookManager:
    books = []
    authors = []
    def __init__(self):
        book1 = FictionBook('惶然录','费尔南多·佩索阿','一个迷失方向且濒于崩溃的灵魂的自我启示，一首对默默无闻、失败、智慧、困难和沉默的赞美诗。')
        book2 = FictionBook('以箭为翅','简媜','调和空灵文风与禅宗境界，刻画人间之缘起缘灭。像一条柔韧的绳子，情这个字，不知勒痛多少人的心肉。')
        book3 = FictionBook('心是孤独的猎手','卡森·麦卡勒斯','我们渴望倾诉，却从未倾听。女孩、黑人、哑巴、醉鬼、鳏夫的孤独形态各异，却从未退场。')
        book4 = FictionBook('撒哈拉的故事','三毛','我每想你一次，天上便落下一粒沙，从此便有了撒哈拉。')
        book5 = FictionBook('梦里花落知多少','三毛','人人都曾拥有荷西，虽然他终会离去。')
        book6 = FictionBook('月亮与六便士','毛姆','满地都是六便士，他却抬头看见了月亮。')
        self.books = [book1,book2,book3,book4,book5,book6]  #注意！！！列表中的元素为Book的实例，而非FictionBook.__str__输出的内容
        # 将实例放在列表books里
        self.authors = [book1.author,book2.author,book3.author,book4.author,book5.author,book6.author]
        # self.authors.append(book3.author)
        # 将实例的作者名添加到列表author里
    
    def menu(self):
        print('欢迎使用流浪图书管理系统，每本沉默的好书都是一座流浪的岛屿，希望你有缘发现并着陆，为精神家园找到一片栖息地。\n')
        while True:
            print('1.查询所有书籍\n2.添加书籍\n3.借出书籍\n4.归还书籍\n5.查询作者\n6.退出系统\n')
            choice = input('请输入数字选择对应的功能：')
            if choice == '1':
                # print(self.books[0])
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
    
    def show_author_book(self):
        author = input('请输入要查询的作者：')
        if author in self.authors:
            for book in self.books:
                if book.author == author:
                    print('《%s》'% book.name)
        else:
            print('暂时还没有该作者的书籍。')            
    
    def show_all_book(self):
        for book in self.books:
            print(book)   #若Book中无__str__,则输出的其实是一个object和内存地址
    
    def add_book(self):
        new_name = input('请输入书名')
        new_author = input('请输入作者')
        new_commend = input('请输入推荐语')
        new_book = FictionBook(new_name,new_author,new_commend) #创建实例
        print(new_book)
        self.books.append(new_book)
        self.authors.append(new_book.author)
        print('录入成功！')
    
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
            else:
                print ('很遗憾，该书已被借出！')
    
    def return_book(self):
        name = input('输入你要归还的书名：')
        a = self.check_book(name)  #若该书存在，则a为该书的实例。
        if a == None:
            print('抱歉，图书馆中不存在该书！但你可以向图书馆添加此书！')
        else:
            a.state = 0
            print('归还成功')

manager = BookManager()
manager.menu()