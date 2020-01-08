
with open(r'd:\桌面\python\知识截图\code.png','rb') as f:
    contener = f.read()
    with open(r'd:\桌面\python\知识截图\code1.png','wb') as f:
        f.write(contener)