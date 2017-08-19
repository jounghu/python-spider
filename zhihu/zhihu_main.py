#encoding:utf-8
import download_manager
from zhihu import zhihu_parser_manager,zhihu_url_manager,zhihu_output_manager

class ZhihuMain(object):
    def __init__(self, total_zhihu_users):
        self.download_manager = download_manager.DownLoadManager()
        self.parser_manager = zhihu_parser_manager.ParserManager()
        self.url_manger = zhihu_url_manager.UrlManager(total_zhihu_users)
        self.output_manager = zhihu_output_manager.OutputManager()

    def crawl_zhihu_user(self, zhihu_url):
        page_urls = self.url_manger.add_new_url(zhihu_url)
        count  = 1
        while self.url_manger.has_new_url():
            try:
                new_link_url = self.url_manger.get_new_link_url();
                zhihu_link_html = self.download_manager.download_html(new_link_url)
                zhihu_user_links = self.parser_manager.parse_zhihu_links(zhihu_link_html)
                # 添加到用户信息url集合中
                self.url_manger.add_new_urls(zhihu_user_links)


                new_url = self.url_manger.get_new_url()

                print "crawl times %d, %s"%(count,new_url)

                zhi_user_followers_html = self.download_manager.download_html(new_url)
                user_data= self.parser_manager.parse_zhihu_user(zhi_user_followers_html)

                self.output_manager.collect_user_info(user_data)

                if(count>50):
                    break
                count  = count + 1
            except:
                print "crawl failed!"

        self.output_manager.output_html()

##    思路：
#     从 https://www.zhihu.com/people/harebu root_url 进去
#     添加url的时候 如果是 不包含？page 去访问粉丝数量，并构造新的分页urls返回 从第二页开始
#     一大坑，通过如上界面进去一开始只能看到三个用户
#
##
##
##
##
##
if __name__=="__main__":
    # 爬取100 * 10000 个用户
    total_zhi_users = 10000
    zhihu = ZhihuMain(total_zhi_users)
    zhihu_url = "https://www.zhihu.com/people/harebu"
    # 先去爬取人
    zhihu.crawl_zhihu_user(zhihu_url)
