#encoding:utf-8
import pymysql


class SdjuOutput(object):
    def __init__(self):
        self.connection = pymysql.connect(host='localhost',
                                          user='root',
                                          password='123456',
                                          db='spider',
                                          charset='utf8',
                                          cursorclass=pymysql.cursors.DictCursor)

    def output_mysql(self, score_datas):
        try:
            cursor = self.connection.cursor()
            for score_data in score_datas:
                    # Create a new record
                    sql = "INSERT INTO `sdju_score` (`kcdm`, `kcmc`, `kcxz`, `xf`, `cj`) VALUES (%s, %s, %s, %s, %s)"
                    cursor.execute(sql, (
                    score_data['kcdm'], score_data['kcmc'], score_data['kcxz'], score_data['xf'], score_data['cj']))
                    self.connection.commit()
        except:
            print "导入失败！"
        finally:
            cursor.close()
            self.connection.close()