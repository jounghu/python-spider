import re
import requests
import json
import sys
import bs4
import sdju_parser

reload(sys)
sys.setdefaultencoding('utf-8')

session_requests = requests.session()
login_url = "http://jwgl.sdju.edu.cn:81/jxfw_web/Home/Login/login"

payload = {
    "username":'xxxx',
    "password":'xxxxx'
}

result = session_requests.post(
    login_url,
    data= payload,
    headers = dict(referer=login_url)
)

print result.content


print result.content == str(1)



# cj_cx_url = "http://jwgl.sdju.edu.cn:81/jxfw_web/Home/Jxgl/xscjcx"
#
# cj_html = session_requests.get(cj_cx_url)
#
#
# soup = bs4.BeautifulSoup(cj_html.content, 'html.parser', from_encoding='utf-8')
#
# xns = soup.find("select",id='xn').find_all('option',value=re.compile(r"\d{4}-\d{4}"))
#
# xn_dict = []
#
# for xn_option in xns:
#     xn_dict.append(dict(xn=xn_option.get_text(),xq="1"))
#     xn_dict.append(dict(xn=xn_option.get_text(),xq="2"))
#
#
#
# def parse_socre(socre_html):
#     socre_data_list = json.loads(socre_html)
#     socre_data = socre_data_list.get('list')
#     print socre_data_list.get('msg')
#     if socre_data is None :
#         return
#
#     for score in socre_data:
#         print score['kcdm'],score['kcmc'],score['kcxz'],score['xf'],score['cj']
#
#     print "\n"
# html_contents = []
# for socre_dict in xn_dict:
#     socre_html = session_requests.post(cj_cx_url,socre_dict)
#     # parse_socre(socre_html.content)
#
#     html_contents.append(socre_html.content)
#
# datas = sdju_parser.SdjuParser().parse_score(html_contents)
# print datas
#
#
#
#
