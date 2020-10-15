set -x
nohup python3 -u main.py > out.log 2>&1 &

tail -f out.log
