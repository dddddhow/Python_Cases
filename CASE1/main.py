# ============================================================================ #
# 程序名称：main.py
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
#           2) 并行版本
# ============================================================================ #

import urllib.request
import requests
import time
import os
from bs4 import BeautifulSoup
from multiprocessing import Process
import multiprocessing

# Sub_function 1 ============================================================= #
''' get_urls_doi '''
def Sub_func1():
    # Step 1.1 : 读取单篇文章的DOI
    print('Step 1.1 : Get DOI of papers is begin')
    time_start_1 = time.time()
    url  = "https://library.seg.org/doi/book/10.1190/segeab.39"
    res  = requests.get(url)
    soup = BeautifulSoup(res.content,'lxml')
    fp = open('1_LIST_of_DOI.txt', 'w')
    for i in soup.select('div[class="issue-item__doi"]'):
        s = i.get_text()+'\n';
        fp.write(s)
    fp.close()
    time_end_1 = time.time()
    print('     Step 1.1 : Get DOI of papers is finish')
    print('     Step 1.1 cost ' ,time_end_1-time_start_1,' s')

    # Step 1.2 : 读取单篇文章的SECTION并创建文件夹
    print('Step 1.2 : Get name of section and make direction is begin')
    time_start_2 = time.time()
    filename='temp'
    fp = open('1_LIST_of_Section.txt', 'w')
    i_count=0
    for i in soup.select('div[class="titled_issues"]'):
        i_count=i_count+1
        try:
            filename = i.h4.string+'\n'
        except:
            filename

        # print(i_count,filename)
        fp.write(filename)
    fp.close()

    lines = open('1_LIST_of_Section.txt').readlines()
    i_count=0
    for s in lines:
        i_count=i_count+1
        try:
            s=s.replace("\n","")
            s=s.replace("/"," ")
            flag_dir=os.path.exists(s)
            if not flag_dir:
                os.mkdir(s)
                print("     mkdir ",s)
        except:
            s=str(i_count)
            flag_dir=os.path.exists(s)
            if not flag_dir:
                os.mkdir(s)
                print("     mkdir ",s)

    time_end_2=time.time()
    print('     Step 1.2 : Get name of section and make direction is finsh')
    print('     Step 1.2 cost ',time_end_2-time_start_2,' s')
    print('Step 1 : Get DOI and make direaction is finsh')
    print('Step 1 cost ',time_end_2-time_start_1,' s')


# Sub_function 2 ============================================================= #
''' get_urls '''
def Sub_func2():
    print('Step 2 : Get URLs of Papers is Begin')
    time_start = time.time()

    lines = open('1_LIST_of_DOI.txt').readlines()
    fp = open('2_LIST_of_URLs_of_Papers.txt', 'w')
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    }

    data = {
        'poster': 'test',
        'syntax': 'cpp',
        'content': 'test',
    }

    for s in lines:
        res = requests.post(url=s, headers=headers, data=data, allow_redirects=False)
        fp.write(res.headers['location']+'\n')
        print(res.headers['location']) #显示进度 好慢啊

    fp.close()
    time_end = time.time()
    print('Step 2 : Get URLs of papers is finsh')
    print('Step 2 cost ',time_end-time_start,'s')


# Sub_function 3 ============================================================= #
def Sub_func3():
    print('Step 3 : Get URLs of PDF is Begin')
    time_start = time.time()
    lines = open('2_LIST_of_URLs_of_Papers.txt').readlines()
    fp = open('3_LIST_of_URLS_of_PDF.txt', 'w')
    for s in lines:
        s = s.replace("library.seg.org/doi/", "library.seg.org/doi/epdf/")
        fp.write(s)
        # print(s)
    fp.close()
    time_end = time.time()
    print('Step 3 : Get URLs of PDF is finsh')
    print('Step 3 cost ',time_end-time_start,'s')


# Sub_function 2 ============================================================= #
''' sigle proc '''
def single_proc(i_count):
    time.sleep(5)
    lines= open('3_LIST_of_URLS_of_PDF.txt',encoding='utf-8', errors='ignore').readlines()
    lines_section = open('1_LIST_of_Section.txt',encoding='utf-8', errors='ignore').readlines()
    i_all=len(lines)
    time_start_line=time.time()
    print(multiprocessing.current_process().name,' No.',i_count+1,'/', i_all,':   ')
    i_count      = i_count+1

    section_path = lines_section[i_count-1]
    section_path = section_path.replace("\n","")

    url_path     = lines[i_count-1]
    url_pdf_path = url_path.replace("/epdf/","/pdf/")
    url_pdf_path = url_pdf_path.replace("\n","?download = true")
    print('     url_path is :',url_path.replace("\n",""))
    print('     url_pdf_path is : ',url_pdf_path)

    res_getname = requests.get(url_path)
    soup = BeautifulSoup(res_getname.content,'html.parser')
    for i in soup.select('title'):
        filename = i.get_text()
        filename = filename.replace("/"," ")
        filename = filename.replace(":"," ")
        filename = './'+section_path+'/'+filename +".pdf"
        print('     path&title is : ',filename)

    res_getpdf = requests.get(url_pdf_path)

    try:
        with open(filename, 'wb+') as pdf:
            pdf.write(res_getpdf.content)
    except:
        filename  = './'+section_path+'/'+str(i_count)+'_.pdf'
        err_count = err_count+1;
        with open(filename, 'wb+') as pdf:
            pdf.write(res_getpdf.content)

    time_end_line = time.time()
    print('     This Paper cost ',time_end_line-time_start_line,'s')


# ============================================================================ #
if __name__ == '__main__':
    time_main_beg=time.time()

    # Step 1 :
    Sub_func1()

    # Step 2 :
    Sub_func2()

    # Step 3 :
    Sub_func3()

    # Step 4 :
    print('Step 4 : Auto download is Begin')
    lines= open('3_LIST_of_URLS_of_PDF.txt',encoding='utf-8', errors='ignore').readlines()
    i_all=len(lines)
    time_start_4=time.time()
    pool = multiprocessing.Pool(processes=1)
    for i in range(i_all):
        pool.apply_async(single_proc,(i, ))
    pool.close()
    pool.join()
    time_end_4=time.time()
    print('Step 4 : Auto download is finish')
    print('Step 4 cost ',time_end_4-time_start_4,'s')

    time_main_end=time.time()
    print("This Program Cost ",time_main_end-time_main_beg," s")
