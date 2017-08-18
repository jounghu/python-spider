import bs4
import re
import urlparse




class ParseManager(object):


    def parse_html(self, page_url, html_con):
        if page_url is None or html_con is None:
            return
        soup = bs4.BeautifulSoup(html_con, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        html_data = self._get_html_data(page_url, soup)
        return new_urls,html_data


    def _get_new_urls(self, new_url, soup):
        new_urls = set()
        urls = soup.find_all('a', href=re.compile(r"/item/*"))
        for url in urls:
            new_urls.add(urlparse.urljoin(new_url,url.get('href')))
        return new_urls

    def _get_html_data(self, page_url, soup):
        html_data = {}
        html_data['url'] = page_url
        # <dd class="lemmaWgt-lemmaTitle-title">
        #   <h1>Python</h1>
        title = soup.find('dd',class_=re.compile(r"lemmaWgt-lemmaTitle-title")).find('h1').get_text()
        html_data['title']=title

        # <div class="lemma-summary" label-module="lemmaSummary">
        summary = soup.find('div',class_=re.compile(r"lemma-summary")).get_text()
        html_data['summary']=summary
        return html_data