#encoding:utf-8
import bs4
import re


class ParserManager(object):
    
    def parse_zhihu_user(self, zhi_user_followers_html):
        soup = bs4.BeautifulSoup(zhi_user_followers_html,"html.parser",from_encoding="utf-8")
        user_info_dict = self.__parse_user_info(soup)
        return user_info_dict


    def parse_zhihu_links(self,zhihu_link_html):
        soup = bs4.BeautifulSoup(zhihu_link_html, "html.parser", from_encoding="utf-8")
        zhihu_user_info_links = self.__parse_user_urls(soup)
        return zhihu_user_info_links

    def parse_zhihu_user_follow(self,zhihu_user_index_html):
        """
        解析用户的关注量和粉丝量
        :param zhihu_user_index_html: 用户首页
        :return:
        """
        soup = bs4.BeautifulSoup(zhihu_user_index_html,"html.parser",from_encoding="utf-8")
        follow_dict = {}
        following_follower = soup.find_all('div', class_="NumberBoard-value")

        #关注量
        num_following = int(following_follower[0].get_text())

        #粉丝数量
        num_followers = int(following_follower[1].get_text())

        follow_dict['following'] = num_following
        follow_dict['followers'] = num_followers
        return follow_dict


    def __parse_user_info(self, soup):
        zhihu_user_info_dict = {}
        # 知乎用户昵称
        zhihu_user_nickname = soup.find('span',class_="ProfileHeader-name").get_text()
        zhihu_user_info_dict['nickname']=zhihu_user_nickname
        # 知乎用户简介
        user_headline = soup.find('span', class_="ProfileHeader-headline").get_text()
        zhihu_user_headline = user_headline if user_headline is not  None and len(user_headline)!=0 else None
        zhihu_user_info_dict['headline'] = zhihu_user_headline
        # 知乎用户性别
        zhihu_user_sex = '男' if soup.find('svg',class_="Icon--male") else '女'
        zhihu_user_info_dict['sex'] = zhihu_user_sex
        # 知乎用户职业
        user_major = soup.find('div', class_="ProfileHeader-infoItem")
        zhihu_user_major = user_major.get_text() if user_major else None
        zhihu_user_info_dict['zhihu_user_major'] = zhihu_user_major

        return zhihu_user_info_dict

    def __parse_user_urls(self, soup):
        #这里每次只能获取三个用户
        user_info_set = set()
        user_info_links = soup.find_all('a', class_="UserLink-link")
        for user_info_link in user_info_links:
            user_info_set.add("http://www.zhihu.com"+user_info_link.get('href'))

        return user_info_set