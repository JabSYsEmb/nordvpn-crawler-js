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

def speedtest_ovpn(path):
    st = speedtest.Speedtest()
    for directory in os.scandir(path):
        if(directory.is_dir()):
            speedtest_ovpn(path + "/" + directory.name)
            continue
        elif(directory.is_file() & (directory.name[-5:] == ".ovpn") ):
            process = subprocess.Popen(['./script.sh',  str(path+"/"+directory.name), './auth.txt'])
            time.sleep(1)
            try:
                print('Running in process', process.pid)
                download_speed = st.download()
                sys.stdout.write("{} : {} \n".format(directory.name, humansize(download_speed)))
                os.system("curl https://ipinfo.io/json")
                sys.stdout.write("kill {}\n".format(process.pid))
                os.system("kill {}".format(process.pid))
                time.sleep(2)
                sys.stdout.write("Processed is called\n")
                os.system("curl https://ipinfo.io/json")
                process.communicate(timeout=20)
            except subprocess.TimeoutExpired:
                print('Timed out - killing', process.pid)
                process.kill()
            break
        else:
            sys.stdout.write("We are {}... \n".format(directory))
            time.sleep(1)

def main():
    speedtest_ovpn(".")

if __name__ == "__main__":
    main()
