#!/usr/bin/env python3

import subprocess
import signal
import time
import sys
import os

import speedtest

def humansize(nbytes):
    suffixes = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']
    i = 0
    while nbytes >= 1024 and i < len(suffixes)-1:
        nbytes /= 1024.
        i += 1
    f = ('%.2f' % nbytes).rstrip('0').rstrip('.')
    return '%s %s' % (f, suffixes[i])

# openvpn --config $1 --auth-nocache --auth-user-pass $2

def speedtest_ovpn(path):
    st = speedtest.Speedtest()
    for directory in os.scandir(path):
        if(directory.is_dir()):
            speedtest_ovpn(path + "/" + directory.name)
            continue
        elif(directory.is_file() & (directory.name[-5:] == ".ovpn") ):
            process = subprocess.Popen(
                [  
                    'openvpn', '--config' , str(path+"/"+directory.name), '--auth-nocache', '--auth-user-pass', './auth.txt' 
                ]
                , stdout = subprocess.DEVNULL
                , stderr = subprocess.DEVNULL
                , restore_signals = False)
            try:
                download_speed = st.download()
                os.system("./myip.sh")
                sys.stdout.write(" - {} : {} \n".format(directory.name, humansize(download_speed)))
                time.sleep(10)
                process.kill()
            except subprocess.TimeoutExpired:
                print('Timed out - killing', process.pid)
                process.kill()
        else:
            sys.stdout.write("We are {}... \n".format(directory))
            time.sleep(1)

def main():
    path = sys.argv[1]
    speedtest_ovpn(path)

if __name__ == "__main__":
    main()