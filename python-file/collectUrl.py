import util.fileutil
import util.stringutils

dir = 'html'
files = util.fileutil.findAllFile(dir)
for file in files:
#     print(file)
#
# if 1 == 1:
#     file = '0.html'
    path = dir + '/' + file
    with open(path, "r") as f:
        html = f.read()
    sps = html.split('<a')
    for i in range(1,len(sps)):
        url = util.stringutils.cutStr('href="','"',sps[i])
        if url.find('#comments') >= 0:
            print(url)
            util.fileutil.Write_Text('url.txt',url)
