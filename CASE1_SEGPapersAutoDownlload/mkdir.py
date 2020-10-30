# ============================================================================ #

import urllib.request
import requests
import wget as wget
import time
import os
from bs4 import BeautifulSoup

# ============================================================================ #
# Step 1 :Get URLs and DOI
# ============================================================================ #
''' get_urls_doi '''
def get_urls_doi:
    # Step 1.1 : 读取单篇文章的DOI
    print('Step 1.1 : Get DOI of papers is begin')
    time_start = time.time()
    url  = "https://library.seg.org/doi/book/10.1190/segeab.39"
    res  = requests.get(url)
    soup = BeautifulSoup(res.content,'lxml')
    fp = open('1_LIST_of_DOI.txt', 'w')
    for i in soup.select('div[class="issue-item__doi"]'):
        s = i.get_text()+'\n';
        fp.write(s)
    fp.close()
    time_end = time.time()
    print('Step 1.1 : Get DOI of papers is finish')
    print('Step 1.1 cost ' time_end-time_start,' s')

    # Step 1.2 : 读取单篇文章的SECTION并创建文件夹
    print('Step 1.2 : Get name of section and make direction is begin')
    time_start = time.time()
    filename='temp'
    fp = open('1_LIST_of_Section.txt', 'w')
    i_count=0
    for i in soup.select('div[class="titled_issues"]'):
        i_count=i_count+1
        try:
            filename = i.h4.string+'\n'
        except:
            filename

        print(i_count,filename)
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

    time_end=time.time()
    print('Step 1.2 : Get name of section and make direction is finsh')
    print('Step 1.2 cost ',time_end-time_start,' s')

    # Step 1.3 : Get URLs of Papers
    print('Step 1.3 : Get URLs of Papers is Begin')
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
    print('Step 1.3 : Get URLs of papers is finsh')
    print('Step 1.3 cost ',time_end-time_start,'s')

# ============================================================================ #











