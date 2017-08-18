import urllib2
import download_manager
import output_manager
import url_manager
import parse_manager


class SpiderMain(object):
    def __init__(self):
        self.url_manager = url_manager.UrlManger()
        self.download_manager = download_manager.DownLoadManager()
        self.parse_manager = parse_manager.ParseManager()
        self.output_manager = output_manager.OutPutManager()

    def craw(self, root_url):
        self.url_manager.add_new_url(root_url)
        count = 1;
        while self.url_manager.has_new_url():
           try:
               new_url = self.url_manager.get_new_url()
               html_con = self.download_manager.download_html(new_url)
               new_urls, data_dict = self.parse_manager.parse_html(new_url, html_con)
               self.url_manager.add_new_urls(new_urls)
               self.output_manager.collect_data(data_dict)
               print  "%d   %s" % (count, new_url)
               if count > 20:
                   break
               count = count + 1
           except:
               print "craw fail"


        self.output_manager.output_data()
        self.output_manager.output_mysql()




if __name__ == "__main__":
    root_url = 'http://baike.baidu.com/item/Python'
    spider_main = SpiderMain()
    spider_main.craw(root_url)
