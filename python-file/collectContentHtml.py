import util.stringutils
from selenium import webdriver
import util.fileutil
import os

with open('url.txt','r') as f:
    datas = f.readlines()

dir = 'contentHtml'
browser = webdriver.Chrome()
for data in datas:
# if 1==1:
#     data = 'https://music.douban.com/review/12512247/#comments'
    ourl = data.strip()
    id = util.stringutils.cutStr('review/','/',ourl)
    for page in range(0,50):
        path = dir + '/' + id + '_' + str(page) + '.html'
        isExists = os.path.exists(path)
        if isExists:
            print('存在:'+path)
            continue
        nurl = 'https://music.douban.com/review/' + id + '/?start='+ str(page * 100) +'#comments'
        print(nurl)
        browser.get(nurl)
        html = browser.page_source
        # print(html)
        if html.find('\'comments\':') >= 0:
            comments = util.stringutils.cutStr('\'comments\':',']',html)
            if comments.strip() == '[' and page != 0:
                break
            print(comments)
            util.fileutil.mkdir(dir)

            util.fileutil.Write_html(path, html)
        else:
            print('没采到:'+path)
