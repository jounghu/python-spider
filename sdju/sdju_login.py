import re
import requests
import ast
import sys
import bs4

reload(sys)
sys.setdefaultencoding('utf-8')


session_requests = requests.session()

login_url = "http://jwgl.sdju.edu.cn:81/jxfw_web/Home/Login/login"

payload = {
    "username":'xxxx',
    "password":'xxxx'
}

result = session_requests.post(
    login_url,
    data= payload,
    headers = dict(referer=login_url)
)

print result.content




cj_cx_url = "http://jwgl.sdju.edu.cn:81/jxfw_web/Home/Jxgl/xscjcx"

cj_paylaod = {
    "xn":"2016-2017",
    "xq":"1"
}


score_html = session_requests.post(cj_cx_url,cj_paylaod)

cj_html = session_requests.get(cj_cx_url)


soup = bs4.BeautifulSoup(cj_html.content, 'html.parser', from_encoding='utf-8')

xns = soup.find("select",id='xn').find_all('option',value=re.compile(r"\d{4}-\d{4}"))
for xn in xns:
    print  xn.get_text()


# xqs = soup.find("select",id='xq').find_all('option',value=re.compile(r"\d"))
#
# for xq in xqs:
#     print xq.get_text()