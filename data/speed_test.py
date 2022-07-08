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
                    'openvpn',
                    '--config',
                    str(path+"/"+directory.name),
                    '--auth-nocache',
                    '--auth-user-pass',
                    './auth.txt' 
                ],
                stdout = subprocess.DEVNULL,
                stderr = subprocess.DEVNULL,
                restore_signals = False,
                preexec_fn = os.setsid
            )
            try:
                download_speed = st.download()
                subprocess.run( ["./myip.sh", directory.name, humansize(download_speed)] )
                time.sleep(2)
            except ( subprocess.SubprocessError, subprocess.CalledProcessError ) as subprocessError:
                print(subprocessError)
                print('Timed out - killing', process.pid)
            finally:
                os.kill(process.pid, signal.SIGTERM)  # Send the signal to all the process groups
        else:
            time.sleep(1)

def main():
    path = sys.argv[1]
    speedtest_ovpn(path)

if __name__ == "__main__":
    main()
