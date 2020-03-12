# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 10:19:46 2019

@author: Administrator

创建word
"""

import docx

doc2 = docx.Document()
doc2.add_paragraph('hei',style='List Bullet')
doc2.save('first.docx')