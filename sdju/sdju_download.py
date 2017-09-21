import re
import requests
import sys
import bs4
import json

reload(sys)
sys.setdefaultencoding('utf-8')
class SdjuDownload(object):
    def __init__(self):
        self.sdju_login_url = "http://jwgl.sdju.edu.cn:81/jxfw_web/Home/Login/login"
        self.login_payload = {
            'username': 'xxxxxxxxxx',
            'password': 'xxxxxxxxxx'
        }
        self.score_html_url = 'http://jwgl.sdju.edu.cn:81/jxfw_web/Home/Jxgl/xscjcx'
        self.session_request = requests.session()


    def do_login(self):
        state = self.session_request.post(self.sdju_login_url,self.login_payload)
        return state.content

    def down_score_html(self, login_state_code):
        if login_state_code is not str(1) or login_state_code != str(1):
            return None

        payloads = self._download_xns()
        if payloads is None or len(payloads)==0:
            return None

        score_datas = []
        for payload in payloads:
            score_data = self.session_request.post(self.score_html_url,payload)
            score_datas.append(json.loads(score_data.content))
        return score_datas

    def _download_xns(self):
        xns_html = self.session_request.get(self.score_html_url)
        if xns_html.content is None or len(xns_html.content) == 0:
            return None

        soup = bs4.BeautifulSoup(xns_html.content,"html.parser",from_encoding='utf-8')
        xns = soup.find("select", id='xn').find_all('option', value=re.compile(r"\d{4}-\d{4}"))
        payloads = []

        for payload in xns:
            payloads.append(dict(xn=payload.get_text(),xq="1"))
            payloads.append(dict(xn=payload.get_text(), xq="2"))

        return payloads
