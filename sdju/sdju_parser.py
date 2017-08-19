#encoding:utf-8
import json


class SdjuParser(object):
    def parse_score(self, score_htmls):
        # {"list":null,msg:"这是你多少学年的成绩"}
        if score_htmls is None:
            return None

        score_datas = []
        for score_html in score_htmls:
            score_list = score_html.get('list')
            # print score_list
            if score_list is not  None:
                for score in score_list:
                    score_dict = {}
                    score_dict['kcdm']=score['kcdm']
                    score_dict['kcmc']=score['kcmc']
                    score_dict['kcxz']=score['kcxz']
                    score_dict['xf']=score['xf']
                    score_dict['cj']=score['cj']
                    score_datas.append(score_dict)
        return  score_datas