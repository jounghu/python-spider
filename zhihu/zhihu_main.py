import download_manager

class ZhihuMain(object):

    def __init__(self):
        self.download_manager = download_manager.DownLoadManager()


if __name__=="__main__":
    zhihu = ZhihuMain()
    url = "https://www.zhihu.com/people/foruok"
    html = zhihu.download_manager.download_html(url)
    print html
