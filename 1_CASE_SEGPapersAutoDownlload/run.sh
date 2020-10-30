set -x
nohup python3 -u auto_download.py > out.log 2>&1 &

tail -f out.log
