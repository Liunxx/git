#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/28 16:48
# @Version    : 3.6
# @File    : table_to_csv.py
# @Software: PyCharm
import re
import csv

class table_to_csv(object):
    def __init__(self):
        pass
    def find_result(self,htmlpage,index):
        result=[]
        htmlpage=htmlpage.replace('\n',' ')
        table_contents=re.findall(r'<table.*?>(.*?)</table.*?>',htmlpage,re.IGNORECASE)
        if self.check_type(table_contents):
            for table_content in table_contents:
                 th_content=re.findall(r'<th.*?>(.*?)</th.*?>',table_content,re.IGNORECASE)
                 if th_content:
                     result.append(th_content)
                 tr_contents=re.findall(r'<tr.*?>(.*?)</tr.*?>',table_content,re.IGNORECASE)
                 if self.check_type(tr_contents):
                     for tr_content in tr_contents:
                         td_content=re.findall(r'<td.*?>(.*?)</td.*?>',tr_content,re.IGNORECASE)
                         if td_content:
                             for i in range(len(td_content)):
                                  rest_content=re.findall(r'<.*?>|</.*?>',td_content[i],re.IGNORECASE)
                                  if rest_content:
                                      contents=re.findall(r'<.*?>(.*?)</.*?>',td_content[i],re.IGNORECASE)
                                      for content in contents:
                                          td_content[i]=content
                                  if td_content[i]=='':
                                      td_content[i]=' '
                             result.append(td_content)

        self.write_csv(result,index)
    def check_type(self,findresult):
        if findresult:
            return True
        else:
            raise TypeError('Html type error!')
            return False
    def write_csv(self,contents,i):
        csvFile=open('out%s.csv'%i,'w')
        writer=csv.writer(csvFile)
        for content in contents:
            if len(content)!=0:
                writer.writerow(content)
        csvFile.close()
    def read_html(self,name):
        htmlfile=open(name,'r')
        htmlpage=htmlfile.read()
        return htmlpage
        print(htmlpage)

if __name__ == "__main__":
    tc=table_to_csv()
    html_cont=tc.read_html('in1.html')
    tc.find_result(html_cont,1)