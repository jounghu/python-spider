
from sdju import sdju_download ,sdju_parser, sdju_output

class SdjuMain(object):
    def __init__(self):
        self.sdju_download = sdju_download.SdjuDownload()
        self.sdju_parser = sdju_parser.SdjuParser()
        self.sdju_output = sdju_output.SdjuOutput()
    pass

    def crawl_sore(self):
        login_state_code = self.sdju_download.do_login()
        score_html = self.sdju_download.down_score_html(login_state_code)
        score_datas = self.sdju_parser.parse_score(score_html)
        print score_datas
        self.sdju_output.output_mysql(score_datas)


if __name__=="__main__":
    sdju_main = SdjuMain()
    sdju_main.crawl_sore()
