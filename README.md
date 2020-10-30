#CASE1 : `Auto Download Papers From url & Rename the PDF`<br>
#CASE1功能:下载2020SEG年会文章，按照SECTION创建文件夹，PDF按照SECTION和PaperTitle存储<br>

>> How to run it :<br>
>>>>``python3 auto_download.py`` or ``./run.sh``<br>

>>>>>> notice : <br>
>>>>>>>> * you can run it step by step.<br>
>>>>>>>> * make sure you have the right to download the paper.<br>
>>>>>>>> * give a enough sleep_time (in Step 4).<br>
>>>>>>>> * mian.py 是一个补充函数``python3 main.py`` ，但是注意不要频繁访问,不然可能会被封网(不要问我为什么知道，而且看起来是封3个小时)<br>



#CASE2: `Frequency Analysis By Matplotlib & Armadillo`<br>
#CASE2功能:众所周知，Python绘图相当好看，这次探索下Matplotlib，看样子和Matlab差不多<br>

>> How to run it : <br>
>>>>提取不同频带：``./run.sh`` or ``g++ main.cpp -lpowershen``<br>
>>>>绘图：``python3 pyshow.py``<br>

>>>>>> notice :<br>
>>>>>>>> * 提取不同频带中，用到``lib_shen``，这个库我似乎还没公开，没关系，主要看``pyshow.py``<br>
>>>>>>>> * 说的好像有人会看似得，哈哈哈哈哈哈<br>

