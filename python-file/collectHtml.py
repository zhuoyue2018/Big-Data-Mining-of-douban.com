from selenium import webdriver
import util.fileutil

browser = webdriver.Chrome()

dir = 'html'
for page in range(17):
    url = 'https://music.douban.com/subject/35030138/reviews?start='+str(page*20)
    browser.get(url)
    html = browser.page_source
    util.fileutil.mkdir(dir)
    path = dir + '/' + str(page) + '.html'
    util.fileutil.Write_html(path, html)