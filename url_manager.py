#encoding:utf-8

class UrlManger(object):
    def __init__(self):
        """
            这里维护两个url set
        """
        self.new_url_set = set()
        self.old_url_set = set()

    def add_new_url(self, root_url):
        if root_url is None:
            return

        if root_url  not in self.new_url_set and root_url not in self.old_url_set:
            self.new_url_set.add(root_url)


    def add_new_urls(self, new_urls):
        if new_urls is None or len(new_urls)==0  :
            return
        for new_url in new_urls:
            self.add_new_url(new_url)

    def has_new_url(self):
       return len(self.new_url_set) !=0

    def get_new_url(self):
        if self.new_url_set is None and len(self.new_url_set) == 0:
            return
        else:
            new_url = self.new_url_set.pop()
            self.old_url_set.add(new_url)
            return new_url

    def get_size(self):
        return len(self.new_url_set)