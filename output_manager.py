#encoding:utf-8
import pymysql
# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')

class OutPutManager(object):
    def __init__(self):
        self.html_datas = []
        self.connection = pymysql.connect(host='localhost',
                                                       user='root',
                                                       password='123456',
                                                       db='spider',
                                                       charset='utf8',
                                                       cursorclass=pymysql.cursors.DictCursor)


    def output_mysql(self):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute("SET NAMES utf8")
                cursor.execute("SET CHARACTER_SET_CLIENT=utf8")
                cursor.execute("SET CHARACTER_SET_RESULTS=utf8")
                # Create a new record
                sql = "INSERT INTO `baike` (`url`, `title`, `summary`) VALUES (%s, %s, %s)"
                for data in self.html_datas:
                    cursor.execute(sql, (data['url'], data['title'].encode('utf-8'), data['summary'].encode('utf-8')))

                # connection is not autocommit by default. So you must commit to save
                # your changes.
                self.connection.commit()
        except:
            print "save failed"
        finally:
            cursor.close()
            self.connection.close()


    def output_data(self):
        f = open("summary.html","w")

        f.write("<html>")
        f.write("<head>")
        f.write("<title>")
        f.write("爬虫数据")
        f.write("</title>")
        f.write("</head>")
        f.write("<body>")
        f.write("<table border=\"1\">")
        f.write("<thead>")
        f.write("<th>url</th>")
        f.write("<th>summary</th>")
        f.write("</thead>")
        f.write("<tbody>")
        for data in self.html_datas:
            f.write("<tr>")
            f.write("<td>")
            f.write("<a href=\""+data['url']+"\">")
            f.write((data['title'].encode('utf-8')))
            f.write("</a>")
            f.write("</td>")
            f.write("<td>" + data['summary'].encode('utf-8') + "</td>")
            f.write("</tr>")
        f.write("</tbody>")
        f.write("</table>")
        f.write("</body>")
        f.write("</html>")
        f.close()

    def collect_data(self, data_dict):
        if data_dict is None:
            return
        self.html_datas.append(data_dict)