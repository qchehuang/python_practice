from urllib import request

def visit_baidu():
    URL = "http://www.baidu.com"
    req = request.urlopen(URL)
    html = req.read()
    html = html.decode("utf_8")
    print(html)

if __name__ == '__main__':
    visit_baidu()
    print('test')