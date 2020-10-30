# ============================================================================ #
# 程序名称：MultiProc_AutoDownload.py
# 程序功能：下载指定部分SEG年会文章并命名
# 参数说明：
#           0) url                     ： 会议文章网页地址
#           1) LIST_of_Section.txt     ： 文件夹名称
#           2) LIST_of_DOI.txt         ： 文献DOI
#           3) LIST_URLs_of_Papers.txt ： 文献地址
#           4) LIST_URLS_of_PDF.txt    ： PDF下载地址
# 依赖关系：
#           1) urllib
#           2) requests
#           3) wegt
#           4) BeautifulSoup
#           5) os
#
# Author：  地球物理界的雷锋
# Data：    2020.10.14
#
# 备注说明：
#           1) 仅供个人阅读使用，禁止商用，虽然也不可能商用，哈哈哈哈哈
#           2) 此程序为主程序的补充程序，可以下载指定范围的论文，这样就可以并行了啊，美滋滋
# ============================================================================ #

import urllib.request
import requests
import wget as wget
import time
import os
from bs4 import BeautifulSoup

# ==========================修改这一部分就行================================== #
i_beg         = 0         #起始文章编号(0-776 in all)
i_end         = 776       #结束文章编号(0-766 in all)
lines         = open('3_LIST_of_URLS_of_PDF.txt').readlines()  #主程序生成的文件
lines_section = open('1_LIST_of_Section.txt').readlines()      #主程序生成的文件

# ===========================以下部分不用修改================================= #
time_start = time.time()

err_count = 0
i_all     = len(lines)
i_seg     = i_end - i_beg
for i_count in range(i_beg,i_end):
    time_start_line=time.time()
    print('This Proc Download [',i_beg,' to 'i_end,']','  No.',i_count+1,'/', i_all,':   ')
    time.sleep(2)
    i_count      = i_count+1

    section_path = lines_section[i_count-1]
    section_path = section_path.replace("\n","")

    url_path     = lines[i_count-1]
    url_pdf_path = url_path.replace("/epdf/","/pdf/")
    url_pdf_path = url_pdf_path.replace("\n","?download = true")
    print('     url_path is :',url_path.replace("\n",""))
    print('     url_pdf_path is : ',url_pdf_path)

    res_getname = requests.get(url_path)
    soup = BeautifulSoup(res_getname.content,'lxml')
    for i in soup.select('title'):
        filename = i.get_text()
        filename = filename.replace("/"," ")
        filename = filename.replace(":"," ")
        filename = './'+section_path+'/'+ filename +".pdf"
        print('     path&title is : ',filename)

    res_getpdf = requests.get(url_pdf_path)

    try:
        with open(filename, 'wb+') as pdf:
            pdf.write(res_getpdf.content)
    except:
        filename  = './' + section_path + '/' +str(i_count)+'_.pdf'
        err_count = err_count+1;
        with open(filename, 'wb+') as pdf:
            pdf.write(res_getpdf.content)

    time_end_line = time.time()
    print('     This Paper cost ',time_end_line-time_start_line,'s')

time_end = time.time()
print('     Step4 cost ',time_end-time_start,'s')

print('\nThe download is complete.')
print('Notice : ',err_count,' papers can not auto_rename!')




